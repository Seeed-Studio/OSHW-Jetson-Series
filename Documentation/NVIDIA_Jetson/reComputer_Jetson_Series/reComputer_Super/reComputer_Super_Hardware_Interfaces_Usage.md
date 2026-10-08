# reComputer Super Hardware and Interfaces Usage

![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/reComputer-super/super.png)

This wiki introduces the various different hardware and interfaces on the reComputer Super and how to use them to expand your project ideas.

[Get One Now 🖱️](https://www.seeedstudio.com/reComputer-Super-Bundle.html)

## CSI Camera

The reComputer Super supports standard 4 MIPI CSI cameras for image and video capture. Please follow the steps below to connect and test your camera.

### Hardware Connection

  ![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/reComputer-super/sci.jpg)

**Step1.** Open the back cover of the Recomputer Super.

**Step2.** Connect the MIPI CSI camera to the appropriate CSI port on the reComputer Super board.

**Step3.** Secure the camera and ensure the connection is firm.

### Usage Instruction

> [!NOTE]
> Before using the CSI camera, please ensure you have installed a JetPack version with the necessary camera drivers.

**Step1.** Check if the camera is recognized by the system:

```bash
ls /dev/video*
```

**Step2.** (Optional) Install video utilities if not already present:

```bash
sudo apt install v4l-utils
```

**Step3.** Start the camera and display the video stream using the following command:

```bash
nvgstcapture-1.0 --sensor-id=0
```

> [!NOTE]
> Change `--sensor-id` to the appropriate value if you have multiple cameras.

  ![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/reComputer-super/csi.png)

---

## USB

The reComputer Super has a total of 4 USB 3.2 ports and 1 USB 2.0 Type-C port for debugging.

### USB 3.2 port

We can enter `watch -n 1 lsusb -tv` in the Jetson terminal to probe the USB ports. Once a USB device is connected, the detailed information about that port will be displayed here.

  ![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/J501/usb_lsusb.png)

Additionally, you can  test the read and write speed of USB storage devices by using the `dd` command:

- **Read:**

  ```bash
  sudo dd if=/dev/sda of=/dev/null bs=1024M count=5 iflag=direct
  ```


  ![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/reComputer-super/usb_read.png)

- **Write:**

  ```bash
  sudo dd if=/dev/zero of=/dev/sda bs=1024M count=5 conv=fdatasync
  ```

  ![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/reComputer-super/usb_w.png)

### USB 2.0 Type-C port

Using this serial port, via the USB C data cable, you can monitor the debugging information of input and output on the PC side.

**Step1.** Switch the switch to the debug mode.

  ![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/reComputer-super/debug.jpg)

**Step2.** Connect the PC via a USB data cable, downloaded the [CP210X Driver](https://www.silabs.com/developer-tools/usb-to-uart-bridge-vcp-drivers?tab=downloads) on your PC.

  ![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/reComputer-super/download_driver.png)

**Step3.** Connect the PC via a USB data cable, extract the downloaded file and install driver on your PC.

  ![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/reComputer-super/install_driver.png)

**Step4.** Open Open the Device Manager on your Windows PC and check the COM port number assigned to the reComputer Super. It should appear under "Ports (COM & LPT)" as "Silicon Labs CP210x USB to UART Bridge (COMX)", where X is the COM port number.

  ![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/reComputer-super/debug1.png)

**Step5.** Open the serial port tool(Here, we use the MobaXterm tool as an example), create a new session.

  ![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/reComputer-super/1.png)

**Step6.** Select the Serial tool.

  ![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/reComputer-super/2.png)

**Step7.** Select corresponding serial port, set the baud rate to 115200 and click "OK".

  ![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/reComputer-super/3.png)

**Step8.** Login your reComputer Super with the username and password.

  ![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/reComputer-super/4.png)

## M.2 Key M

M.2 Key M is an interface designed for high-speed solid-state drives (SSDs), providing ultra-fast data transfer speeds, ideal for high-performance applications.

### Supported SSD are as follows

- [128GB NVMe M.2 PCle Gen3x4 2280 Internal SSD](https://www.seeedstudio.com/M-2-2280-SSD-128GB-p-5332.html)
- [256GB NVMe M.2 PCle Gen3x4 2280 Internal SSD](https://www.seeedstudio.com/NVMe-M-2-2280-SSD-256GB-p-5333.html)
- [512GB NVMe M.2 PCle Gen3x4 2280 Internal SSD](https://www.seeedstudio.com/NVMe-M-2-2280-SSD-512GB-p-5334.html)
- [1TB NVMe M.2 PCle Gen3x4 2280 Internal SSD](https://www.seeedstudio.com/NVMe-M-2-2280-SSD-1TB-p-5767.html)
- [2TB NVMe M.2 PCle Gen3x4 2280 Internal SSD](https://www.seeedstudio.com/NVMe-M-2-2280-SSD-2TB-p-6265.html)

### Hardware Connection

  ![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/reComputer-super/ssd.jpg)

### Usage Instruction

Open the terminal in Jetson device and enter the following command to test the SSD's read and write speed.

```bash
#create a blank test file first
sudo touch /ssd/test
dd if=/dev/zero of=/home/seeed/ssd/test bs=1024M count=5 conv=fdatasync
```

  ![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/reComputer-super/ssd_w.png)

> [!WARNING]
> Please run `sudo rm /home/seeed/ssd/test` command to delete the cache files after the test is complete.

## M.2 Key E

The M.2 Key E interface is a compact, high-speed data interface designed for wireless communication modules such as Wi-Fi and Bluetooth, used to expand wireless capabilities.

### Hardware Connection

  ![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/reComputer-super/wifi_c.png)

### Usage Instruction

After installing the Wi-Fi module and powering on the device, we can configure the device's Wi-Fi and Bluetooth settings.

  ![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/A608/J401-wifi-bluetooth-test.gif)

Of course, we can also check the device's operating status using the following commands.

```bash
ifconfig
```

  ![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/J501/wifi_ifconfig.png)

**Bluetooth:**

  ```bash
  bluetoothctl
  scan on
  ```

  ![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/reComputer-super/bluetooth.png)

## Mini PCIe

The reComputer super comes with a mini-PCIe for LTE 4G module.

#### Hardware Connection

  ![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/reComputer-super/mini_p.png)

> [!NOTE]
> If you want to remove the SIM card, push the card in to hit the internal spring so that the SIM will come out of the slot

### Usage Instruction

**Step1.** Install minicom:

```bash
sudo apt update
sudo apt install minicom -y
```

**Step2.** Enter the serial console of the connected 4G module so that we can enter AT commands and interact with the 4G module:

```bash
sudo minicom -D /dev/ttyUSB2 -b 115200
```

**Step3.** Press Ctrl+A and then press E to turn on local echo.

**Step4.** Enter the command "AT" and press enter. If you see the response as "OK", the 4G module is working properly.

  ![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/22.jpg)

**Step5.** Enter the command "ATI" to check the module information.

  ![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/23.png)

Using 4G network for internet access

  ![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/reComputer-super/4g2.png)

## RTC

The reComputer Super features RTC interfaces, providing accurate timekeeping even when the system is powered off.

### Hardware Connection

Connect a 3V CR1225 coin cell battery to the RTC socket on the board as shown below. Make sure the **positive (+)** end of the battery is facing upwards.

  ![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/reComputer-super/rtc.jpg)

### Usage Instruction

**Step1.** Connect an RTC battery as mentioned above.

**Step2.** Turn on reComputer Super.

**Step3.** On the Ubuntu Desktop, click the drop-down menu at the top right corner, navigate to `Settings > Date & Time`, connect to a network via an Ethernet cable and select **Automatic Date & Time** to obtain the date/ time automatically.

  ![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/13.png)

> [!NOTE]
> If you have not connected to internet via Ethernet, you can manually set the date/ time here.

**Step4.** Open a terminal window, and execute the below command to check the hardware clock time:

```bash
cat /sys/devices/platform/bpmp/bpmp\:i2c/i2c-4/4-003c/nvvrs-pseq-rtc/rtc/rtc0/time
```

  ![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/reComputer-super/rtc_time1(1).png)

**Step5.** Disconnect the network connection and reboot the device. You will find that the system time has lost power but still functions normally.

  ![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/reComputer-super/rtc_time2.png)

## Ethernet

There are 2 RJ45 Gigabit Ethernet on reComputer Super supported 10/100/1000M. ETH0 is the native Ethernet port, and the other one ETH1 is converted from PCIe.

  ![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/reComputer-super/eth.jpg)

There are 2 LEDs (green and yellow) on each Ethernet port:

- Green LED: ON only when connected to 1000M/10G network.
- Yellow LED: Shows the network activity status.

Test the Ethernet speed:

```bash
iperf3 -c 192.168.254.100 -R
```

> [!NOTE]
> -c `<ip address>` is the server IP address, and -R means reverse mode.

  ![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/reComputer-super/eth_a.png)

```bash
iperf3 -c 192.168.254.100
```

  ![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/reComputer-super/eth_p.png)

## LED Indicators

The reComputer Super is equipped with 2 LED indicators (PWR and ACT) to show power status and system activity, allowing users to monitor device operation in real time.

  ![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/reComputer-super/led.jpg)

## Fan

The reComputer Super is equipped with two types of fan connectors to meet different voltage and cooling needs:

- 1x 4-Pin Fan Connector (5V PWM): Designed for low-voltage, low-power silent fans, this connector supports PWM speed control, allowing intelligent fan speed adjustment based on system temperature to improve energy efficiency and reduce noise.

- 1x 4-Pin Fan Connector (12V PWM): Compatible with standard 12V PWM fans, it also supports precise speed control, making it ideal for high-performance cooling requirements.

### Hardware Connection

  ![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/reComputer-super/fan.jpg)

> [!NOTE]
> For more information, please check [here](https://docs.nvidia.com/jetson/archives/r35.4.1/DeveloperGuide/text/SD/PlatformPowerAndPerformance/JetsonOrinNanoSeriesJetsonOrinNxSeriesAndJetsonAgxOrinSeries.html?highlight=fan#fan-profile-control).

**Set fan speed:**

  ```bash
  sudo -i
  echo 100 > /sys/bus/platform/devices/pwm-fan/hwmon/hwmon1/pwm1
  ```

Additionally, we can manually set the fan speed using the jtop tool.

## CAN

The reComputer Super series provides a CAN interface where the CAN signal is output directly from the SOM at TTL/CMOS levels, which is a non-standard differential signal requiring an external CAN transceiver to connect to a standard CAN bus; it supports CAN FD frame formats, allowing extended data length and higher data rates, making it suitable for industrial automation, robotics, automotive prototyping, and other applications requiring reliable, real-time communication.

### Hardware Connection

Please note the sequence of the connected lines (R OUT ↔ RX, D IN ↔ TX), and then convert them to CAN_L and CAN_H through the CAN bus transceiver.

  ![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/reComputer-super/can1.png)

According to the [Datasheet of reComputer Super](../../../../reComputer%20Jetson%20carrier%20board/reComputer%20Super%20J401/Manual/reComputer_super_user_manual.pdf), connect the CAN heater to the CAN bus transceiver in the corresponding manner, then connect the CAN bus transceiver to the [USB to CAN Analyzer Adapter](https://www.seeedstudio.com/USB-CAN-Analyzer-p-2888.html), and finally connect it to the Jetson for loopback communication testing.

  ![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/reComputer-super/can_port.png)

  ![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/reComputer-super/can_connect.png)

### Usage Instruction

**Step 1.** Configure and open can0:

```bash
sudo ip link set can0 down
sudo ip link set can0 type can bitrate 500000
sudo ip link set can0 up
```
**Step 2.** Communication test.
Open a terminal to receive signals.
```bash
candump can0
```

**Step 3.** Open another terminal to send the signal.
```bash
cansend can0 123#abcdabcd
```

  ![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/reComputer-super/can_loop.png)

## Extension Port

The Extension Port includes a 40-pin extension header and a 12-pin control and UART header, providing versatile connectivity options for peripherals and communication interfaces.

### 40-Pin Extension Header

  ![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/reComputer-super/40pin3.jpg)

The 40-Pin Extension Header is a versatile expansion interface that provides various functions such as GPIO, I2C, SPI, and UART, making it convenient for connecting sensors, peripherals, or other modules.

The detail of 40-pin header is shown below:

  Header Pin
  Signal
  BGA Pin
  Default Function

13.3V-Main 3.3V Supply
25V-Main 5V Supply
3I2C1_SDAPDD.02I2C #1 Data
45V-Main 5V Supply
5I2C1_SCLPDD.01I2C #1 Clock
6GND-Ground
7GPIO09PAC.06General Purpose I/O
8UART1_TXDPR.02UART #1 Transmit
9GND-Ground
10UART1_RXDPR.03UART #1 Receive
11UART1_RTSPR.04UART #1 Request to Send
12I2S0_SCLKPH.07Audio I2S #0 Clock
13SPI1_SCKPY.00SPI #1 Clock
14GND-Ground
15GPIO12PN.01General Purpose I/O
16SPI1_CS1PY.04SPI #1 Chip Select #1
173.3V-Main 3.3V Supply
18SPI1_CS0PY.03SPI #1 Chip Select #0
19SPI0_MOSIPZ.05SPI #0 Master Out / Slave In
20GND-Ground
21SPI0_MISOPZ.04SPI #0 Master In / Slave Out
22SPI1_MISOPY.01SPI #1 Master In / Slave Out
23SPI0_SCKPZ.03SPI #0 Clock
24SPI0_CS0PZ.06SPI #0 Chip Select #0
25GND-Ground
26SPI0_CS1PZ.07SPI #0 Chip Select #1
27ID_I2C_SDA (I2C0_SDA)PDD.00I2C #0 Data
28ID_I2C_SCL (I2C0_SCL)PCC.07I2C #0 Clock
29GPIO01PQ.05General Purpose I/O
30GND-Ground
31GPIO11PQ.06General Purpose I/O
32GPIO07PG.06General Purpose I/O
33GPIO13PG.00System Reserved
34GND-Ground
35I2S0_LRCK (I2S0_FS)PI.02Audio I2S #0 Frame Sync
36UART1_CTSPR.05UART #1 Clear to Send
37SPI1_MOSIPY.02SPI #1 Master Out / Slave In
38I2S0_SDIN (I2S0_DIN)PI.01Audio I2S #0 Data In
39GND-Ground
40I2S0_SDOUT (I2S0_DOUT)PI.00Audio I2S #0 Data Out

### Usage Instruction

Simple GPIO control example
```bash
#install
sudo apt-get install gpiod

# Search for the corresponding number for the pin
sudo gpiofind PH.00
gpiochip0 43

#Set the pin to H, then press Enter to release.
sudo gpioset --mode=wait 0 43=1

#Set the Pin to L, then press Enter to release.
sudo gpioset --mode=wait 0 43=0

#gpio 0_119 Low level maintained for 2 seconds
sudo gpioset --mode=time -s 2 0 119=0

#input
sudo gpioget 0 43
```
**If you want to configure the GPIO that is not enabled by default, please refer to the following steps:**

Enable 40-Pin Header:
```bash
  sudo /opt/nvidia/jetson-io/jetson-io.py
```

  ![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/reComputer-super/40_1.png)

  ![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/reComputer-super/40_2.png)

  ![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/reComputer-super/40_3.png)

Save and reboot.

**Configure the uncontrolled GPIO through the Overlay configuration:**

**Step 1.** Download and extract the [overlay package](../../../../reComputer%20Jetson%20carrier%20board/Common/overlay.zip) to your jetson device.
```bash
wget ../../../../../../../../reComputer%20Jetson%20carrier%20board/Common/overlay.zip
```
**Step 2.** Copy build.sh and gpio-overlay.dts to Jetson.

**Step 3.** Edit the `pio-overlay.dts` file and modify it to include the pinmux definitions for the pins you need.
> [!NOTE]
> more details you can see in [jetson-orin-nx-and-orin-nano-series-pinmux-config](https://developer.nvidia.com/downloads/jetson-orin-nx-and-orin-nano-series-pinmux-config-template)

**Step 3.**   Enable overlay configuration.
```bash
sudo bash ./build.sh
#The following command needs to be executed only once.
sudo /opt/nvidia/jetson-io/config-by-hardware.py -n "seeed gpio config Overlay"
```
**Step 4.** Reboot the device enables the configuration to take effect.
```bash
sudo reboot
```
**Step 5.** Now you can control the pins by `gpioset` that were just modified.
```bash
#For example px7
sudo gpioset --mode=wait 0 121=1
```

### 12-Pin Control and UART Header

  ![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/reComputer-super/12pin2.jpg)

The 12-Pin Control and UART Header provides essential control signals and UART communication interfaces for connecting and managing external devices.

> [!NOTE]
> The pin functions of reComputer Super are similar to those of reComputer Classic. For more detailed information, please refer to [here](https://wiki.seeedstudio.com/J401_carrierboard_Hardware_Interfaces_Usage/#gpio).

## HDMI

reComputer Super is equipped with an HDMI 2.1 Type A port, which supports a resolution of 7680x4320. This allows for ultra-high-definition video output.

## Resources
- [User Manual&Datasheet](../../../../reComputer%20Jetson%20carrier%20board/reComputer%20Super%20J401/Manual/reComputer_super_user_manual.pdf)
- [Temperature Test Report](../../../../reComputer%20Jetson%20carrier%20board/reComputer%20Super%20J401/Manual/reComputer_Super_Temperature_Test_Report.pdf)
- [Schematic](../../../../reComputer%20Jetson%20carrier%20board/reComputer%20Super%20J401/Schematic/reComputer%20Super%20J401_v1.0_SCH_PDF_250401.pdf)
- [3D File](../../../../reComputer%20Jetson%20carrier%20board/reComputer%20Super%20J401/3D%20Model/reComputer%20Super%20J401.stp)
- [Mechanical Document-reComputer Super](../../../../reComputer%20Jetson%20carrier%20board/reComputer%20Super%20J401/Mechanical/Mechanical_reComputer_Super.dxf)
- [Mechanical Document-reComputer Super PCBA](../../../../reComputer%20Jetson%20carrier%20board/reComputer%20Super%20J401/Mechanical/Mechanical_reComputer_Super_PCBA.dxf)

## Tech Support & Product Discussion

Thank you for choosing our products! We are here to provide you with different support to ensure that your experience with our products is as smooth as possible. We offer several communication channels to cater to different preferences and needs.

<https://forum.seeedstudio.com/>
<https://www.seeedstudio.com/contacts>

<https://discord.gg/eWkprNDMU7>
<https://github.com/Seeed-Studio/wiki-documents/discussions/69>
