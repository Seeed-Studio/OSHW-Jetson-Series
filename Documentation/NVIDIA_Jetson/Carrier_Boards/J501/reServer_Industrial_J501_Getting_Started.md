# Getting Started with reServer J501

  ![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/J501/reServer_J501.png)

  [Get One Now 🖱️](https://www.seeedstudio.com/reServer-Industrial-J501-Carrier-Board-Add-on.html)

The J501 carrier board is a powerful extension board that supports NVIDIA Jetson AGX Orin modules. It features rich data ports and extension interfaces, completely unleashed the full performance of the AGX Orin module. Also it supports adding GMSL extension to connect up to 8 GMSL cameras.

## Features

- **Build most powerful AI computer for edge computing:** Design to intgerate with  Jetson AGX Orin module, with up to 275 TOPS AI performance, 8 times AI performance compared to Jetson AGX Xavier. Power configurable between 15W and 60W.
- **High-speed interface support for multiple sensors:** 22 lanes of PCIe Gen4, 1x 10GbE, a Display Port, 16 lanes of MIPI CSI-2, USB 3.2 interfaces, and a 40-pin header.
- **Low-speed interface support for multiple IO:** 4x DI, 4x DO, 3x GND_DI, 2x GND_DO, 1x GND_ISO, 1x CAN, 1x RS232/RS422/RS485.
<!-- - **BSP ready for development:** Jetpack 6 supported Board BSP ready for developing your custom system image. -->

## Specifications



      I/O
      Ethernet
       1x LAN0 RJ45 GbE (10/100/1000Mbps), <br> 1x LAN RJ45 GbE (10/100/1000/10000Mbps)


      USB
       3x USB3.1, <br> 1x USB3.1 Type C(Host mode), <br> 1x USB2.0 Type C(Device mode)


      DI/DO
       4x DI,4x DO,3x GND_DI,2x GND_DO,1x GND_ISO,1x CAN
1x RS232/RS422/RS485


      Display
       1x HDMI 2.1 Type A 7680x4320


      SATA
       2x SATA III 6.0Gbps at 30 Hz


      SIM
       1x Nano SIM card slot


      Button
       Reset Button, Recovery Button


      Expansion
       Mini PCIE
       1x Mini PCIe for LoRaWAN®/4G/Series Wireless (Module not included)


       M.2 Key B
       1x M.2 Key B (3042/3052) support 4G/5G (Module not included)


       M.2 Key E
       1x M.2 Key E


       M.2 Key M
       1x M.2 Key M (PCIE 4.0)


       Fan
       1x Fan connectors (5V PWM)


       TPM
       1x TPM 2.0 connector (Module not included)


       RTC
       1x RTC socket (CR1220 included), <br>1x RTC 2-pin


       Camera
       2x Expansion connector (8lanes for each connector)


       PCIE
       1x PCIE


       Power
       Power Supply
       DC 12V-36V Terminal block 2 pin (included 24V/5A Power Adapter)


       Mechanical
       Dimensions (W x D)
       176 x 163mm (Module not included)


       Operating Temerature
       -20~60℃


       Weight
       225g (Module not included)



## Hardware Overview

  ![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/J501/hardware_overview.jpeg)

## Flash JetPack OS to J501 Carrier Board

Here, we will show you how to flash [Jetpack](https://developer.nvidia.com/embedded/jetson-linux-archive) to an NVMe SSD connected to the reServer J501.

### Supported Module

- [NVIDIA® Jetson AGX Orin™ Module 32GB](https://www.seeedstudio.com/NVIDIA-Jetson-AGX-Orin-Module-32GB-p-5956.html)
- [NVIDIA® Jetson AGX Orin™ Module 64GB](https://www.seeedstudio.com/NVIDIA-Jetson-AGX-Orin-Module-64GB-p-5957.html)

### Prerequisites

- Ubuntu host PC
- reServer J501 Carrier Board
- NVIDIA® Jetson AGX Orin™ Module 32GB/64GB
- AGX Orin Active Fan
- NVMe M.2 2280 Internal SSD
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
>
>
>         JetPack 5.x
>          ✅
>          ✅
>
>
>
>         JetPack 6.x
>
>          ✅
>          ✅
>
>
>
>

### Prepare the Jetpack Image

Here, we need to download the system image to our Ubuntu PC corresponding to the Jetson module we are using:



      Jetpack Version
      Jetson Module
       GMSL
      Download Link1
      Download Link2
      SHA256




      5.1.3
      AGX Orin 32GB
      ❌
      <a href="https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/IQD3U5NHij5gR5r4FB_AzC9vAbb3ERak_RvvIMoow0-X2fM?e=Ddf7Zi" target="_blank" rel="noopener noreferrer">Download</a>
      <a href="https://szseeedstudio-my.sharepoint.cn/:u:/g/personal/youjiang_yu_szseeedstudio_partner_onmschina_cn/ERG3upqXAQNHsJP6ZvG2MAEBGsndVCgrLnhcKvtWoGA6tA?e=14KO6z" target="_blank" rel="noopener noreferrer">Download</a>
      c673dc8ae75addf8ca3224cf700be35<br>4eec0ca41cb5ecabb8953c276213a7119


      AGX Orin 32GB
      ✅
      <a href="https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/IQD3ZjNepbc7SoC24H82Y4txAUhoSQIZ4l2ZcKGa3qgd9_E?e=bk1qc5" target="_blank" rel="noopener noreferrer">Download</a>
      <a href="https://szseeedstudio-my.sharepoint.cn/:u:/g/personal/youjiang_yu_szseeedstudio_partner_onmschina_cn/EZ7iNOxMxL9AjcKFPLygVT8Bg5qnkE-ZsMmNmHkZzNayOg?e=qv2sbB" target="_blank" rel="noopener noreferrer">Download</a>
      425a931e65f2715d8486c68565ad711<br>fd34b626ab023d025df2d84af81b62aa3


      AGX Orin 64GB
      ❌
      <a href="https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/IQClLB_mdGMPQpqEw1jxTRuFAYqxZRQJZIAtiYt7-clcocI" target="_blank" rel="noopener noreferrer">Download</a>
      F95E91C3BFB00D50EB999383F85949B4
      76abdd6de0a49bd95d57b361bebea59<br>a6a05e56779c7ceb863ad178f3ed98aaf


      AGX Orin 64GB
      ✅
      <a href="https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/IQBh9HqX5MHBQZF0WLe01k7mAXYqzHd4YJXaDt4uS2VZ8T4?e=AX0KSd" target="_blank" rel="noopener noreferrer">Download</a>
      <a href="https://szseeedstudio-my.sharepoint.cn/:u:/g/personal/youjiang_yu_szseeedstudio_partner_onmschina_cn/Eccs1larF2FNhKi8MHred5kB4pQImN4ZHSgDM3BUDVzBtQ?e=reKIhD" target="_blank" rel="noopener noreferrer">Download</a>
      49076bd4bb7179dfe38c25bd5831c03<br>296bf26e86d67d9bca766a749a14257bd


      6.0
      AGX Orin 32GB
      ❌
      <a href="https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/ERTmpYBKF2tAodLyqpajhLkBxPdGUIWXfGytdCGwNu28qw?e=cJIbtM" target="_blank" rel="noopener noreferrer">Download</a>
      <a href="https://szseeedstudio-my.sharepoint.cn/:u:/g/personal/youjiang_yu_szseeedstudio_partner_onmschina_cn/EeHcCFk-chtDnEzoXiwvxZwBQuK3I3mTOAJ8mnZJE-P2uA?e=X9g0HK" target="_blank" rel="noopener noreferrer">Download</a>
      B1C1BBB14058B0F5C00C5657A8EF8FA<br>7A4C3711DB8AD82F7E614311F95063989


      AGX Orin 32GB
      ✅
      <a href="https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/Ef5wlNXtxVRIulSKwJTT3ocBmCBlHbQNVnz3LRDJtRwlGQ?e=KAIiVS" target="_blank" rel="noopener noreferrer">Download</a>
      <a href="https://szseeedstudio-my.sharepoint.cn/:u:/g/personal/youjiang_yu_szseeedstudio_partner_onmschina_cn/EX5HoeV09eFKtWj9YhAfgZ8Bt2k9bxxxSO5-TQBZoGLB-Q?e=hvcfG1" target="_blank" rel="noopener noreferrer">Download</a>
      0C58022F626321EE42464AACBB47029<br>6B1AFE0A7256787158539BE7EC73E19C6


      AGX Orin 64GB
      ❌
      <a href="https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/IQClLB_mdGMPQpqEw1jxTRuFAYqxZRQJZIAtiYt7-clcocI" target="_blank" rel="noopener noreferrer">Download</a>
      <a href="https://szseeedstudio-my.sharepoint.cn/:u:/g/personal/youjiang_yu_szseeedstudio_partner_onmschina_cn/EY-HFdsaHWVOvJJ5fMynVO0BvEOv5W0h1IxeSfesNFRYag?e=5thYHs" target="_blank" rel="noopener noreferrer">Download</a>
      4077631986A66EB3AF5FBF4FF2FBDBC<br>CD07E4DC1AA4076414EB1F4640AF72451


      AGX Orin 64GB
      ✅
      <a href="https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/IQClLB_mdGMPQpqEw1jxTRuFAYqxZRQJZIAtiYt7-clcocI" target="_blank" rel="noopener noreferrer">Download</a>
      <a href="https://szseeedstudio-my.sharepoint.cn/:u:/g/personal/youjiang_yu_szseeedstudio_partner_onmschina_cn/EUmpL5LNJDRLjoC6oQg6Vv4BgQ9eA4MUl4yE43fycz667w?e=Xw5nga" target="_blank" rel="noopener noreferrer">Download</a>
      8DCFF0FFBA81B756B0C62E50F4A106B<br>44116CC8171C05F48A328DE594D6A4CD9


      6.2
      AGX Orin 32GB
      ❌
      <a href="https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/EfhMqk5d6tFKiDqbtyWKFdsBV-NLqs9L4NBY0dRC-Y_jHw?e=JQMYcn" target="_blank" rel="noopener noreferrer">Download</a>
       -
      69CFD82D0C70B55D5BDD34E3EAF7AE8<br>DDCE002CCCDBA3DCEE40F40CD8BBA0478


      AGX Orin 32GB
      ✅
      <a href="https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/Edgau76MPUZAnuAixzf7TSUBGF2edqqdZO3mHRaZB_Gd7Q?e=omVwi3" target="_blank" rel="noopener noreferrer">Download</a>
       -
      3BAEB35868E4B187F4B7C35FA44D8E0<br>BD9486161E14F9F073993216F83DFA0E4


      AGX Orin 64GB
      ❌
      <a href="https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/IQCcNYUtYA0RTL2GQwXFv35rAdWnduxknLXrUtQNxklpIZo" target="_blank" rel="noopener noreferrer">Download</a>
       -
      B6A9F41B8B42060D19F811B718E4B71<br>FCBE699BB9EC7A50B4B24DF205003111B


      AGX Orin 64GB
      ✅
      <a href="https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/IQCcNYUtYA0RTL2GQwXFv35rAdWnduxknLXrUtQNxklpIZo" target="_blank" rel="noopener noreferrer">Download</a>
       -
      AA04EFB99374DCDC89A57C039FA4E1F<br>F5C9371B22F8ED83612AC4C799CCB2640



> [!WARNING]
> The jetpack5 image file is approximately **4.5GB** in size and should take around 15 minutes to download. The Jetpack6 image file is approximately **16.7GB** in size and should take around 60 minutes to download. Please kindly wait for the download to complete.

> [!NOTE]
> To verify the integrity of the downloaded firmware, you can compare the SHA256 hash value.
>
> On an Ubuntu host machine, open the terminal and run the command `sha256sum <File>` to obtain the SHA256 hash value of the downloaded file. If the resulting hash matches the SHA256 hash provided in the wiki, it confirms that the firmware you downloaded is complete and intact.

### Enter Force Recovery Mode

> [!NOTE]
> Before we can move on to the installation steps, we need to make sure that the board is in force recovery mode.

> Embedded media: <https://www.youtube.com/embed/CGMGZGqZPKM>

<details>

<summary> Step-by-Step </summary>

**Step 1.** Press and hold the force recovery button without releasing it.

  ![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/J501/button.jpg)

**Step 2.** Power up the carrier board by connecting the power cable.

**Step 3.** Release the force recovery button.

**Step 4.** Connect the board to the Ubuntu host PC with a USB Type-C data transmission cable.

**Step 5.** On the Linux host PC, open a Terminal window and enter the command `lsusb`. If the returned content has one of the following outputs according to the Jetson SoM you use, then the board is in force recovery mode.

- For AGX Orin 32GB: **0955:7223 NVidia Corp**
- For AGX Orin 64GB: **0955:7023 NVidia Corp**

The below image is for AGX Orin 32GB

  ![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/J501/lsusb.png)

</details>

### Flash to Jetson

**Step 1:** Extract the downloaded image file:

```bash
cd <path-to-image>
sudo tar xpf mfi_xxxx.tar.gz
# For example: sudo tar xpf mfi_recomputer-orin-nano-8g-j401-6.0-36.3.0-2024-06-07.tar.gz
```

**Step 2:** Execute the following command to flash jetpack system to the NVMe SSD:

```bash
cd mfi_xxxx
# For example: cd mfi_recomputer-orin-j401
sudo ./tools/kernel_flash/l4t_initrd_flash.sh --flash-only --massflash 1 --network usb0  --showlogs
```

You will see the following output if the flashing process is successful

![image](https://files.seeedstudio.com/wiki/reComputer-J4012/4.png)

> [!NOTE]
> The flash command may run for 2-10 minutes.

**Step 3:** Connect the J501 to a display using the HDMI connector on the board and finish the initial configuration setup:

  ![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/J401/jetpack6_configuration.png)

> [!NOTE]
> Please complete the **System Configuration** according to your needs.

**Step 4 (Optional):** Install Nvidia Jetpack SDK

Please open the terminal on the Jetson device and execute the following commands:

```bash
sudo apt update
sudo apt install nvidia-jetpack
```

## Hardware Interfaces Usage

> [!NOTE]
> If you want to learn more about the detailed specifications and usage of the hardware interfaces, please refer to [this wiki](https://wiki.seeedstudio.com/j501_carrier_board_interfaces_usage/).

## Resources

- [reServer Industrial J501 Carrier Board Datasheet](../../../../reServer%20Jetson%20carrier%20board/reServer%20Industrial%20J501/Datasheet/reServer_Industrial_J501_Carrier_Board_Datasheet.pdf)
- [reServer Industrial J501 Schematic](../../../../reServer%20Jetson%20carrier%20board/reServer%20Industrial%20J501/Schematic/202003906_reServer_Industrial_J501_Carrier_Board_v1.0_SCH_PDF_20240529.pdf)
- [reServer Industrial J501 3D File](../../../../reServer%20Jetson%20carrier%20board/reServer%20Industrial%20J501/3D%20Model/RESERVER_AGX_ORIN_CARRIER_BOARD.stp.gz)
- [Seeed Jetson Serials Catalog](../../../../reComputer%20Jetson%20carrier%20board/Common/Datasheet/Seeed-NVIDIA_Jetson_Catalog_V1.4.pdf)
- [Seeed Studio Edge AI Success Stories](../../../../reComputer%20Jetson%20carrier%20board/Common/Datasheet/Seeed_NVIDIA_Jetson_Success_Cases_and_Examples.pdf)
- [Seeed Jetson Serials Comparision](https://www.seeedstudio.com/blog/nvidia-jetson-comparison-nano-tx2-nx-xavier-nx-agx-orin/)
- [Seeed Jetson Devices One Page](../../../../reComputer%20Jetson%20carrier%20board/Common/Datasheet/Seeed-Jetson-one-pager.pdf)

## Tech Support & Product Discussion

Thank you for choosing our products! We are here to provide you with different support to ensure that your experience with our products is as smooth as possible. We offer several communication channels to cater to different preferences and needs.

<https://forum.seeedstudio.com/>
<https://www.seeedstudio.com/contacts>

<https://discord.gg/eWkprNDMU7>
<https://github.com/Seeed-Studio/wiki-documents/discussions/69>
