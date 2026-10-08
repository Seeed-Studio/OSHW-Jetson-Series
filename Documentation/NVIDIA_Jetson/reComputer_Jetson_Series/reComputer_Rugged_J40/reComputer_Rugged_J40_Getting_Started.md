# Getting Started with reComputer Rugged J40

  ![reComputer Rugged J4012](https://media-cdn.seeedstudio.com/media/catalog/product/cache/bb49d3ec4ee05b6f018e93f896b8a25d/1/0/100046979-gallery_img_2.jpg)

The reComputer Rugged J4012 is an IP66-rated edge AI computer powered by NVIDIA Jetson Orin NX 16GB. Its sealed M12 connectivity provides USB, Ethernet with PSE, CAN, RS-232/422/485, and DI/DO interfaces, while an M.2 Key B slot supports 5G expansion, making it well suited for AMR, robotics, agriculture, industrial automation, and maritime applications.

  [Get One Now 🖱️](https://www.seeedstudio.com/reComputer-Rugged-J4012-p-6920.html)

## Features

- **IP66 Waterproof**: Fully sealed enclosure with M12 waterproof connectors for all external interfaces
- **Fanless Passive Cooling**: Silent operation across -20°C to +60°C with 0.7 m/s airflow
- **Rugged & Vibration-Resistant**: 3 Grms @ 5–500 Hz, 1 hr/axis — suitable for vehicle and marine use
- **Rich Industrial I/O**: CAN-FD (isolated), RS-232/422/485, DI/DO, all via M12 A-code connectors
- **Flexible Networking**: 4× PoE GbE + 1× GbE (M12), M.2 Key E (Wi-Fi/BT), M.2 Key B (5G/GPS)
- **Wide Voltage Input**: 19–48 V DC via M12 B/A-code connector
- **Certifications**: CE, FCC, RoHS, REACH

## Specifications



      Product Name
      reComputer Rugged J4012
      reComputer Rugged J3011




      SKU
      100046979
      100002634


      NVIDIA Jetson Module
      Orin NX 16GB
      Orin Nano 8GB


      Processor System
      AI Performance
      100 TOPS
      40 TOPS


      GPU
      1024-core NVIDIA Ampere, 32 Tensor Cores
      1024-core NVIDIA Ampere, 32 Tensor Cores


      CPU
      8-core Arm Cortex-A78AE v8.2 64-bit, 2MB L2 + 4MB L3
      6-core Arm Cortex-A78AE v8.2 64-bit, 1.5MB L2 + 4MB L3


      Memory
      16GB 128-bit LPDDR5 @ 102.4 GB/s
      8GB 128-bit LPDDR5 @ 68 GB/s


      Storage
      eMMC
      -


      Expansion
      M.2 Key M (2280) NVMe SSD — 128 GB included


      I/O
      Ethernet
      4× GbE RJ45 PoE PSE (802.3af, M12 waterproof) + 1× GbE RJ45 (M12 waterproof)


      USB
      4× USB 3.2 Type-A (M12 waterproof) + 1× USB 2.0/3.0 Type-C (flashing, waterproof cap) + 1× USB Type-C (debug)


      Display
      1× HDMI (waterproof cap)


      CAN
      2× CAN-FD (isolated, 120 Ω) via M12 A-code 8-pin


      Serial
      1× RS-232/422/485 via M12 A-code 8-pin


      DI/DO
      2× DI + 2× DO via M12 12-pin / 8-pin


      SIM
      1× Nano SIM card slot


      Antenna
      4× SMA waterproof antenna connectors


      Expansion
      M.2 Key E
      Wi-Fi / Bluetooth module (optional)


      M.2 Key B
      5G / GPS module (optional)


      Power
      Input
      19–48 V DC via M12 B/A-code connector


      Consumption
      Typical 25 W, fuse 10 A


      Environment
      Ingress Protection
      IP66


      Operating Temperature
      -20°C to +60°C (with 0.7 m/s airflow)


      Humidity
      10–95% RH (non-condensing)


      Vibration
      3 Grms @ 5–500 Hz, random, 1 hr/axis


      Dimensions
      210 mm × 190 mm × 93 mm


      Color
      Silver-grey (mid-frame silver, heatsink black)


      Certification
      CE, FCC, RoHS, REACH


      Warranty
      2 Years



## Hardware Overview

> [!NOTE]
> Hardware overview images will be added once the product is finalized.

**LED Indicators:**

| LED | Color | Status | Description |
|-----|-------|--------|-------------|
| PWR | Green | On | Device is powered |
| PWR | Green | Off | Device is not powered |
| ACT | Green | Flashing | SSD access activity |

## Flash JetPack

> [!NOTE]
> Flash instructions will be added once the BSP is available. The flashing process follows the same procedure as other reComputer J40 series devices.

Please refer to the [Flash BSP with Jetpack to Selected Jetson](https://wiki.seeedstudio.com/flash/jetpack_to_selected_product/) page for the latest flashing guide.

### Prerequisites

- reComputer Rugged J40
- Power supply (19–48 V DC)
- Ubuntu host PC (20.04 or 22.04)
- USB Type-C data cable (for flashing)
- External monitor + HDMI cable
- Keyboard and mouse

### Enter Force Recovery Mode

  ![image](https://files.seeedstudio.com/wiki/rugged_J401/1.jpg)

1. Connect a USB Type-C cable between the **DEVICE** port and your Ubuntu host PC.
2. Press and hold the **REC** (Recovery) button.
3. While holding REC, connect the power supply to power on the board.
4. Release the Recovery button.

On the Ubuntu host PC, verify recovery mode with:

```bash
lsusb
```

Expected output by module:
- Orin NX 16GB: `0955:7323 NVidia Corp`
- Orin Nano 8GB: `0955:7523 NVidia Corp`

## Extract and Flash

**Step 1:** Extract the downloaded image file:

```bash
cd <path-to-image>
sudo tar xpf mfi_xxxx.tar.gz
```

**Step 2:** Enter the extracted directory and execute the flash command:

```bash
cd mfi_xxxx
sudo ./tools/kernel_flash/l4t_initrd_flash.sh --flash-only --massflash 1 --network usb0 --showlogs
```

## Resources

- [reComputer Rugged J401 Datasheet](../../../../reComputer%20Jetson%20carrier%20board/reComputer%20Rugged%20J401/Datasheet/reComputer_rugged_J401_datasheet.pdf)
- [Linux_for_Tegra Source Code](https://github.com/Seeed-Studio/Linux_for_Tegra)
- [NVIDIA Jetson Devices Comparison](../../../../reComputer%20Jetson%20carrier%20board/Common/Datasheet/NVIDIA-Jetson-Devices-and-carrier-boards-comparision.pdf)

## Tech Support & Product Discussion

Thank you for choosing our products! We are here to provide you with different support to ensure that your experience with our products is as smooth as possible.

<https://forum.seeedstudio.com/>
<https://www.seeedstudio.com/contacts>

<https://discord.gg/eWkprNDMU7>
<https://github.com/Seeed-Studio/wiki-documents/discussions/69>
