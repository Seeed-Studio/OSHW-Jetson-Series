# Getting Started with reComputer Robotics J601

  ![image](https://files.seeedstudio.com/wiki/reComputer_Robotics_J601/Getting_Start/robotics_j601_carrier_board_getting_started_01.jpg)

The reComputer J601 is a compact yet powerful edge AI carrier board for Jetson AGX Thor, delivering up to 2070 TFLOPS. Built for development and production, it features M.2 Key E/M/B, 4x 10Gb RJ45, 4×USB 3.2, HDMI 2.1, 8×GMSL, and various IO's, ensuring seamless integration. It can be served as brain of humanoid. Supporting LLM & Physical AI frameworks like NVIDIA Isaac, Hugging Face, PyTorch, and ROS2/1, it bridges AI and robotics. With optimized real-time processing, it runs vision AI, transformers, and multimodal models, unlocking advanced AI for edge devices.

## Features

- Supports **NVIDIA Jetson AGX Thor T5000 and T4000** modules
- Up to **2070 TFLOPS** of AI performance
- Up to **4x 10GbE RJ45** ports
- **4x USB 3.2 Type-A** ports at up to 10Gbps
- **HDMI 2.1** display output
- **M.2 Key M** for PCIe Gen 4 NVMe 2280 SSD
- **M.2 Key E** for M.2 2230 Wi-Fi modules
- **M.2 Key B** for 4G/5G modules
- Up to **8x GMSL2 cameras** through two Mini-Fakra connectors and GMSL extension boards
- Robotics I/O including isolated CAN, RS-232/422/485, I2C, I2S, GPI, and GPO
- Wide-range **19V to 48V DC** input through XT30
- Software platform: **JetPack 7.1**

## Specifications



      Module Compatibility
      NVIDIA Jetson AGX Thor T5000 / T4000


      PCB Size
      168 mm x 155 mm (without the Jetson AGX Thor module)


      Display
      1x HDMI 2.1


      USB
      4x USB 3.2 Type-A (10Gbps, Host), 1x USB 2.0 Type-C (Debug), 1x USB 3.0 Type-C (Recovery)


      Ethernet
      4x RJ45 10GbE with T5000; 3x RJ45 10GbE with T4000


      M.2 Key M
      1x M.2 Key M for PCIe Gen 4 NVMe 2280 SSD


      M.2 Key E
      1x M.2 Key E for M.2 2230 Wi-Fi module


      M.2 Key B
      1x M.2 Key B for 4G/5G module


      Serial
      1x RS-232/422/485 (DB9 connector)


      JST Ports
      4x CAN with T5000 or 2x CAN with T4000, 1x RS-485, 1x I2S, 1x I2C, 4x GPI, and 4x GPO


      Audio
      1x microphone input and 1x audio output


      Fan
      1x 4-pin fan connector (12V PWM)


      RTC
      1x RTC 2-pin header


      LEDs
      1x green PWR LED, 1x green SSD LED, and 1x RGB USR LED


      Buttons
      1x Recovery button and 1x Reset button


      GMSL
      2x Mini-Fakra connectors for up to 8x GMSL2 cameras


      Operating Temperature
      -10°C to 60°C with thermal grease; -10°C to 55°C with a thermal pad


      Power Supply
      XT30, 19V to 48V DC


      JetPack
      JetPack 7.1



## Hardware Overview

| **Side View 1** |
|:---------:|
| ![fig1](https://files.seeedstudio.com/wiki/reComputer_Robotics_J601/Getting_Start/robotics_j601_carrier_board_getting_started_04.jpg) |
| **Side View 2** |
| ![fig2](https://files.seeedstudio.com/wiki/reComputer_Robotics_J601/Getting_Start/robotics_j601_carrier_board_getting_started_05.jpg) |
| **Bottom View** |
| ![fig3](https://files.seeedstudio.com/wiki/reComputer_Robotics_J601/Getting_Start/robotics_j601_carrier_board_getting_started_06.jpg) |

## Flash JetPack

Here, we will show you how to flash JetPack to an NVMe SSD connected to the reComputer Robotics J6014 / J6015. Both devices use the J601 carrier board, and the flashing procedure is the same.

### Supported Module

- [NVIDIA Jetson T4000 module](https://www.seeedstudio.com/NVIDIA-Jetson-AGX-Thor-T4000-Module-p-6939.html)
- [NVIDIA Jetson T5000 module](https://www.seeedstudio.com/NVIDIA-Jetson-AGX-Thor-T5000-Module-p-6938.html)

### Prerequisites

- Ubuntu host PC
- reComputer Robotics J6014 or J6015
- NVMe M.2 2280 Internal SSD
- USB Type-C data transmission cable
- At least 220 GB of free storage on the host PC

> [!NOTE]
> We recommend using a physical Ubuntu host instead of a virtual machine. Seeed Jetson DevelopTool also supports Windows through WSL2, but a native Ubuntu host provides the most reliable flashing experience.
>
>
>
>
>          JetPack Version
>          Ubuntu Version (Host Computer)
>
>
>          20.04
>          22.04
>          24.04
>
>
>         JetPack 7.1
>
>          ✅
>          ✅
>
>
>
>

### Choose a Flashing Method

Select either the graphical Seeed Jetson DevelopTool workflow or the command-line workflow below.

#### Option

Seeed Jetson DevelopTool provides a guided graphical workflow that downloads, verifies, extracts, and flashes the firmware without requiring BSP commands. Install the tool by following the [Seeed Jetson DevelopTool installation guide](https://wiki.seeedstudio.com/jetson_developtool_installation/).

#### Video Tutorial

> Embedded media: <https://www.youtube.com/embed/O2rlSOdYujE>

#### Software Flashing Workflow

<details>

<summary> Step-by-Step </summary>

**Step 1.** Launch Seeed Jetson DevelopTool and open **Flash Center**. Select **reComputer J601** and **JetPack 7.1 (L4T 38.4.0)**.

![image](https://files.seeedstudio.com/wiki/reComputer_Robotics_J601/Getting_Start/robotics_j601_carrier_board_getting_started_07.jpg)

**Step 2.** Connect the host PC to the **USB 3.0 Type-C flashing port**. Press and hold the **RECOVERY** button, connect the 19V to 48V DC power supply through XT30, and then release the button after two seconds.

![image](https://files.seeedstudio.com/wiki/reComputer_Robotics_J601/Getting_Start/robotics_j601_carrier_board_getting_started_08.jpg)

**Step 3.** Click **Detect Device**. Confirm that the connected Jetson module is detected (for example, **AGX Thor T5000**), and then click **Next**.

![image](https://files.seeedstudio.com/wiki/reComputer_Robotics_J601/Getting_Start/robotics_j601_carrier_board_getting_started_09.jpg)

**Step 4.** Click **Download / Prepare BSP**. The tool downloads the firmware, verifies its SHA256 checksum, and extracts the BSP automatically.

![image](https://files.seeedstudio.com/wiki/reComputer_Robotics_J601/Getting_Start/robotics_j601_carrier_board_getting_started_10.jpg)

**Step 5.** Click **Start Flash** and wait until the interface reports that flashing is complete. Do not disconnect the power supply or USB cable during this process.

> [!WARNING]
> Flashing erases the data on the target NVMe SSD. Back up important data before you begin.

**Step 6.** Connect the reComputer Robotics J601 to an HDMI display and complete the initial system configuration.

![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/J401/jetpack6_configuration.png)

</details>

#### Option

Download and flash the JetPack image that matches the Jetson module on your board. Both products use the same J601 carrier board; select the tab for your module:

#### Option

#### Prepare the JetPack Image

  <colgroup>
    <col />
    <col />
    <col />
    <col />
    <col />
  </colgroup>


      JetPack Version
      Jetson Module
      Product
      Download Link
      SHA256




      7.1 (L4T 38.4.0)
      AGX Thor T5000
      reComputer Robotics J6015

        <a href="https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/IQAq5ofKK9Y1RaCzAfJ8-3J4ARhePBbGBc-mcjQ1bNAP0bY?e=CbmAN9" target="_blank" rel="noopener noreferrer">Download</a>

      3f75780b43f6559bc950b6a97aa38fd6f61d4d001cce870bdfb498f64e6d18e5



> [!WARNING]
> The JetPack image file is large and may take around 60 minutes to download. Wait for the download to finish before extracting the archive.

To verify the downloaded firmware, run `sha256sum <file>` on the Ubuntu host and compare the result with the SHA256 value in the table.

#### Enter Force Recovery Mode

> [!NOTE]
> Before flashing, make sure the board is in Force Recovery Mode.

**Step 1.** Connect the Ubuntu host PC to the **USB 3.0 Type-C flashing port** using a USB Type-C data cable.

![image](https://files.seeedstudio.com/wiki/reComputer_Robotics_J601/Getting_Start/robotics_j601_carrier_board_getting_started_03.jpg)

**Step 2.** Press and hold the **RECOVERY** button.

**Step 3.** Connect the power supply (19V to 48V DC through XT30).

**Step 4.** Release the **RECOVERY** button after two seconds.

**Step 5.** On the host PC, run `lsusb`. The following entry confirms that the board is in Force Recovery Mode:

- **0955:7026 NVIDIA Corp.**

![image](https://files.seeedstudio.com/wiki/reComputer_Robotics_J601/Getting_Start/robotics_j601_carrier_board_getting_started_02.jpg)

#### Flash to Jetson

**Step 1.** Extract the downloaded image:

```bash
cd <path-to-image>
sudo tar xpf mfi_recomputer-thor-carrier-j6015-7.1-38.4.0-YYYY-MM-DD.tar.gz
```

**Step 2.** Flash JetPack to the NVMe SSD:

```bash
cd mfi_recomputer-thor-carrier-j6015
sudo ./tools/kernel_flash/l4t_initrd_flash.sh --flash-only --showlogs --external-device nvme0n1p1 -c tools/kernel_flash/flash_l4t_t264_nvme.xml -S 80GiB --network usb0 recomputer-thor-carrier-j6015 external
```

The flash command usually takes 2–10 minutes. The following output indicates a successful flash:

![image](https://files.seeedstudio.com/wiki/reComputer-J4012/4.png)

**Step 3.** Connect the reComputer Robotics J6015 to an HDMI display and complete the initial system configuration.

![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/J401/jetpack6_configuration.png)

#### Option

#### Prepare the JetPack Image

  <colgroup>
    <col />
    <col />
    <col />
    <col />
    <col />
  </colgroup>


      JetPack Version
      Jetson Module
      Product
      Download Link
      SHA256




      7.1 (L4T 38.4.0)
      AGX Thor T4000
      reComputer Robotics J6014

        <a href="https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/IQBofCO4bWF9SLdbLQE1V8DgAS1tW6-UmQGEH3ULOZ7W16o?e=zdnK3s" target="_blank" rel="noopener noreferrer">Download</a>

      c63eddfe7005a088ab439c64fb5d3bf9a52b85d62d377c6a4bf829295f7222ef



> [!WARNING]
> The JetPack image file is large and may take around 60 minutes to download. Wait for the download to finish before extracting the archive.

To verify the downloaded firmware, run `sha256sum <file>` on the Ubuntu host and compare the result with the SHA256 value in the table.

#### Enter Force Recovery Mode

> [!NOTE]
> Before flashing, make sure the board is in Force Recovery Mode.

**Step 1.** Connect the Ubuntu host PC to the **USB 3.0 Type-C flashing port** using a USB Type-C data cable.

![image](https://files.seeedstudio.com/wiki/reComputer_Robotics_J601/Getting_Start/robotics_j601_carrier_board_getting_started_03.jpg)

**Step 2.** Press and hold the **RECOVERY** button.

**Step 3.** Connect the power supply (19V to 48V DC through XT30).

**Step 4.** Release the **RECOVERY** button after two seconds.

**Step 5.** On the host PC, run `lsusb`. The following entry confirms that the board is in Force Recovery Mode:

- **0955:7226 NVIDIA Corp.**

![image](https://files.seeedstudio.com/wiki/reComputer_Robotics_J601/Getting_Start/robotics_j601_carrier_board_getting_started_02.jpg)

#### Flash to Jetson

**Step 1.** Extract the downloaded image:

```bash
cd <path-to-image>
sudo tar xpf mfi_recomputer-thor-carrier-j6014-7.1-38.4.0-YYYY-MM-DD.tar.gz
```

**Step 2.** Flash JetPack to the NVMe SSD:

```bash
cd mfi_recomputer-thor-carrier-j6014
sudo ./tools/kernel_flash/l4t_initrd_flash.sh --flash-only --showlogs --external-device nvme0n1p1 -c tools/kernel_flash/flash_l4t_t264_nvme.xml -S 80GiB --network usb0 recomputer-thor-carrier-j6014 external
```

The flash command usually takes 2–10 minutes. The following output indicates a successful flash:

![image](https://files.seeedstudio.com/wiki/reComputer-J4012/4.png)

**Step 3.** Connect the reComputer Robotics J6014 to an HDMI display and complete the initial system configuration.

![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/J401/jetpack6_configuration.png)

⚙️ **All `.dts` files and other source code for Seeed's Jetson carrier boards can be downloaded from** [Linux_for_Tegra](https://github.com/Seeed-Studio/Linux_for_Tegra).

> [!NOTE]
> Complete the **System Configuration** according to your needs after the first boot.

For detailed interface usage, please refer to [Robotics J601 Hardware Interfaces Usage](https://wiki.seeedstudio.com/recomputer_jetson_robotics_j601_interfaces_usage/).

## What Can You Do with J601?

After you flash JetPack, explore the demo wikis below to see what you can build on reComputer Robotics J601. These cards are generated automatically from published Jetson **Application** and **Other Devices** wikis that mention **J601** or **Jetson Thor**.

## Resources

- [reComputer J601 Carrier Board Datasheet](../../../../reComputer%20Jetson%20carrier%20board/reComputer%20Robotics%20J601/Datasheet/reComputer_J601_datasheet.pdf)
- [reComputer J601 Carrier Board Schematic](../../../../reComputer%20Jetson%20carrier%20board/reComputer%20Robotics%20J601/Schematic/reComputer%20J601%20Carrier%20Board_V1.0_SCH_260612.pdf)
- [reComputer J601 3D File](https://files.seeedstudio.com/products/NVIDIA-Jetson/reComputer_J601.stp)
- [Seeed NVIDIA Jetson Product Catalog](../../../../reComputer%20Jetson%20carrier%20board/Common/Datasheet/Seeed-NVIDIA_Jetson_Catalog_V1.4.pdf)
- [Seeed NVIDIA Jetson Success Cases](../../../../reComputer%20Jetson%20carrier%20board/Common/Datasheet/Seeed_NVIDIA_Jetson_Success_Cases_and_Examples.pdf)
- [Seeed Jetson AGX One Pager](../../../../reComputer%20Jetson%20carrier%20board/Common/Datasheet/seeed_jetson_agx_new_series.pdf)
- [Linux_for_Tegra BSP source](https://github.com/Seeed-Studio/Linux_for_Tegra)
- [reComputer J601 Carrier Board Product Page](https://www.seeedstudio.com/reComputer-J601-Carrier-Board-for-Jetson-AGX-Thor-p-6937.html)

## Tech Support

Thank you for choosing our products! We are here to provide you with different support to ensure that your experience with our products is as smooth as possible.

<https://forum.seeedstudio.com/>
<https://www.seeedstudio.com/contacts>

<https://discord.gg/eWkprNDMU7>
<https://github.com/Seeed-Studio/wiki-documents/discussions/69>
