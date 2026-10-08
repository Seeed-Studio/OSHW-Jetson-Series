# Getting start with reComputer J1010

![image](https://media-cdn.seeedstudio.com/media/catalog/product/cache/bb49d3ec4ee05b6f018e93f896b8a25d/1/-/1-110061362-recomputer-j1010-first.jpg)

[Get One Now 🖱️](https://www.seeedstudio.com/Jetson-10-1-A0-p-5336.html)

## Introduction

reComputer J1010 is a compact edge computer built with NVIDIA Jetson Nano 4GB  production module, comes with 128 NVIDIA CUDA® cores deliver 0.5 TFLOPs (FP16) to run AI frameworks and applications like image classification, object detection, and speech processing. The production modules offers 16GB eMMC, a longer warranty, and 5-10 year operating life in a production environment([Jetson FAQ](https://developer.nvidia.com/embedded/faq)). We also have reComputer [J20 series](https://www.seeedstudio.com/reComputer-J2021-p-5438.html?queryID=14111cbf2ca4f2951fd8a4c1762eb435&objectID=5438&indexName=bazaar_retailer_products) built with a Jetson Xavier NX module, delivering 21 TOPS AI performance for more complex AI workloads.

Besides the Jetson module, reComputer J1010 also includes [J101 carrier board](https://www.seeedstudio.com/reComputer-J101-v2-Carrier-Board-for-Jetson-Nano-p-5396.html) with onboard microSD card slot, 1×USB 3.0, 2×USB2.0, HDMI, M.2 Key E for WiFI, LTE and Bluetooth, RTC, Raspberry Pi GPIO 40-pin, and so on, as well as a heatsink, and aluminum case. The device has been pre-installed Jetpack 4.6.1, just plug in a USB C 5V/3A power supply, keyboard, mouse, and ethernet cable, you are ready to start your embedded AI journey! If you need more USB 3.0 and onboard M.2 key M for attaching SSD, you can choose reComputer J1020.

Note: We received customer inquiries they need more storage than 16GB eMMC offered. For orders after July 30th, 2022, we have included the microSD card slot on the [carrier board](https://www.seeedstudio.com/reComputer-J101-v2-Carrier-Board-for-Jetson-Nano-p-5396.html) of reComputer J1010. Please check the [guide](https://wiki.seeedstudio.com/J1010_Boot_From_SD_Card/#flashing-system-from-j101-to-sd-card) on boot image to microSD card and adjust I/O speed.

## Features

- **Hand-size edge AI full system:** delivering modern AI power of 0.5 TFLOPs (FP16)  and rich interfaces for embedded development.
- **Ready for development and deployment:** pre-installed NVIDIA JetPack supports the entire [Jetson software stack](https://developer.nvidia.com/embedded/develop/software) and industry-leading [AI developer tools](https://wiki.seeedstudio.com/Jetson-AI-developer-tools/) for building robust AI applications such as logistics, retail, service, agriculture, smart city, healthcare, and life sciences, etc
- **Power efficient:** powered by Type C 5V/3A, consuming as little as 5 watts.
- **Expandable:** with the onboard interfaces and reComputer case, able to mount on the wall with mounting holes on the back.

## Specifications



      Specifications
      <a href="https://www.seeedstudio.com/Jetson-10-1-A0-p-5336.html">reComputer J1010</a>
      <a href="https://www.seeedstudio.com/Jetson-10-1-H0-p-5335.html">reComputer J1020</a>
      <a href="https://www.seeedstudio.com/NVIDIA-Jetson-Nano-Development-Kit-B01-p-4437.html">NVIDIA Jetson Nano Developer Kit-B01</a>




      Module
      Jetson Nano 4GB (production version)
      Nano (not production version)


      Storage
      16 GB eMMC
      MicroSD (Card not included)


      SD Card Slot
      Included (On the carrier board)
      -
      Included (On the module)


      Video Encoder
      4K30 | 2x1080p60 | 4x1080p30 | 4x720p60 | 9x720p30 (H.265 & H.264)
      4Kp30 | 4x 1080p30 | 9x 720p30 (H.264/H.265)


      Video Decoder
      4K60 | 2x 4K30 | 4x 1080p60 | 8x 1080p30 | 9x 720p60 (H.265 & H.264)
      4Kp60 | 2x 4Kp30 | 8x 1080p30 | 18x 720p30 (H.264/H.265)


      Gigabit Ethernet
      1×RJ45 Gigabit Ethernet Connector (10/100/1000)


      USB
      1 × USB 3.0 Type A; 2 × USB 2.0 Type A; 1 × USB Type C for device mode; 1 × USB Type C for 5V power input
      4 × USB 3.0 Type-A ；1 × Micro-USB port for device mode;
      4 × USB 3.0 Type-A; 1 × Micro-USB port for 5V power input  or for device mode


      CSI Camera Connect
      2×CSI Camera (15 pos, 1mm pitch, MIPI CSI-2 )


      Display
      1×HDMI Type A
      1×HDMI Type A; 1×DP


      FAN
      1× FAN Connector (5V PWM)
      1× FAN (5V PWM)


      M.2 KEY E
      1×M.2 Key E
      1×M.2 Key E (Disabled)
      1×M.2 Key E


      M.2 KEY M
      -
      1×M.2 Key M
      -


      RTC
      RTC socket(reserved)
      -


      Multifunctional port
      1× 40-Pin header


      Power Supply
      USB-Type C 5V⎓3A
      DC Jack 12V/2A
      DC Jack 5V⎓4A；Micro-USB 5V⎓2A


      Mechanical
      130 mm x 120 mm x 50 mm (with case)
      100 mm x 80 mm x 29 mm



## Flash JetPack to reComputer J1010

> [!NOTE]
> Please refer to this [wiki](https://wiki.seeedstudio.com/reComputer_J1010_J101_Flash_Jetpack/) page for more information because J1010 use J101 carrier board.

## Resources

[reComputer J1010 datasheet](../../../../../reComputer%20Jetson%20carrier%20board/reComputer%20J1010/Datasheet/reComputer-J1010-datasheet.pdf)

[reComptuer J101 Carrier Boards Schematic](../../../../../reComputer%20Jetson%20carrier%20board/reComputer%20J101/Datasheet/reComputer%20J101_V2.0_SCH_240822.pdf)

[reComputer J1010 3D file](../../../../../reComputer%20Jetson%20carrier%20board/reComputer%20J1010/3D%20Model/J1010-Jetson-Nano.stp)

[Seeed Jetson Serials Catalog](../../../../../reComputer%20Jetson%20carrier%20board/Common/Datasheet/Seeed-NVIDIA_Jetson_Catalog_V1.4.pdf)

[Seeed Studio Edge AI Success Stories](../../../../../reComputer%20Jetson%20carrier%20board/Common/Datasheet/Seeed_NVIDIA_Jetson_Success_Cases_and_Examples.pdf)

[Seeed Jetson Serials Comparision](https://www.seeedstudio.com/blog/nvidia-jetson-comparison-nano-tx2-nx-xavier-nx-agx-orin/)

[Seeed Jetson Devices One Page](../../../../../reComputer%20Jetson%20carrier%20board/Common/Datasheet/Seeed-Jetson-one-pager.pdf)
