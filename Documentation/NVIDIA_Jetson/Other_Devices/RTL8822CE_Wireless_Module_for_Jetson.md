# RTL8822CE Wireless Module for Jetson

![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/wifi/RTL8822CE_Wireless_NIC_for_Jetson.png)

  [Get One Now 🖱️](https://www.seeedstudio.com/RTL8822CE-WIFI-Module-p-6313.html)

The RTL8822CE is a compact Dual-band WLAN+Bluetooth Combo M.2 Card that integrates a 2T2R Dual-band WLAN subsystem with PCI Express controllers and a Bluetooth v5.0 subsystem with USB support. Compatible with IEEE 802.11 a/b/g/n/ac standards, it delivers a maximum PHY rate of up to 867 Mbps and supports Bluetooth dual mode (v5.0/v4.2/v2.1). Ideal for high-performance wireless and Bluetooth connectivity for using with embedded devices such as [reComputer J4012](https://www.seeedstudio.com/reComputer-J4012-p-5586.html).

## Features

- Supports 2.4G/5GHz dual-band
- Wireless PHY rate can reach up to 867Mbps
- IEEE Standards: IEEE 802.11a/b/g/n/ac
- Form factor: M.2 2230 generic A key or E key
- Connect to external antenna through MHF4 connectors
- Power Supply: DC3.3V±0.2V power supply
- Supports Linux, Windows 10/11, etc.

## Specifications


      Chipset
      **TRL8822CE-CG**


      WLAN Standards
      IEEE802.11a/b/g/n/ac


      BT Specification
      Bluetooth Core Specification v5.0/4.2/2.1


      Host Interface
      PCI Express 2.1 for WLAN & USB2.0 FS for Bluetooth


      Antenna
      Connect to the external antennas through MHF4 connector


      Dimension
      M.2 30*22*2.15mm (L*W*H)


      Power Supply
      DC 3.3V±0.2V@ 1000mA(Max)


      Operation Temperature
      -20℃ to +70℃


      Operation Humidity
      10% to 95% RH (Non-Condensing)



## Supported Devices

- [reComputer J4012](https://www.seeedstudio.com/reComputer-J4012-w-o-power-adapter-p-5628.html)
- [reComputer J4011](https://www.seeedstudio.com/reComputer-J4011-w-o-power-adapter-p-5629.html)
- [reComputer J3011](https://www.seeedstudio.com/reComputer-J3011-w-o-power-adapter-p-5630.html)
- [reComputer J3010](https://www.seeedstudio.com/reComputer-J3010-w-o-power-adapter-p-5631.html)

## Hardware Connection

> [!WARNING]
> In this wiki, we will use the reComputer J4012 as an example to demonstrate how to install and configure a RTL8822CE wireless module on Jetson device.

Step1. Prepare all materials that will be used.

- reComputer J4012 equipped with Jetpack 5.1.2
- Infineon Wi-Fi Module

Step 2. Insert the wireless module into the M.2 Key E port.

  ![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/wifi/rtl8822ce.jpg)

## Configure the Wireless Module

We can directly access the Jetson desktop and connect to wifi network through `Settings` --> `WiFi`.

  ![image](https://files.seeedstudio.com/wiki/reComputer/Hard_ware/Infineon_wifi_module/connect_to_wifi.png)

We can also configure Bluetooth through `Settings` --> `Bluetooth`.

> [!NOTE]
> Additionally, we can configure the wireless module via the command line, such as using the `bluetoothctl` command to configure Bluetooth devices.
>
>
>   ![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/A608/J401-bluetooth-test.png)
>
>

## Tech Support & Product Discussion

Thank you for choosing our products! We are here to provide you with different support to ensure that your experience with our products is as smooth as possible. We offer several communication channels to cater to different preferences and needs.

<https://forum.seeedstudio.com/>
<https://www.seeedstudio.com/contacts>

<https://discord.gg/eWkprNDMU7>
<https://github.com/Seeed-Studio/wiki-documents/discussions/69>
