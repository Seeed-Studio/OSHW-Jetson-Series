# Getting Started with reComputer Robotics

The reComputer Robotics J401 is a compact, high-performance edge AI carrier board designed for advanced robotics. Compatible with NVIDIA Jetson Orin Nano/Orin NX modules in Super/MAXN mode, it delivers up to 157 TOPS of AI performance. Equipped with extensive connectivity options—including dual Gigabit Ethernet ports, M.2 slots for 5G and Wi-Fi/BT modules, 6 USB 3.2 ports, CAN, GMSL2 (via optional expansion), I2C, and UART—it serves as a powerful robotic brain capable of processing complex data from various sensors. Pre-installed with JetPack 6 and Linux BSP, it ensures seamless deployment.​

  ![image](https://media-cdn.seeedstudio.com/media/catalog/product/cache/bb49d3ec4ee05b6f018e93f896b8a25d/1/-/1-114110310-recomputer-robotics_2.jpg)

[Get One Now 🖱️](https://www.seeedstudio.com/reComputer-Robotics-J4012-p-6505.html)

<!-- Buy links -->

## Features

- **Robust Hardware Design**: A compact, high-performance edge AI computer with NVIDIA® Jetson™ Orin™ NX 16GB module in Super/MAXN mode, providing up to 157 TOPS of AI performance.
- **Multiple Interfaces for robotics**: Including dual RJ45, M.2 slots for 5G/Wi-Fi/BT modules, 6x USB 3.2, 2x CAN, GMSL2(additional purchase), I2C, and UART, functioning as a powerful robotic brain.
- **Software Setup**: Pre-installed with JetPack 6.2 and Linux BSP for seamless deployment.
- **Application and Benefit**: Ideal for rapid development of autonomous robots, accelerating time-to-market with ready-to-use interfaces and optimized AI frameworks.
- **Wide Operating Range**: Operates reliably across a temperature range of -20°C to 60°C at 25W mode and -20°C to 50°C at 40W mode

## Specification

### Carrier Board Specifications



      Category
      Item
      Details




      Storage
      M.2 KEY M PCIe
      1x M.2 KEY M PCIe (M.2 NVMe 2280 SSD 128G included)


      Networking
      M.2 KEY E
      1x M.2 Key E for WiFi/Bluetooth module


      M.2 KEY B
      1x M.2 Key B for 5G module


      Ethernet
      2x RJ45 Gigabit Ethernet


      I/O
      USB
      6x USB 3.2 Type-A (5Gbps);<br>1x USB 3.0 Type-C (Host/DP 1.4);<br>1x USB 2.0 Type-C (Device Mode/Debug)


      Camera
      1x 4 in 1 GMSL2 (mini fakra) (optional board)


      CAN
      2x CAN0 (XT30(2+2));<br>3x CAN1 (4-Pin GH 1.25 Header)


      Display
      1x DP1.4 (Type C Host)


      UART
      1x UART 4-Pin GH 1.25 Header


      I2C
      2x I2C 4-Pin GH 1.25 Header


      Fan
      1x 4-Pin Fan Connector (5V PWM);<br>1x 4-Pin Fan Connector (12V PWM)


      Extension Port
      1x Camera Expansion Header (for GMSL2 board)


      RTC
      1x RTC 2-pin;<br>1x RTC Socket


      LED
      3x LED (PWR, ACT, and User LED)


      Pinhole Button
      1x PWR;<br>1x RESET


      DIP Switch
      1x REC


      Antenna Hole
      5x Antenna Hole


      Power
      19-54V XT30(2+2) (XT30 to 5525 DC Jack Cable included)


      Jetpack Version
      JetPack 6 pre-installed; JetPack 7.2 supported


      Mechanical
      Dimensions (W x D x H)
      115mm x 115mm x 38mm


      Weight
      1100g


      Installation
      Desk, Wall-mounting


      Operating Temperature
      -20℃~55℃ (25W Mode);<br>-20℃~50℃ (MAXN Mode);<br>(with reComputer Robotics heat sink with fan)


      Warranty
      2 Years


      Certification
      RoHS, REACH, CE, FCC, UKCA, KC



## Hardware Overview

  ![image](https://media-cdn.seeedstudio.com/media/wysiwyg/upload/image-114110308_1.jpeg)

  ![image](https://media-cdn.seeedstudio.com/media/wysiwyg/upload/image-robotic-1.jpeg)

  ![image](https://media-cdn.seeedstudio.com/media/wysiwyg/upload/image-robotic-2.jpeg)

## Flash JetPack OS

### Supported Module

- [NVIDIA® Jetson Orin™ Nano Module 4GB](https://www.seeedstudio.com/NVIDIA-JETSON-ORIN-NANO-4GB-Module-p-5553.html)
- [NVIDIA® Jetson Orin™ Nano Module 8GB](https://www.seeedstudio.com/NVIDIA-JETSON-ORIN-NANO-8GB-Module-p-5551.html?___store=retailer)
- [NVIDIA® Jetson Orin™ NX Module 8GB](https://www.seeedstudio.com/NVIDIA-Jetson-Orin-NX-Module-8GB-p-5522.html)
- [NVIDIA® Jetson Orin™ NX Module 16GB](https://www.seeedstudio.com/NVIDIA-Jetson-Orin-NX-Module-16GB-p-5523.html)

### Prerequisites

- Ubuntu host PC
- reComputer Robotics
- NVIDIA® Jetson Orin™ Nano/NX Module
- USB Type-C data transmission cable

> [!NOTE]
>
> We recommend that you use physical ubuntu host devices instead of virtual machines.
> Please refer to the table below to prepare the host machine.
>
>
>
>
>          JetPack Version
>          Ubuntu Version (Host Computer)
>
>
>          18.04
>          20.04
>          22.04
>          24.04
>
>
>         JetPack 6.x
>
>          ✅
>          ✅
>
>
>
>         JetPack 7.2
>
>          ✅
>          ✅
>          ✅
>
>
>
>
> <strong>Note:</strong> For JetPack 7.2, Ubuntu 24.04 is supported for flashing and target-side component installation only. Use Ubuntu 20.04 or 22.04 if you need host development components.
>

### Prepare the Jetpack Image

Here, we need to download the system image to our Ubuntu PC corresponding to the Jetson module we are using:



      Jetpack Version
      Jetson Module
       GMSL
      Download Link1
      SHA256




      6.2
       Orin Nano 4GB
      ✅
      <a href="https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/IQBwi3AQXJiaTZiPQaKocDSkAciLsok9znKGnAPczuZ_IfY?e=S2v5QV">Download</a>
      3dc9d5b27e01f223e6d75b50a8cd5fa3<br>3b0fb259018011418f0692ff0eb91a54


      Orin Nano 8GB
      ✅
      <a href="https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/IQB8NF028_DESZJ9WwSg2Q34AVCNXeZFkwJi8pbvCOcX4cI?e=Zahpfm">Download</a>
      9b8a11bfb335fd159bbc2f29ef47f3d0<br>0d94a88c190a58ea94762954c476c176


      Orin NX 8GB
      ✅
      <a href="https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/IQAakIBc6l2wS7qKAy-1ZeHPAbTtT8XLYaIgITvBGy8vezo?e=mPygXS">Download</a>
      dade14539ef525506dba4f59a2e99254<br>48621d89db52b8a94417f438c0cf8024


      Orin NX 16GB
      ✅
      <a href="https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/IQBnWlTaU6nIQLDOcM2KRQM6AQ6A-ODC8DnWFKRSfW8vRmc?e=1AAVH8">Download</a>
      2ed5792564202430c1550183158d2f4a<br>6c47d65af248a634cf1d4d13ee465bf4


      7.2
       Orin Nano 4GB
      ✅
      <a href="https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/IQCXU7mPG_OyR7z-VhF3E5j8AcmgsCPAZAuXSdKduZUKtHQ">Download</a>
      6c499899d6c00a1661a48974d4dfc734<br>e9cbfefc06fc9c5c02ac7040dd1f2eb8


      Orin Nano 8GB
      ✅
      <a href="https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/IQBxz11HG6naSak2wIytiRbXAaqxhsgIWFaVR9H9GfGWqus">Download</a>
      23b68b43e630d166e5079f72509c71ea<br>0e13f76e372ddd06fe22df5494ad3f41


      Orin NX 8GB
      ✅
      <a href="https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/IQBw84cKdsnuRYQLA1pkfg3mAY1x0HW0UMppZbnaDBaV6XI">Download</a>
      2712fe373afb3dff8202cdd9288b266f<br>080b76837eb13161918efd80111d9035


      Orin NX 16GB
      ✅
      <a href="https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/IQDqVVHOlgc7T6b5LbNYFImdAaUr2OlKT1IkQKk2P89lCW8">Download</a>
      6d9086d692a0f40fad02c75df1ff56ae<br>d9b368320bb2bfe3a777692513529697



> [!WARNING]
> The JetPack image file is large and may take around 60 minutes to download. Please kindly wait for the download to complete.

> [!NOTE]
> To verify the integrity of the downloaded firmware, you can compare the SHA256 hash value.
>
> On an Ubuntu host machine, open the terminal and run the command `sha256sum <File>` to obtain the SHA256 hash value of the downloaded file. If the resulting hash matches the SHA256 hash provided in the wiki, it confirms that the firmware you downloaded is complete and intact.

### Enter Force Recovery Mode

> [!NOTE]
> Before we can move on to the installation steps, we need to make sure that the board is in force recovery mode.

<details>

<summary> Step-by-Step </summary>

**Step 1.** Switch the switch to the RESET mode.

  ![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/robotics_j401/flash1.jpg)

**Step 2.** Power up the carrier board by connecting the power cable.

**Step 3.** Connect the board to the Ubuntu host PC with a USB Type-C data transmission cable.

**Step 4.** On the Linux host PC, open a Terminal window and enter the command `lsusb`. If the returned content has one of the following outputs according to the Jetson SoM you use, then the board is in force recovery mode.

- For Orin NX 16GB: **0955:7323 NVidia Corp**
- For Orin NX 8GB: **0955:7423 NVidia Corp**
- For Orin Nano 8GB: **0955:7523 NVidia Corp**
- For Orin Nano 4GB: **0955:7623 NVidia Corp**

The below image is for Orin Nano 8GB

  ![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/robotics_j401/lsusb_f.png)

</details>

### Flash to Jetson

**Step 1:** Extract the downloaded image file:

```bash
cd <path-to-image>
sudo tar xpf mfi_xxxx.tar.gz
# For example: sudo tar xpf mfi_recomputer-robo-orin-nano-8g-j401-gmsl-6.2-36.4.3-2026-02-06.tar.gz
```

**Step 2:** Execute the following command to flash jetpack system to the NVMe SSD:

```bash
cd mfi_xxxx
# For example: cd mfi_recomputer-orin-robotics-j401
sudo ./tools/kernel_flash/l4t_initrd_flash.sh --flash-only --massflash 1 --network usb0  --showlogs
```

You will see the following output if the flashing process is successful

![image](https://files.seeedstudio.com/wiki/reComputer-J4012/4.png)

> [!NOTE]
> The flash command may run for 2-10 minutes.

**Step 3:** Connect the Robotics J401 to a display use the PD to HDMI adapter to connect to a display that supports HDMI input, or directly connect to a display that supports PD input using the PD cable, and finish the initial configuration setup:

  ![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/J401/jetpack6_configuration.png)

> [!NOTE]
> Please complete the **System Configuration** according to your needs.

## Hardware Interfaces Usage

> [!NOTE]
> If you want to learn more about the detailed specifications and usage of the hardware interface, please refer to [this wiki](https://wiki.seeedstudio.com/recomputer_jetson_robotics_j401_getting_started/#interfaces-usage).

## Resources

- [reComputer Robotics J401 Carrier Board Schematic](../../../../reComputer%20Jetson%20carrier%20board/reComputer%20Robotics%20J401/Schematic/reComputer%20Robotics%20J401_V1.0_SCH_250421.pdf)
- [reComputer Robotics J401 Carrier Board Datasheet](../../../../reComputer%20Jetson%20carrier%20board/reComputer%20Robotics%20J401/Datasheet/reComputer_robotics_J401_datasheet.pdf)
- [reComputer Robotics 3D file](../../../../reComputer%20Jetson%20carrier%20board/reComputer%20Robotics%20J401/3D%20Model/recomputer_robotics_j401.stp)
- [Mechanical Document-reComputer Robotics PCBA](../../../../reComputer%20Jetson%20carrier%20board/reComputer%20Robotics%20J401/Mechanical/Mechanical_reComputer_Robotics_PCBA.dxf)
- [Seeed NVIDIA Jetson Product Catalog](../../../../reComputer%20Jetson%20carrier%20board/Common/Datasheet/Seeed_NVIDIA_Jetson_Catalog_in_Robotics_and_Edge_AI.pdf)
- [Nvidia Jetson Comparison](https://www.seeedstudio.com/blog/nvidia-jetson-comparison-nano-tx2-nx-xavier-nx-agx-orin/)
- [Seeed Nvidia Jetson Success Cases](../../../../reComputer%20Jetson%20carrier%20board/Common/Datasheet/Seeed_NVIDIA_Jetson_Success_Cases_and_Examples.pdf)
- [Seeed Jetson One Pager](../../../../reComputer%20Jetson%20carrier%20board/Common/Datasheet/Seeed-Jetson-one-pager.pdf)

## Tech Support & Product Discussion

Thank you for choosing our products! We are here to provide you with different support to ensure that your experience with our products is as smooth as possible. We offer several communication channels to cater to different preferences and needs.

<https://forum.seeedstudio.com/>
<https://www.seeedstudio.com/contacts>

<https://discord.gg/eWkprNDMU7>
<https://github.com/Seeed-Studio/wiki-documents/discussions/69>
