#!/usr/bin/env python3
"""
sync_bazaar.py — scrape Seeed bazaar product pages for certifications &
resources, then archive them into this repository.

Discovery
---------
Product pages are discovered automatically from the migrated wiki
(Documentation/NVIDIA_Jetson/**) by extracting store links, or supplied
explicitly via --products <tsv>.

For every product page the Seeed GraphQL endpoint is queried for:
  - certification_info_eccn / certification_info  -> certificate PDFs
  - documents                                     -> datasheets / 3D / SCH / firmware
  - certification_info_part                       -> part-list links (optional)
plus the bazaar-exclusive per-SKU PDF:
  https://files.seeedstudio.com/Bazaar/product_pdf/{SKU}.pdf

Routing
-------
A slug->folder rule table maps each store product to a product folder under
"reComputer Jetson carrier board/" or "reServer Jetson carrier board/".
Certificates land in <product>/Certificate/, every other resource is routed by
type into the product subfolder: Datasheet/ (PDFs & SKU pages), 3D Model/
(.stp/.step/.stl), Schematic/ (DSN & *_SCH*.pdf), Layout/ (.brd),
Mechanical/ (.dxf/.dwg), Manual/ (guides & manuals), Firmware/ (drivers/BSP).
A per-product manifest is written to Resources/_bazaar_download_report.md.

Usage
-----
  python3 scripts/sync_bazaar.py [--repo .] [--products file.tsv] [--dry-run]
                                 [--limit N] [--workers 8]

Dependencies: Python >= 3.8 stdlib only (urllib, concurrent.futures, curl).
"""
import argparse
import concurrent.futures
import json
import pathlib
import re
import subprocess
import sys
import urllib.parse
import urllib.request

GRAPHQL = "https://www.seeedstudio.com/graphql"
ATTR_CODES = ["certification_info_eccn", "certification_info", "documents"]
CERT_PREFIX = "https://files.seeedstudio.com/Seeed_Certificate/documents_certificate/"
BAZAAR_PDF = "https://files.seeedstudio.com/Bazaar/product_pdf/{sku}.pdf"
STORE_LINK_RE = re.compile(r"https://www\.seeedstudio\.com/([A-Za-z0-9-]+)-p-(\d+)\.html")
SKU_RE = re.compile(r"^sku:\s*(.+)$", re.M)
RES_EXTS = (".pdf", ".stp", ".step", ".stl", ".dxf", ".dwg", ".zip", ".7z", ".rar", ".tar.gz")

RECOMP = "reComputer Jetson carrier board"
RESERV = "reServer Jetson carrier board"

# (slug regex, repo dir) — first match wins
ROUTING = [
    # reComputer series
    (r"^reComputer-Industrial-J2011$|^reComputer-Industrial-J2012$", f"{RECOMP}/reComputer Industrial J201"),
    (r"^reComputer-Industrial-J30(10|11)$|^reComputer-Industrial-J40(11|12)$", f"{RECOMP}/reComputer Industrial J30-J40"),
    (r"^reComputer-J101-v2", f"{RECOMP}/reComputer J101"),
    (r"^reComputer-J1020-v2", f"{RECOMP}/reComputer J1020 v2"),
    (r"^reComputer-J2021$|^recomputer-j202-carrier-board", f"{RECOMP}/reComputer J202"),
    (r"^reComputer-J30(10|11)$|^reComputer-J40(11|12)$", f"{RECOMP}/reComputer J401"),
    (r"^reComputer-J30(10|11)-w-o-power|^reComputer-J40(11|12)-w-o-power", f"{RECOMP}/reComputer J401"),
    (r"^reComputer-J30(10|11)B$|^reComputer-J40(11|12)B$", f"{RECOMP}/reComputer J401B"),
    (r"^reComputer-J401-Carrier-Board", f"{RECOMP}/reComputer J401"),
    (r"^reComputer-Super-J30|^reComputer-Super-J40", f"{RECOMP}/reComputer Super J401"),
    (r"^reComputer-Mini-J4012-with-Extension", f"{RECOMP}/reComputer Mini J401"),
    (r"^reComputer-Mini-J501", f"{RECOMP}/reComputer Mini J501"),
    (r"^reComputer-Robotics-J30|^reComputer-Robotics-J4012|^reComputer-Robotics-Carrier-board", f"{RECOMP}/reComputer Robotics J401"),
    (r"^reComputer-Robotics-J501(1|2)", f"{RECOMP}/reComputer Robotics J501"),
    (r"^reComputer-Robotics-J601|^reComputer-J601-Carrier", f"{RECOMP}/reComputer Robotics J601"),
    (r"^reComputer-Classic-J501", f"{RECOMP}/reComputer Classic J501"),
    (r"^reComputer-Rugged", f"{RECOMP}/reComputer Rugged J401"),
    (r"^reComputer-J101-Bundle", f"{RECOMP}/reComputer J101"),
    (r"^reComputer-Jetson-20-1-H[12]$|^reServer-Jetson-20-1-H2$", f"{RESERV}/reServer J2032"),
    (r"^reServer-industrial-J30|^reServer-industrial-J40", f"{RESERV}/reServer Industrial J30-J40"),
    (r"^reServer-Industrial-J501", f"{RESERV}/reServer Industrial J501"),
    (r"^A203-Carrier-Board", f"{RECOMP}/reComputer A203 v2"),
    (r"^A205-Carrier-Board", f"{RECOMP}/reComputer A205"),
    (r"^A206-Carrier-Board", f"{RECOMP}/reComputer A206"),
    (r"^A60[3-8]-Carrier-Board|^Jetson-A608", f"{RECOMP}/reComputer A608"),
    (r"^Jetson-Xavier-AGX-H01|^AGX-Orin-32GB-H01", f"{RECOMP}/Jetson Xavier AGX H01"),
    (r"^Jetson-SUB-Mini-PC", f"{RECOMP}/Jetson SUB Mini PC"),
    (r"^Jetson-20-1-H1$", f"{RECOMP}/reComputer J202"),   # reComputer J2011 (J20 series)
    (r"^Jetson-20-1-H2$", f"{RECOMP}/reComputer J202"),   # reComputer J2012 (J20 series)
    (r"^Jetson-10-1-A0$", f"{RECOMP}/reComputer J1010"),  # reComputer J1010
    (r"^Jetson-10-1-H0$", f"{RECOMP}/reComputer J1020 v2"),  # reComputer 1020
    (r"^Jetson-Mate", f"{RECOMP}/Jetson-Mate"),
    (r"^A203-Mini-PC", f"{RECOMP}/reComputer A203E"),
    (r"^A205E-Mini-PC|^A205E-Carrier-Board", f"{RECOMP}/reComputer A205E"),
    (r"^Mini-AI-Computer-T906", f"{RECOMP}/Mini AI Computer T906"),
    (r"^reComputer-Robotics-GMSL-board", f"{RECOMP}/reComputer Robotics J401"),
    # Note: Accessories (cameras / LTE / WiFi / ReSpeaker / RPLiDAR / NVIDIA
    # modules / robotics add-ons …) and the reComputer J501 carrier-board folder
    # were dropped from the repo — matching slugs stay unrouted (no download).
]


def norm(s: str) -> str:
    return re.sub(r"[\s_-]+", "", s).lower()


def route(slug: str):
    for pat, dest in ROUTING:
        if re.match(pat, slug):
            return dest
    return None


# Per-type routing of a downloaded document into the product subfolder.
SUB_3D = (".stp", ".step", ".stl", ".stp.gz", ".step.gz", ".stl.gz")
SUB_MECH = (".dxf", ".dwg")
SUB_FW = (".zip", ".7z", ".rar", ".tar.gz")
FW_KEYS = ("firmware", "driver", "qspi", "jetpack", "flash", "_jp", "dail", "sam")
SCH_KEYS = ("_sch", "schematic", "schematics")
MANUAL_KEYS = ("manual", "assembly", "reference-guide", "user guide", "getting", "thermal", "test report")


def doc_subdir(fname: str) -> str:
    """Pick the product subfolder for a file based on its name."""
    low = fname.lower()
    if low.endswith(SUB_3D) or (low.endswith((".7z", ".zip")) and "3d" in low):
        return "3D Model"
    if low.endswith(SUB_MECH):
        return "Mechanical"
    if low.endswith(".brd"):
        return "Layout"
    if low.endswith(".dsn"):
        return "Schematic"
    if low.endswith(SUB_FW):
        if any(k in low for k in SCH_KEYS):
            return "Schematic"
        return "Firmware" if any(k in low for k in FW_KEYS) else "Datasheet"
    if low.endswith(".pdf"):
        if any(k in low for k in MANUAL_KEYS):
            return "Manual"
        if any(k in low for k in SCH_KEYS):
            return "Schematic"
    return "Datasheet"


# --------------------------------------------------------------------------
# Discovery
# --------------------------------------------------------------------------
def discover_products(wiki_dir: pathlib.Path, explicit: pathlib.Path | None):
    """Return list of (pid, slug, sku)."""
    found = {}
    if explicit:
        for line in open(explicit):
            line = line.strip()
            if not line:
                continue
            parts = line.split("\t")
            pid, slug = parts[0], parts[1] if len(parts) > 1 else ""
            sku = parts[2] if len(parts) > 2 else ""
            found[pid] = (slug, sku)
    else:
        for p in wiki_dir.rglob("*"):
            if p.suffix not in (".md", ".mdx"):
                continue
            txt = p.read_text(errors="replace")
            for m in STORE_LINK_RE.finditer(txt):
                pid = m.group(2)
                if pid not in found:
                    found[pid] = (m.group(1), "")
            sku_m = SKU_RE.search(txt)
            if sku_m and found:
                sku = sku_m.group(1).split(",")[0].strip()
                # attach sku to the first product this doc links that lacks one
                for pid in sorted(found):
                    if found[pid][1] == "":
                        found[pid] = (found[pid][0], sku)
                        break
    return [(pid, slug, sku) for pid, (slug, sku) in sorted(found.items())]


# --------------------------------------------------------------------------
# GraphQL
# --------------------------------------------------------------------------
def gql(product_id: str) -> dict:
    q = json.dumps({"query": "{ customProductAttributes(id: \"" + product_id + "\", attributeCodes: " + json.dumps(ATTR_CODES) + ") }"})
    req = urllib.request.Request(GRAPHQL, data=q.encode(),
        headers={"Content-Type": "application/json", "User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        raw = r.read().decode()
    d = json.loads(raw)
    attrs = (d.get("data") or {}).get("customProductAttributes")
    return json.loads(attrs) if attrs else {}


def unescape(v: str) -> str:
    return v.replace("\\/", "/").replace('\\"', '"').replace("\\r\\n", "\n").replace("\\n", "\n") if v else ""


def scrape(pid: str, slug: str, sku: str):
    try:
        attrs = gql(pid)
    except Exception as e:
        return {"pid": pid, "slug": slug, "sku": sku, "error": f"gql: {e}"}
    certs = []
    for key in ("certification_info_eccn", "certification_info"):
        html = unescape(attrs.get(key, ""))
        for m in re.finditer(r"Seeed_Certificate/documents_certificate/([^\"'<> ]+\.pdf)", html, re.I):
            url = CERT_PREFIX + m.group(1)
            if url not in certs:
                certs.append(url)
    docs = []
    for m in re.finditer(r'<a\b[^>]*href="([^"]+)"[^>]*>(.*?)</a>', unescape(attrs.get("documents", "")), re.S):
        url = m.group(1)
        label = re.sub(r"<[^>]+>", "", m.group(2)).strip()
        if re.search(r"\.(pdf|stp|step|stl|dxf|dwg|zip|7z|rar|tar\.gz)(\?|$)", url, re.I):
            docs.append((label, url))
    return {"pid": pid, "slug": slug, "sku": sku, "certs": certs, "docs": docs,
            "parts": len(attrs.get("certification_info_part", "") or "")}


# --------------------------------------------------------------------------
# Download
# --------------------------------------------------------------------------
GIT_LIMIT = 100 * 1024 * 1024  # GitHub hard limit per file


def fetch(url: str, dest: pathlib.Path, timeout: int = 240):
    gz_dest = pathlib.Path(str(dest) + ".gz")
    if dest.exists() and dest.stat().st_size > 0:
        return "exists"
    if gz_dest.exists() and gz_dest.stat().st_size > 0:
        return "exists"  # previously stored compressed
    dest.parent.mkdir(parents=True, exist_ok=True)
    try:
        r = subprocess.run(["curl", "-sSL", "--fail", "--max-time", str(timeout), "-A", "Mozilla/5.0",
                            "-o", str(dest), url], capture_output=True, text=True, timeout=timeout + 20)
        if r.returncode == 0 and dest.exists() and dest.stat().st_size > 0:
            if dest.stat().st_size > GIT_LIMIT:
                gz = subprocess.run(["gzip", "-9", "-c", str(dest)], capture_output=True)
                if gz.returncode == 0 and len(gz.stdout) > 0:
                    gz_dest.write_bytes(gz.stdout)
                    dest.unlink()
                    return "ok(gz)"
                return f"fail(gzip)"
            return "ok"
        return f"fail({r.returncode})"
    except Exception as e:
        return f"exc {str(e)[:80]}"


def process(pid, slug, sku, repo: pathlib.Path, dry_run: bool):
    rec = scrape(pid, slug, sku)
    dest = route(slug)
    out = {"pid": pid, "slug": slug, "sku": sku, "dir": dest, "certs": [], "docs": [], "bazaar_pdf": None}
    if rec.get("error"):
        out["error"] = rec["error"]
        return out
    if dest is None:
        out["unrouted"] = True
        return out

    cert_dir = (repo / dest) / "Certificate"
    doc_dir = (repo / dest) / "Datasheet"
    seen = set()
    for url in rec["certs"]:
        fname = urllib.parse.unquote(url.rstrip("/").split("/")[-1])
        if fname.lower() in seen:
            continue
        seen.add(fname.lower())
        st = "exists" if dry_run else fetch(url, cert_dir / fname)
        out["certs"].append({"file": fname, "status": st})
    if sku:
        url = BAZAAR_PDF.format(sku=sku)
        st = "exists" if dry_run else fetch(url, doc_dir / f"{sku}.pdf")
        out["bazaar_pdf"] = {"sku": sku, "status": st}
    for label, url in rec["docs"]:
        u = url.split("?")[0]
        fname = urllib.parse.unquote(u.rstrip("/").split("/")[-1])
        if not fname or "/" in fname:
            continue
        sub = (repo / dest) / doc_subdir(fname)
        st = "exists" if dry_run else fetch(u, sub / fname)
        out["docs"].append({"file": f"{doc_subdir(fname)}/{fname}", "status": st})
    return out


# --------------------------------------------------------------------------
# Report
# --------------------------------------------------------------------------
def write_report(results, repo: pathlib.Path):
    ok = sum(1 for r in results for c in r["certs"] if c["status"] == "ok")
    ex = sum(1 for r in results for c in r["certs"] if c["status"] == "exists")
    fail = sum(1 for r in results for c in r["certs"] if c["status"] not in ("ok", "exists"))
    d_ok = sum(1 for r in results for c in r["docs"] if c["status"] == "ok")
    d_ex = sum(1 for r in results for c in r["docs"] if c["status"] == "exists")
    b_ok = sum(1 for r in results if r["bazaar_pdf"] and r["bazaar_pdf"]["status"] == "ok")
    unrouted = sum(1 for r in results if r.get("unrouted"))
    errs = [r for r in results if r.get("error")]

    out = ["# Bazaar certifications & documents download report\n",
           f"- Products processed: {len(results)}",
           f"- Certificates: {ok} downloaded, {ex} already present, {fail} failed",
           f"- Extra datasheets/docs: {d_ok} downloaded, {d_ex} already present",
           f"- Bazaar SKU PDFs: {b_ok} downloaded",
           f"- Unrouted (no repo folder): {unrouted}",
           f"- GraphQL errors: {len(errs)}", ""]
    for r in sorted(results, key=lambda x: x["slug"]):
        out.append(f"## {r['slug']}  (`{r['pid']}`, {r['dir'] or 'UNROUTED'})")
        if r.get("error"):
            out.append(f"- ERROR: {r['error']}")
        if r.get("unrouted"):
            out.append("- no matching repo folder (see scripts/sync_bazaar.py ROUTING)")
        if r.get("bazaar_pdf"):
            out.append(f"- Bazaar PDF `{r['bazaar_pdf']['sku']}.pdf`: {r['bazaar_pdf']['status']}")
        if r["certs"]:
            out.append("\n| Cert | Status |\n|---|---|")
            for c in r["certs"]:
                out.append(f"| {c['file']} | {c['status']} |")
        if r["docs"]:
            out.append("\n- Extra docs:")
            for d in r["docs"]:
                out.append(f"  - {d['file']}: {d['status']}")
        out.append("")
    (repo / "Resources").mkdir(parents=True, exist_ok=True)
    (repo / "Resources" / "_bazaar_download_report.md").write_text("\n".join(out))


# --------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser(description="Scrape Seeed bazaar certs & resources into the repo")
    ap.add_argument("--repo", default=".", help="repo root (default: cwd)")
    ap.add_argument("--products", default=None, help="TSV file pid<TAB>slug<TAB>sku; default: auto-discover from wiki")
    ap.add_argument("--wiki", default="Documentation/NVIDIA_Jetson", help="wiki dir for discovery")
    ap.add_argument("--dry-run", action="store_true", help="scan + report only, no downloads")
    ap.add_argument("--limit", type=int, default=0, help="max products to process (0 = all)")
    ap.add_argument("--workers", type=int, default=8)
    args = ap.parse_args()

    repo = pathlib.Path(args.repo).resolve()
    products = discover_products(repo / args.wiki, pathlib.Path(args.products) if args.products else None)
    if args.limit:
        products = products[: args.limit]
    print(f"discovered {len(products)} products")

    results = []
    if args.dry_run:
        for pid, slug, sku in products:
            rec = scrape(pid, slug, sku)
            results.append({"pid": pid, "slug": slug, "sku": sku,
                            "dir": route(slug),
                            "certs": [{"file": urllib.parse.unquote(c.rsplit("/", 1)[-1]), "status": "?"} for c in rec["certs"]],
                            "docs": [{"file": urllib.parse.unquote(d[1].split("?")[0].rstrip("/").rsplit("/", 1)[-1]), "status": "?"} for d in rec["docs"]],
                            "bazaar_pdf": {"sku": sku, "status": "?"} if sku else None,
                            "unrouted": route(slug) is None})
        print(f"dry-run: {sum(1 for r in results if r['dir'] and not r.get('unrouted'))} routable products")
    else:
        with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as ex:
            futs = [ex.submit(process, pid, slug, sku, repo, False) for pid, slug, sku in products]
            for f in concurrent.futures.as_completed(futs):
                results.append(f.result())
        write_report(results, repo)

    # console summary
    unrouted = [r["slug"] for r in results if r.get("unrouted")]
    if unrouted:
        print(f"unrouted ({len(unrouted)}): {', '.join(unrouted[:12])}")
    if not args.dry_run:
        print("report: Resources/_bazaar_download_report.md")


if __name__ == "__main__":
    main()