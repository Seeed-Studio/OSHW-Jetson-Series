# RTL8852BE Wireless Module for Jetson

![image](https://files.seeedstudio.com/wiki/reComputer/rtl8852be/8852be.png)

  [Get One Now 🖱️](https://www.seeedstudio.com/RTL8852BE-WIFI-Module-M-2-Key-E-p-6835.html)

The RTL8852BE is a Wi-Fi 6 (802.11ax) M.2 wireless module based on the Realtek chipset. It integrates a PCIe interface for WLAN and a USB interface for Bluetooth, delivering significantly higher throughput and lower latency compared to previous-generation Wi-Fi 5 modules. It is ideal for embedded devices such as [reComputer J4012](https://www.seeedstudio.com/reComputer-J4012-p-5586.html) that require high-performance wireless connectivity.

## Features

- Supports 2.4 GHz / 5 GHz dual-band
- IEEE 802.11 a/b/g/n/ax (Wi-Fi 6)
- PHY rate up to 1200 Mbps on 5 GHz band
- Form factor: M.2 2230, A key or E key
- Power Supply: DC 3.3V
- Supports Linux (JetPack 5 / JetPack 6), Windows 10/11

## Specifications


      Chipset
      **RTL8852BE**


      WLAN Standards
      IEEE 802.11 a/b/g/n/ax (Wi-Fi 6)


      BT Specification
      Bluetooth 5.2


      Host Interface
      PCIe 2.1/2.0 for WLAN & USB 2.0 for Bluetooth


      Antenna
      Connect to the external antennas through MHF4 connector


      Dimension
      M.2 2230 (22 x 30 x 2.15 mm)


      Power Supply
      DC 3.3V


      Max Wireless Speed
      Up to 1200 Mbps


      Operation Temperature
      -20°C to +70°C


      Operation Humidity
      10% to 95% RH (Non-Condensing)



## Supported Devices

All reComputer Seri

- All reComputer Series

## Driver Installation

The RTL8852BE module may be detected by the Jetson as a PCIe device but may not have its driver loaded automatically. You will need to install the driver manually depending on your JetPack version.

```bash
lspci | grep -i network
```

  ![image](https://files.seeedstudio.com/wiki/reComputer/rtl8852be/lspci.PNG)

### JetPack 5.x

For JetPack 5, use the [lwfinger/rtw8852be](https://github.com/lwfinger/rtw8852be) driver:

```bash
git clone https://github.com/lwfinger/rtw8852be.git
cd rtw8852be/
sudo apt-get update
sudo apt-get install make gcc linux-headers-$(uname -r) build-essential git
```

  ![image](https://files.seeedstudio.com/wiki/reComputer/rtl8852be/jp5_install.png)

```bash
make
sudo make install
sudo modprobe 8852be
```

### JetPack 6.x

For JetPack 6, use the [rtw89](https://github.com/a5a5aa555oo/rtw89) driver:

```bash
git clone https://github.com/a5a5aa555oo/rtw89
cd rtw89
```

Edit the `Makefile` to set the correct kernel headers path:

```diff
# JP 6.2
KDIR ?= /usr/src/linux-headers-5.15.148-tegra-ubuntu22.04_aarch64/3rdparty/canonical/linux-jammy/kernel-source/

# JP 6.0
KDIR ?= /usr/src/linux-headers-5.15.136-tegra-ubuntu22.04_aarch64/3rdparty/canonical/linux-jammy/kernel-source
```

  ![image](https://files.seeedstudio.com/wiki/reComputer/rtl8852be/makefile.png)

Then build and install:

```bash
make
sudo make install
sudo modprobe rtw89_8852be
```

  ![image](https://files.seeedstudio.com/wiki/reComputer/rtl8852be/jp6_install.png)

## Verify the Wireless Module
> [!NOTE]
> The interface name may vary depending on the JetPack version:
>
> - JetPack 5: typically `wlan0`
> - JetPack 6: may appear as `wlP1p1s0`
>
> Adjust the interface name in the commands below accordingly.Use following command to figure out:
> ```bash
> ifconfig
> ```
>
>   ![image](https://files.seeedstudio.com/wiki/reComputer/rtl8852be/interface.png)
>
>

## Configure the Wireless Network

### Scan for Nearby WiFi Networks

```bash
sudo iw dev wlan0 scan | grep -E "SSID|freq"
```

Replace `wlan0` with your actual interface name if different.

### Connect to a WiFi Network

```bash
sudo nmcli device wifi connect "YOUR_SSID" password "YOUR_PASSWORD" ifname wlan0
```

  ![image](https://files.seeedstudio.com/wiki/reComputer/rtl8852be/link_wifi.PNG)

### Verify WiFi 6 Connection

Check the current link status:

```bash
iw dev wlan0 link
```

  ![image](https://files.seeedstudio.com/wiki/reComputer/rtl8852be/veryfiy_wifi6.PNG)

The output will show information such as:

- **freq**: The operating frequency (e.g., 5180 MHz corresponds to 5 GHz band)
- **HE-MCS**: The Wi-Fi 6 modulation and coding scheme (e.g., MCS 9 represents the highest coding efficiency)
- **TX/RX rate**: The current transmit and receive speeds

## Bluetooth Configuration

The Bluetooth functionality of the RTL8852BE module can be configured using `bluetoothctl`:

```bash
bluetoothctl
```

  ![image](https://files.seeedstudio.com/wiki/reComputer/rtl8852be/bluetooth.png)

## Tech Support & Product Discussion

Thank you for choosing our products! We are here to provide you with different support to ensure that your experience with our products is as smooth as possible. We offer several communication channels to cater to different preferences and needs.

<https://forum.seeedstudio.com/>
<https://www.seeedstudio.com/contacts>

<https://discord.gg/eWkprNDMU7>
<https://github.com/Seeed-Studio/wiki-documents/discussions/69>
