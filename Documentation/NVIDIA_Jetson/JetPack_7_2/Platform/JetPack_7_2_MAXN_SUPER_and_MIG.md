# JetPack 7.2 MAXN_SUPER and MIG

> [!NOTE] Planned content
> This page is reserved for two platform-specific JetPack 7.2 capabilities: `MAXN_SUPER` on supported Jetson AGX Orin 32GB configurations and Multi-Instance GPU on supported Jetson Thor configurations.

The planned guide will include:

- supported modules, carrier boards, power supplies, and thermal requirements;
- enabling, confirming, benchmarking, and reverting `MAXN_SUPER`;
- MIG partition creation, workload placement, monitoring, and teardown on Thor;
- memory, power, thermal, latency, and throughput comparison methodology;
- production safety limits and unsupported configuration warnings.

Do not enable a new power mode or GPU partitioning scheme before confirming the complete hardware and BSP support matrix.
