# Supported Devices

Seeed Jetson DevelopTool supports the full range of Seeed Studio reComputer Jetson products, plus the most common NVIDIA Jetson developer kits and carrier boards. The **Flash Center** can download and flash the official JetPack firmware for every model listed on this page.

The tables below are generated from the same firmware metadata that the application ships with (`l4t_data.json`) and refreshes from this wiki repository at runtime, so this page always matches what the Flash Center offers. If you installed an older version of the tool, update it to see the newest releases.

## Understanding L4T and JetPack

**L4T** (Linux for Tegra) is the NVIDIA system image — kernel and rootfs — that runs on a Jetson module. **JetPack** is the developer distribution built on a specific L4T version. The Flash Center asks for the L4T version; the table below maps each L4T release to the JetPack distribution it belongs to.

<!-- GEN:Jetson-DevelopTool:JetPack:BEGIN -->

Tables generated from [L4TData.json](https://github.com/Seeed-Studio/wiki-documents/blob/docusaurus-version/src/data/jetson/L4TData.json) (merged with the app bundle) — 2026-09-16.

### JetPack ↔ L4T

| JetPack | L4T |
|---|---|
| 5.1.1 | 35.3.1 |
| 5.1.3 | 35.5.0 |
| 6.0 | 36.3.0 |
| 6.1 | 36.4.0 |
| 6.2 | 36.4.3 |
| 6.2.1 | 36.4.4 |
| 6.2.2 | 36.5.0 |
| 7.1 | 38.4.0 |
| 7.2.0 | 39.2.0 |
<!-- GEN:Jetson-DevelopTool:JetPack:END -->

> [!NOTE]
> Orin-based boards (reComputer Super / Mini / Robotics / Classic / Industrial, reServer Industrial, J501 family) are available on the **JetPack 6.x (L4T 36.x)** and the newest **JetPack 7.2 (L4T 39.2.0)** release trains. Xavier NX boards (J2011 / J2012) stop at JetPack 5.1 (L4T 35.x), and the Jetson Thor based J6015 uses JetPack 7.1 (L4T 38.4.0).

## How to Check Your Current L4T

Run on the Jetson:

```bash
dpkg-query -W nvidia-l4t-core
cat /etc/nv_tegra_release
```

`nvidia-l4t-core` reports the installed L4T package version (for example `36.4.3`). To see the JetPack version:

```bash
dpkg-query -W nvidia-jetpack
```

## Which L4T Should I Flash?

- **New projects** — use the newest supported release for your model, usually JetPack 7.2 (L4T 39.2.0) on Orin boards.
- **Existing applications** — stay on the JetPack your application and container images were built for (for example 6.2 / 36.4.3), and upgrade when your stack is ready.
- **Xavier NX (J2011 / J2012)** — only JetPack 5.1 (L4T 35.3.1 / 35.5.0) is available; do not select a 36.x release.

## Supported Devices

<!-- GEN:Jetson-DevelopTool:Devices:BEGIN -->

### reComputer Super (Orin NX / Nano)

![reComputer Super (Orin NX / Nano)](https://raw.githubusercontent.com/Seeed-Projects/Seeed-Jetson-DevelopTool/main/assets/devices/super.jpg)

| Model | Jetson Module | Memory | Supported L4T |
|---|---|---|---|
| J4012s | Jetson Orin NX | 16 GB | 39.2.0, 36.4.3 |
| J4011s | Jetson Orin NX | 8 GB | 39.2.0, 36.4.3 |
| J3011s | Jetson Orin Nano | 8 GB | 39.2.0, 36.4.3 |
| J3010s | Jetson Orin Nano | 4 GB | 39.2.0, 36.4.3 |

See also: [Getting Started](https://wiki.seeedstudio.com/recomputer_jetson_super_getting_started/) · [Hardware Interfaces](https://wiki.seeedstudio.com/recomputer_jetson_super_hardware_interfaces_usage/)

### reComputer Mini (Orin NX / Nano)

![reComputer Mini (Orin NX / Nano)](https://raw.githubusercontent.com/Seeed-Projects/Seeed-Jetson-DevelopTool/main/assets/devices/mini.jpg)

| Model | Jetson Module | Memory | Supported L4T |
|---|---|---|---|
| J4012mini | Jetson Orin NX | 16 GB | 36.4.3, 36.3.0, 35.5.0 |
| J4011mini | Jetson Orin NX | 8 GB | 36.4.3, 36.3.0, 35.5.0 |
| J3011mini | Jetson Orin Nano | 8 GB | 36.4.3, 36.3.0, 35.5.0 |
| J3010mini | Jetson Orin Nano | 4 GB | 36.4.3, 36.3.0, 35.5.0 |

See also: [Getting Started](https://wiki.seeedstudio.com/recomputer_jetson_mini_getting_started/) · [Hardware Interfaces](https://wiki.seeedstudio.com/recomputer_jetson_mini_hardware_interfaces_usage/)

### reComputer Robotics (GMSL, Orin NX / Nano)

![reComputer Robotics (GMSL, Orin NX / Nano)](https://raw.githubusercontent.com/Seeed-Projects/Seeed-Jetson-DevelopTool/main/assets/devices/robotics.jpg)

| Model | Jetson Module | Memory | Supported L4T |
|---|---|---|---|
| J4012robotics | Jetson Orin NX | 16 GB | 39.2.0, 36.4.3 |
| J4011robotics | Jetson Orin NX | 8 GB | 39.2.0, 36.4.3 |
| J3011robotics | Jetson Orin Nano | 8 GB | 39.2.0, 36.4.3 |
| J3010robotics | Jetson Orin Nano | 4 GB | 39.2.0, 36.4.3 |

See also: [Getting Started](https://wiki.seeedstudio.com/recomputer_robotics_j401_getting_started/) · [Hardware Interfaces](https://wiki.seeedstudio.com/recomputer_robotics_j401_hardware_interfaces_usage/)

### reComputer Classic (Orin NX / Nano)

![reComputer Classic (Orin NX / Nano)](https://raw.githubusercontent.com/Seeed-Projects/Seeed-Jetson-DevelopTool/main/assets/devices/classic.jpg)

| Model | Jetson Module | Memory | Supported L4T |
|---|---|---|---|
| J4012classic | Jetson Orin NX | 16 GB | 39.2.0, 36.4.3, 36.4.0, 36.3.0, 35.5.0 |
| J4011classic | Jetson Orin NX | 8 GB | 39.2.0, 36.4.3, 36.4.0, 36.3.0, 35.5.0 |
| J3011classic | Jetson Orin Nano | 8 GB | 39.2.0, 36.4.3, 36.4.0, 36.3.0, 35.5.0 |
| J3010classic | Jetson Orin Nano | 4 GB | 39.2.0, 36.4.3, 36.4.0, 36.3.0, 35.5.0 |

See also: [Getting Started](https://wiki.seeedstudio.com/reComputer_J30_40_with_Jetson_getting_start/) · [Hardware Interfaces](https://wiki.seeedstudio.com/J401_carrierboard_Hardware_Interfaces_Usage/)

### reComputer Classic (AGX Orin)

![reComputer Classic (AGX Orin)](https://raw.githubusercontent.com/Seeed-Projects/Seeed-Jetson-DevelopTool/main/assets/devices/classic.jpg)

| Model | Jetson Module | Memory | Supported L4T |
|---|---|---|---|
| J5012classic | Jetson AGX Orin | 64 GB | 39.2.0 |
| J5011classic | Jetson AGX Orin | 32 GB | 39.2.0 |

### reComputer Industrial (Orin NX / Nano / Xavier NX)

![reComputer Industrial (Orin NX / Nano / Xavier NX)](https://raw.githubusercontent.com/Seeed-Projects/Seeed-Jetson-DevelopTool/main/assets/devices/industrial.jpg)

| Model | Jetson Module | Memory | Supported L4T |
|---|---|---|---|
| J4012industrial | Jetson Orin NX | 16 GB | 39.2.0, 36.4.3, 36.4.0, 36.3.0, 35.5.0, 35.3.1 |
| J4011industrial | Jetson Orin NX | 8 GB | 39.2.0, 36.4.4, 36.4.3, 36.4.0, 36.3.0, 35.5.0, 35.3.1 |
| J3011industrial | Jetson Orin Nano | 8 GB | 39.2.0, 36.4.3, 36.4.0, 36.3.0, 35.5.0, 35.3.1 |
| J3010industrial | Jetson Orin Nano | 4 GB | 39.2.0, 36.4.3, 36.4.0, 36.3.0, 35.5.0, 35.3.1 |
| J2012industrial | Jetson Xavier NX | 16 GB | 35.5.0, 35.3.1 |
| J2011industrial | Jetson Xavier NX | 8 GB | 35.5.0, 35.3.1 |

See also: [Getting Started](https://wiki.seeedstudio.com/reComputer_Industrial_Getting_Started/) · [Hardware Interfaces](https://wiki.seeedstudio.com/reComputer_Industrial_J40_J30_Hardware_Interfaces_Usage/) · [Hardware Interfaces](https://wiki.seeedstudio.com/reComputer_Industrial_J20_Hardware_Interfaces_Usage/)

### reServer Industrial (Orin NX / Nano)

![reServer Industrial (Orin NX / Nano)](https://raw.githubusercontent.com/Seeed-Projects/Seeed-Jetson-DevelopTool/main/assets/devices/reserver.jpg)

| Model | Jetson Module | Memory | Supported L4T |
|---|---|---|---|
| J4012reserver | Jetson Orin NX | 16 GB | 39.2.0, 36.4.3, 36.4.0, 36.3.0, 35.5.0, 35.3.1 |
| J4011reserver | Jetson Orin NX | 8 GB | 39.2.0, 36.4.3, 36.4.0, 36.3.0, 35.5.0, 35.3.1 |
| J3011reserver | Jetson Orin Nano | 8 GB | 39.2.0, 36.4.3, 36.4.0, 36.3.0, 35.5.0, 35.3.1 |
| J3010reserver | Jetson Orin Nano | 4 GB | 39.2.0, 36.4.3, 36.4.0, 36.3.0, 35.5.0, 35.3.1 |

See also: [Getting Started](https://wiki.seeedstudio.com/reServer_Industrial_Getting_Started/) · [Hardware Interfaces](https://wiki.seeedstudio.com/reserver_industrial_hardware_interface_usage/)

### reServer J501 Carrier Board (AGX Orin)

![reServer J501 Carrier Board (AGX Orin)](https://raw.githubusercontent.com/Seeed-Projects/Seeed-Jetson-DevelopTool/main/assets/devices/j501_carrier.jpg)

| Model | Jetson Module | Memory | Supported L4T |
|---|---|---|---|
| J501 32GB (standard) | Jetson AGX Orin | 32 GB | 36.4.3, 36.3.0, 35.5.0 |
| J501 32GB (GMSL) | Jetson AGX Orin | 32 GB | 39.2.0, 36.4.3, 36.3.0, 35.5.0 |
| J501 64GB (standard) | Jetson AGX Orin | 64 GB | 36.4.3, 36.3.0, 35.5.0 |
| J501 64GB (GMSL) | Jetson AGX Orin | 64 GB | 39.2.0, 36.4.3, 36.3.0, 35.5.0 |

See also: [Getting Started](https://wiki.seeedstudio.com/reserver_j501_getting_started/) · [Hardware Interfaces](https://wiki.seeedstudio.com/j501_carrier_board_interfaces_usage/)

### reComputer Robotics J501 (AGX Orin)

![reComputer Robotics J501 (AGX Orin)](https://raw.githubusercontent.com/Seeed-Projects/Seeed-Jetson-DevelopTool/main/assets/devices/j501_robotics.jpg)

| Model | Jetson Module | Memory | Supported L4T |
|---|---|---|---|
| J501 32GB | Jetson AGX Orin | 32 GB | 39.2.0, 36.4.4 |
| J501 64GB | Jetson AGX Orin | 64 GB | 39.2.0, 36.4.4 |

See also: [Getting Started](https://wiki.seeedstudio.com/ai_robotics_recomputer_j501_robotics_getting_started/) · [Hardware Interfaces](https://wiki.seeedstudio.com/ai_robotics_recomputer_j501_robotics_getting_started/)

### reComputer Robotics J501 Mini (AGX Orin)

![reComputer Robotics J501 Mini (AGX Orin)](https://raw.githubusercontent.com/Seeed-Projects/Seeed-Jetson-DevelopTool/main/assets/devices/j501_mini.jpg)

| Model | Jetson Module | Memory | Supported L4T |
|---|---|---|---|
| J501 Mini 32GB | Jetson AGX Orin | 32 GB | 39.2.0, 36.4.4 |
| J501 Mini 64GB | Jetson AGX Orin | 64 GB | 39.2.0, 36.4.4 |

See also: [Getting Started](https://wiki.seeedstudio.com/recomputer_j501_mini_getting_started/) · [Hardware Interfaces](https://wiki.seeedstudio.com/recomputer_j501_mini_getting_started/)

### NVIDIA Jetson AGX Orin Developer Kit

![NVIDIA Jetson AGX Orin Developer Kit](https://raw.githubusercontent.com/Seeed-Projects/Seeed-Jetson-DevelopTool/main/assets/devices/agx_orin_devkit.png)

| Model | Jetson Module | Memory | Supported L4T |
|---|---|---|---|
| AGX Orin DevKit 32GB | Jetson AGX Orin (DevKit) | 32 GB | 39.2.0, 36.5.0 |
| AGX Orin DevKit 64GB | Jetson AGX Orin (DevKit) | 64 GB | 39.2.0, 36.5.0 |

See also: [Getting Started](https://wiki.seeedstudio.com/reComputer_J30_40_with_Jetson_getting_start/) · [Hardware Interfaces](https://wiki.seeedstudio.com/reComputer_J30_40_with_Jetson_getting_start/)

### NVIDIA Jetson Orin Nano Developer Kit (Super)

![NVIDIA Jetson Orin Nano Developer Kit (Super)](https://raw.githubusercontent.com/Seeed-Projects/Seeed-Jetson-DevelopTool/main/assets/devices/orin_nano_devkit_super.jpg)

| Model | Jetson Module | Memory | Supported L4T |
|---|---|---|---|
| Orin Nano DevKit (Super) | Jetson Orin Nano (DevKit Super) | 8 GB | 39.2.0, 36.4.3 |

See also: [Getting Started](https://wiki.seeedstudio.com/reComputer_J30_40_with_Jetson_getting_start/) · [Hardware Interfaces](https://wiki.seeedstudio.com/reComputer_J30_40_with_Jetson_getting_start/)

### reComputer J6015 (Jetson Thor)

![reComputer J6015 (Jetson Thor)](https://raw.githubusercontent.com/Seeed-Projects/Seeed-Jetson-DevelopTool/main/assets/devices/j601-carrier-board.jpg)

| Model | Jetson Module | Memory | Supported L4T |
|---|---|---|---|
| J6015 | Jetson Thor | – | 38.4.0 |
<!-- GEN:Jetson-DevelopTool:Devices:END -->

> [!TIP]
> Find your exact model code on the sticker of the device (for example `J4012`), then look it up in the table above. The [Connect Device](https://wiki.seeedstudio.com/jetson_developtool_connect_device/) and [Flash Firmware](https://wiki.seeedstudio.com/jetson_developtool_flash_firmware/) guides walk you through recovery mode and flashing.

## Next Steps

- [Connect Your Device →](https://wiki.seeedstudio.com/jetson_developtool_connect_device/)
- [Flash Firmware →](https://wiki.seeedstudio.com/jetson_developtool_flash_firmware/)

## Tech Support & Product Discussion

Thank you for choosing our products! We are here to provide you with different support to ensure that your experience with our products is as smooth as possible. We offer several communication channels to cater to different preferences and needs.

<https://forum.seeedstudio.com/>
<https://www.seeedstudio.com/contacts>

<https://discord.gg/eWkprNDMU7>
<https://github.com/Seeed-Studio/wiki-documents/discussions/69>
