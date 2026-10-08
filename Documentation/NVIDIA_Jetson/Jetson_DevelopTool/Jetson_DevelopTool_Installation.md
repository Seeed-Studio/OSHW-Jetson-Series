# Installation

## Requirements

| Item | Requirement |
|------|-------------|
| Host OS | Ubuntu 20.04 / 22.04 / 24.04, or Windows 10/11 |
| Python | 3.8 or newer |

## Option 1 — Install via pip (Recommended)

```bash
pip install seeed-jetson-developer
```

Then launch the GUI:

```bash
seeed-jetson-developer
```

## Option 2 — Install from Source

```bash
git clone https://github.com/Seeed-Projects/Seeed-Jetson-DevelopTool.git
cd Seeed-Jetson-DevelopTool
pip install .
```

Launch after installation:

```bash
seeed-jetson-developer
```

## Option 3 — Run Directly (No Install)

If you prefer to run without installing:

```bash
git clone https://github.com/Seeed-Projects/Seeed-Jetson-DevelopTool.git
cd Seeed-Jetson-DevelopTool
pip install PyQt5 paramiko requests
python3 run_v2.py
```

## Verify Installation

After launching, the main window should appear with all eight module tabs visible. If the window does not open, check that PyQt5 is installed:

```bash
pip show PyQt5
```

> [!TIP]
> On Ubuntu, if you get a display error such as `cannot connect to X server`, make sure you are running in a graphical desktop session, not an SSH terminal without X forwarding.

## Next Steps

- [Connect Your Device →](https://wiki.seeedstudio.com/jetson_developtool_connect_device/)
- [Flash Firmware →](https://wiki.seeedstudio.com/jetson_developtool_flash_firmware/)

## Tech Support & Product Discussion

Thank you for choosing our products! We are here to provide you with different support to ensure that your experience with our products is as smooth as possible. We offer several communication channels to cater to different preferences and needs.

<https://forum.seeedstudio.com/>
<https://www.seeedstudio.com/contacts>

<https://discord.gg/eWkprNDMU7>
<https://github.com/Seeed-Studio/wiki-documents/discussions/69>
