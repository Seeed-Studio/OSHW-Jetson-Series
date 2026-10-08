# J401B Interfaces Usage

## Introduction

  ![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/J401B/j401b_interfaces.png)

This wiki introduces the various different hardware and interfaces on the reComputer J401B and how to use them to expand your project ideas.

  [Get One Now 🖱️](https://www.seeedstudio.com/reComputer-J401B-optional-accessories.html)

## Mini-PCIe

reComputer J401B comes with a mini PCIe connector that supports 4G.

### Supported 4G Module

- [LTE Cat 4 EC25-AFXGA](https://www.seeedstudio.com/LTE-Cat-4-EC25-AFXGA-mini-PCIe-p-5668.html)
- [LTE Cat 4 EC25-EUX](https://www.seeedstudio.com/LTE-Cat-4-EC25-EUX-mini-PCIe-p-5669.html)
- [LTE Cat 4 EC25-AUXGR](https://www.seeedstudio.com/LTE-Cat-4-EC25-AUXGR-mini-PCIe-p-5885.html)
- [LTE Cat 4 EC25-EFA](https://www.seeedstudio.com/LTE-Cat-4-EC25-EFA-mini-PCIe-p-5824.html)
- [LTE Cat 4 EC25-EMGA](https://www.seeedstudio.com/LTE-Cat-4-EC25-EMGA-mini-PCIe-p-5831.html)
- [LTE Cat 4 EC25-JFA](https://www.seeedstudio.com/LTE-Cat-4-EC25-JFA-mini-PCIe-p-5899.html)

### Connection Overview

- Step1. Install the 4G Module
- Step2. Attach the Antennas
- Step3. Insert the SIM Card


> Embedded media: <https://www.youtube.com/embed/q5nV0RqvceU>

### Usage

- Setp1. Open Mobile Broadband and configure the network connection according to the specifications of the 4G SIM card. `Settings` --> `Network` --> `Mobile Broadband`

- Setp2. Open a browser to test if the 4G network is functioning properly.

> Embedded media: <https://www.youtube.com/embed/IJEvmHhrmbc>

## 260 Pin SODIMM

The main function of 260 pin SODIMM is to connect your carrier board with **[NVIDIA Jetson Orin Nano 4GB](https://www.seeedstudio.com/NVIDIA-JETSON-ORIN-NANO-4GB-Module-p-5553.html?___store=retailer)/[NVIDIA Jetson Orin Nano 8GB](https://www.seeedstudio.com/NVIDIA-JETSON-ORIN-NANO-8GB-Module-p-5551.html)**, **[NVIDIA Jetson Orin NX 8GB](https://www.seeedstudio.com/NVIDIA-Jetson-Orin-NX-Module-8GB-p-5522.html)/[NVIDIA Jetson Orin NX 16GB](https://www.seeedstudio.com/NVIDIA-Jetson-Orin-NX-Module-16GB-p-5523.html)**.

### Connection Overview

![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/A608/Jetson-connect-J401.gif)

> [!NOTE]
> If the connection is correct, when you connect your power adapter, you will see the power indicator light up.

## M.2 Key M

M.2 Key M is a specification for the physical and electrical layout of an M.2 connector that supports high-speed data transfer using the PCIe (Peripheral Component Interconnect Express) interface. M.2 Key M connectors are commonly used for connecting solid-state drives (SSDs) and other high-performance expansion cards to a motherboard or other host device. The "Key M" designation refers to the specific pin configuration and keying of the M.2 connector, which determines the type of devices that can be connected to it.

### Supported SSD are as follows

- [128GB NVMe M.2 PCle Gen3x4 2280 Internal SSD](https://www.seeedstudio.com/M-2-2280-SSD-128GB-p-5332.html)
- [256GB NVMe M.2 PCle Gen3x4 2280 Internal SSD](https://www.seeedstudio.com/NVMe-M-2-2280-SSD-256GB-p-5333.html)
- [512GB NVMe M.2 PCle Gen3x4 2280 Internal SSD](https://www.seeedstudio.com/NVMe-M-2-2280-SSD-512GB-p-5334.html)
- [1TB NVMe M.2 PCle Gen3x4 2280 Internal SSD](https://www.seeedstudio.com/NVMe-M-2-2280-SSD-1TB-p-5767.html)
- [2TB NVMe M.2 PCle Gen3x4 2280 Internal SSD](https://www.seeedstudio.com/NVMe-M-2-2280-SSD-2TB-p-6265.html)

### Connection Overview

If you want to remove the included SSD and install a new one, you can follow the steps below.

![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/A608/J401-Install-new-ssd.gif)

### Usage

We will explain how to do a simple benchmark on the connected SSD.

- **Step 1:** Check the write speed by executing the below command.

```sh
sudo dd if=/dev/zero of=/home/nvidia/test bs=1M count=512 conv=fdatasync
```

- **Step 2:** Check the read speed by executing the below commands. Make sure to execute this after executing the above command for write speed.

```sh
sudo sh -c "sync && echo 3 > /proc/sys/vm/drop_caches"
sudo dd if=/home/nvidia/test of=/dev/null bs=1M count=512
```

## M.2 Key E

M.2 Key E is a specification for the physical and electrical layout of an M.2 connector that supports wireless communication modules, such as Wi-Fi and Bluetooth cards. The "Key E" designation refers to the specific pin configuration and keying of the M.2 connector, which is optimized for wireless networking devices. M.2 Key E connectors are commonly found on motherboards and other devices that require wireless connectivity options.Here we recommand [Intel wifi/bluetooth](https://www.seeedstudio.com/RTL8822CE-Wireless-NIC-Kits-for-Nvidia-Jetson-Orin.html?qid=eyJjX3NlYXJjaF9xdWVyeSI6Ijg4MjIiLCJjX3NlYXJjaF9yZXN1bHRfcG9zIjozLCJjX3RvdGFsX3Jlc3VsdHMiOjQsImNfc2VhcmNoX3Jlc3VsdF90eXBlIjoiUHJvZHVjdCIsImNfc2VhcmNoX2ZpbHRlcnMiOiJzdG9yZUNvZGU6W3JldGFpbGVyXSJ9) module.

### Connection Overview

![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/A608/J401-connect-wifi-model.gif)

### Usage

After installing wifi/bluetooth module, you can see the wifi/bluetooth icon in the top right corner.

![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/A608/J401-wifi-bluetooth-test.gif)

#### Wi-Fi test

```
ifconfig
```

![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/A608/J401-wifi-test.png)

#### Bluetooth test

```
bluetoothctl
power on   #open bluetooth
agent on   #registe agent
scan on    #search other bluetooths
connect xx:xx:xx:xx #connect target bluetooth
paired-devices #show all paired devices
```

![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/A608/J401-bluetooth-test.png)

## CSI Cameras

CSI stands for Camera Serial Interface. It is a specification that describes a serial communication interface for transferring video data from image sensors to a host processor. CSI is commonly used in mobile devices, cameras, and embedded systems to enable high-speed and efficient transfer of image and video data for processing and analysis.

### Supported cameras are as follows

- IMX219 cameras

  - [Raspberry Pi Camera V2](https://www.seeedstudio.com/Raspberry-Pi-Camera-Module-V2.html)

  <!-- - [IMX219-130 8MP Camera with 130° FOV](https://www.seeedstudio.com/IMX219-130-Camera-130-FOV-Applicable-for-Jetson-Nano-p-4606.html)
  - [IMX219-160 8MP Camera with 160° FOV](https://www.seeedstudio.com/IMX219-160-Camera-160-FOV-Applicable-for-Jetson-Nano-p-4603.html)
  - [IMX219-200 8MP Camera with 200° FOV](https://www.seeedstudio.com/IMX219-200-Camera-200-FOV-Applicable-for-Jetson-Nano-p-4609.html) -->

  - [IMX219-77 8MP Camera with 77° FOV](https://www.seeedstudio.com/IMX219-77-Camera-77-FOV-Applicable-for-Jetson-Nano-p-4608.html)
  - [IMX219 M12/CS mount CMOS Camera Module](https://www.seeedstudio.com/IMX-219-CMOS-camera-module-M12-and-CS-camera-available-p-5372.html)
  - [IMX219-83 8MP 3D Stereo Camera Module](https://www.seeedstudio.com/IMX219-83-Stereo-Camera-8MP-Binocular-Camera-Module-Depth-Vision-Applicable-for-Jetson-Nano-p-4610.html)
  - [IMX219-77IR 8MP IR Night Vision Camera with 77° FOV](https://www.seeedstudio.com/IMX219-77IR-Camera-77-FOV-Infrared-Applicable-for-Jetson-Nano-p-4607.html)
  - [IMX219-160IR 8MP Camera with 160° FOV](https://www.seeedstudio.com/IMX219-160IR-Camera160-FOV-Infrared-Applicable-for-Jetson-Nano-p-4602.html)

- IMX477 cameras

  - [Raspberry Pi High Quality Camera](https://www.seeedstudio.com/Raspberry-Pi-High-Quality-Cam-p-4463.html)
  - [Raspberry Pi HQ Camera - M12 mount](https://www.seeedstudio.com/Raspberry-Pi-HQ-Camera-M12-mount-p-5578.html)
  - [High Quality Camera for Raspberry Pi](https://www.seeedstudio.com/High-Quality-Camera-For-Raspberry-Pi-Compute-Module-Jetson-Nano-p-4729.html)

### Connection Overview

Here the 2 CSI camera connectors are marked as **CAM0 and CAM1**. You can either connect one camera to any connector out of the 2 or connect 2 cameras to both the connectors at the same time.

![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/A608/camera-connect-J401.gif)

### Usage

Open your terminal(Ctrl+Alt+T) and input command like below:

```sh
sudo /opt/nvidia/jetson-io/jetson-io.py
```

![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/A608/J401-cameral.gif)

#### Option

For CAM0 port

```sh
nvgstcapture-1.0 sensor-id=0
```

For CAM1 port

```sh
nvgstcapture-1.0 sensor-id=1
```

> [!NOTE]
> If you want to change further settings of the camera, you can type **"nvgstcapture-1.0 --help"** to access all the configurable options available.

#### Option

For CAM0 port

```sh
gst-launch-1.0 nvarguscamerasrc sensor-id=0 sensor-mode=0 ! 'video/x-raw(memory:NVMM),width=1920, height=1080, framerate=20/1, format=NV12' ! nvvidconv ! xvimagesink
```

For CAM1 port

```sh
gst-launch-1.0 nvarguscamerasrc sensor-id=1 sensor-mode=0 ! 'video/x-raw(memory:NVMM),width=1920, height=1080, framerate=20/1, format=NV12' ! nvvidconv ! xvimagesink
```

> [!NOTE]
> If you want to change further settings of the camera, you can update the arguments such as **width, height, framerate, format**, etc.

## RTC

RTC stands for Real-Time Clock. It is a clock that keeps track of the current time and date independently of the main system clock. RTCs are commonly used in computers, embedded systems, and other electronic devices to maintain accurate timekeeping even when the device is powered off. They are often powered by a small battery to ensure continuous operation and retain time and date information during power cycles.

### Connection Overview

#### Option

Connect a **3V CR1220 coin cell battery** to the RTC socket on the board as shown below. Make sure the **positive (+)** end of the battery is facing upwards.

![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/A608/J401-connect-coin-cell-back.gif)

#### Option

Connect a **3V CR2302 coin cell battery with JST connector** to the 2-pin 1.25mm JST socket on the board as shown below:

![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/A608/J401-connect-coin-cell.gif)

### Usage

- **Step 1:** Connect an RTC battery as mentioned above.

- **Step 2:** Turn on reComputer Industrial.

- **Step 3:** On the Ubuntu Desktop, click the drop-down menu at the top right corner, navigate to `Settings > Date & Time`, connect to a network via an Ethernet cable and select **Automatic Date & Time** to obtain the date/ time automatically.

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/13.png)

> [!NOTE]
> If you have not connected to internet via Ethernet, you can manually set the date/time here.

- **Step 4:** Open a terminal window, and execute the below command to check the hardware clock time.

```sh
sudo hwclock
```

You will see the output something like below which is not the correct date/time.

![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/A608/J401-RTC.png)

- **Step 5:** Change the hardware clock time to the current system clock time by entering the below command.

```sh
sudo hwclock --systohc
```

- **Step 6:** Remove any Ethernet cables connected to make sure it will not grab the time from the internet and reboot the board.

```sh
sudo reboot
```

- **Step 7:** Check hardware clock time to verify that the date/ time stays the same eventhough the device was powered off.

- **Step 8:** Create a new shell script using any text editor of your preference. Here we use **vi** text editor.

```sh
sudo vi /usr/bin/hwtosys.sh
```

- **Step 9:** Enter **insert mode** by pressing **i**, copy and paste the following content inside the file.

```sh
#!/bin/bash

sudo hwclock --hctosys
```

- **Step 10:** Make the script executable.

```sh
sudo chmod +x /usr/bin/hwtosys.sh
```

- **Step 11:** Create a systemd file.

```sh
sudo nano /lib/systemd/system/hwtosys.service
```

- **Step 12:** Add the following inside the file.

```sh
[Unit]
Description=Change system clock from hardware clock

[Service]
ExecStart=/usr/bin/hwtosys.sh

[Install]
WantedBy=multi-user.target
```

- **Step 13:** Reload systemctl daemon.

```sh
sudo systemctl daemon-reload
```

- **Step 14:** Enable the newly created service to start on boot and start the service.

```sh
sudo systemctl enable hwtosys.service
sudo systemctl start hwtosys.service
```

- **Step 15:** Verify the script is up and running as a systemd service.

```sh
sudo systemctl status hwtosys.service
```

- **Step 16:** Reboot the board and you will the system clock is now in sync with the hardware clock.

## Fan control

nvfancontrol is a userspace fan speed control daemon. This manages the fan speed based on the temperature-to-fan-speed mapping table in the nvfancontrol configuration file.

There are some basic elements in the nvfancontrol service, including Tmargin, kickstart PWM, fan profile, fan control, and fan governor. All of these can be programmed via the configuration file based on the user’s preferences. This chapter will explain each of them in the following sections.

> [!NOTE]
> If you want to change  nvfancontrol.conf make sure you have read [it](https://docs.nvidia.com/jetson/archives/r35.4.1/DeveloperGuide/text/SD/PlatformPowerAndPerformance/JetsonOrinNanoSeriesJetsonOrinNxSeriesAndJetsonAgxOrinSeries.html?highlight=fan#fan-profile-control)

### Usage

#### Option

- **Step 1:** Stop the nvfancontrol systemd service.

```
sudo systemctl stop nvfancontrol
```

- **Step 2:** Change nvfancontrol.conf.

```
vi /etc/nvfancontrol.conf
```

> [!NOTE]
> After you change nvfancontrol.conf, print `Ese` and `:q` to quit

- **Step 3:** Remove the status file.

```
sudo rm /var/lib/nvfancontrol/status
```

- **Step 4:** Restart nvfancontrol systemd service.

```
sudo systemctl restart nvfancontrol
```

#### Option

- **Step 1:**  Enter root model.

```
sudo -i
```

- **Step 2:**  Stop the nvfancontrol systemd service.

```
sudo systemctl stop nvfancontrol
```

- **Step 3:**  Change PWM value.

```
echo 100 > /sys/devices/platform/pwm-fan/hwmon/hwmon3/pwm1
```

> [!NOTE]
> The larger of value, the faster of fan speed. PWM value should between 0 to 255, maybe **hwmon3** is not your pathword so check your own pathword

- **Step 4:**  Check rpm.

```
cat /sys/class/hwmon/hwmon0/rpm
```

## GPIO

**The detail of 40-pin header is shown below:**

  Header Pin
  Module Pin Name
  Module Pin
  SoC Pin name
  Default Usage
  Alternate Functionality



      1
      -
      -
      -
      Main 3.3V Supply
      -


      2
      -
      -
      -
      Main 5.0V Supply
      -


      3
      I2C1_SDA
      191
      DP_AUX_CH3_N
      I2C #1 Data
      -


      4
      -
      -
      -
      Main 5.0V Supply
      -


      5
      I2C1_SCL
      189
      DP_AUX_CH3_P
      I2C #1 Clock
      -


      6
      -
      -
      -
      Ground
      -


      7
      GPIO09
      211
      AUD_MCLK
      GPIO
      Audio Master Clock


      8
      UART1_TXD
      203
      UART1_TX
      UART #1 Transmit
      GPIO


      9
      -
      -
      -
      Ground
      -


      10
      UART1_RXD
      205
      UART1_RX
      UART #1 Receive
      GPIO


      11
      UART1_RTS*
      207
      UART1_RTS
      GPIO
      UART #2 Request to Send


      12
      I2S0_SCLK
      199
      DAP5_SCLK
      GPIO
      Audio I2S #0 Clock


      13
      SPI1_SCK
      106
      SPI3_SCK
      GPIO
      SPI #1 Shift Clock


      14
      -
      -
      -
      Ground
      -


      15
      GPIO12
      218
      TOUCH_CLK
      GPIO
      -


      16
      SPI1_CSI1*
      112
      SPI3_CS1
      GPIO
      SPI #1 Chip Select #1


      17
      -
      -
      -
      GPIO
      -


      18
      SPI1_CSI0*
      110
      SPI3_CS0
      GPIO
      SPI #0 Chip Select #0


      19
      SPI0_MOSI
      89
      SPI1_MOSI
      GPIO
      SPI #0 Master Out/Slave In


      20
      -
      -
      -
      Ground
      -


      21
      SPI0_MISO
      93
      SPI1_MISO
      GPIO
      SPI #0 Master In/Slave Out


      22
      SPI1_MISO
      108
      SPI3_MISO
      GPIO
      SPI #1 Master In/Slave Out


      23
      SPI0_SCK
      91
      SPI1_SCK
      GPIO
      SPI #0 Shift Clock


      24
      SPI0_CS0*
      95
      SPI1_CS0
      GPIO
      SPI #0 Chip Select #0


      25
      -
      -
      -
      Ground
      -


      26
      SPI0_CS1*
      97
      SPI1_CS1
      GPIO
      SPI #0 Chip Select #1


      27
      I2C0_SDA
      187
      GEN2_I2C_SDA
      I2C #0 Data
      GPIO


      28
      I2C0_SCL
      185
      GEN2_I2C_SCL
      I2C #0 Clock
      GPIO


      29
      GPIO01
      118
      SOC_GPIO41
      GPIO
      General Purpose Clock #0


      30
      -
      -
      -
      Ground
      -


      31
      GPIO11
      216
      SOC_GPIO42
      GPIO
      General Purpose Clock #1


      32
      GPIO07
      206
      SOC_GPIO44
      GPIO
      PWM


      33
      GPIO13
      228
      SOC_GPIO54
      GPIO
      PWM


      34
      -
      -
      -
      Ground
      -


      35
      I2S0_FS
      197
      DAP5_FS
      GPIO
      Audio I2S #0 Field Select


      36
      UART1_CTS*
      209
      UART1_CTS
      GPIO
      UART #1 Clear to Send


      37
      SPI1_MOSI
      104
      SPI3_MOSI
      GPIO
      SPI #1 Master Out/Slave In


      38
      I2S0_DIN
      195
      DAP5_DIN
      GPIO
      Audio I2S #0 Data in


      39
      -
      -
      -
      Ground
      -


      40
      I2S0_DOUT
      193
      DAP5_DOUT
      GPIO
      Audio I2S #0 Data Out



### UART

UART stands for Universal Asynchronous Receiver/Transmitter. It is a communication protocol used for serial communication between two devices. UART communication involves two pins: one for transmitting data (TX) and one for receiving data (RX). It is asynchronous, meaning that data is transmitted without a shared clock signal between the devices. UART is commonly used in various applications such as microcontrollers, sensors, and communication between different electronic devices.

#### Connection Overview

The UART interface is using the pin below, or you can use another UART interface on J401:



      Header Pin
      Module Pin Name
      Module Pin
      SoC Pin name
      Default Usage
      Alternate Funcationality




      6
      -
      -
      -
      Ground
      -


      8
      UART1_TXD
      203
      UART1_TX
      UART #1 Transmit
      GPIO


      10
      UART1_RXD
      205
      UART1_RX
      UART #1 Receive
      GPIO



Connect the J401 with TTL with UART as below:



      J401 Header Pin
       Usage
      USB translate TTL
      Usage




      6
      Ground
      GND
      Ground


      8
      UART1_TXD
      U_RX
      UART_RX


      10
      UART1_RXD
      U_TX
      UART_TX



![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/A608/J401-UART-connect.gif)

#### Usage

- **Step 1:** Install [PuTTy](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) on your windows laptop, and set PuTTy as below:

![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/A608/J401-windows-uart-set.png)

- **Step 2:** Install PuTTy on Jetson, open your terminal(ALT+Ctrl+T) and type the following command.

```
sudo apt install putty
```

- **Step 3:** Use PuTTy on Windows send 'hello linux' to Jetson, and use PuTTy on Jetson send 'hello windows' to windwos.

> [!NOTE]
> Make sure your baudrate have be set 115200.

The result is as below:

![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/A608/J401-uart-result.gif)

### I2C

I2C stands for Inter-Integrated Circuit. It is a widely used serial communication protocol that enables communication between multiple integrated circuits in a system. I2C uses two bidirectional lines: one for data (SDA) and one for clock (SCL). Devices connected on an I2C bus can act as either a master or a slave, allowing for multiple devices to communicate with each other. I2C is popular for its simplicity, flexibility, and ability to connect a variety of devices such as sensors, memory chips, and other peripherals in embedded systems and electronic devices.

#### Connection Overview

The I2C interface is using pin as below, or you can use other I2C interface on J401:



      Header Pin
      Module Pin Name
      Module Pin
      SoC Pin name
      Default Usage
      Alternate Funcationality



      2
      -
      -
      -
      Main 5.0V Supply
      -


      3
      I2C1_SDA
      191
      DP_AUX_CH3_N
      I2C #1 Data
      -


      5
      I2C1_SCL
      189
      DP_AUX_CH3_P
      I2C #1 Clock
      -


      6
      -
      -
      -
      Ground
      -



Connect the J401 to [Grove-3-Axis Digital Accelerometer](https://www.seeedstudio.com/Grove-3-Axis-Digital-Accelerometer-1-5g.html) with I2C as below:



      J401
      Usage
      Grove-3-Axis Digital Accelerometer
      Usage



      2
      5V supply
      Vcc
      -


      3
      I2C1_SDA
      SDA
      I2C_SDA


      5
      I2C1_SCL
      SCL
      I2C_SCL


      6
      Ground
      GND
      Ground


![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/A608/J401-I2C-connect.gif)

#### Test

Open your terminal(ALT+Ctrl+T) and type the following command:

```
i2cdetect -y -r 7
```

> [!NOTE]
> Your channel may be different from mine in the commmand: ```i2cdetect -y -r x```.

You will see the result as below, before connecting to the I2C, no I2C device was detected on channel 7, but afterwards an I2C device with the address 0x19 was detected.:

![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/A608/J401-I2C-test.png)

> [!NOTE]
> If you want to use general IO pins for logic control, please refer to [this wiki](https://wiki.seeedstudio.com/reComputer_Jetson_GPIO/).

## Tech Support & Product Discussion

Thank you for choosing our products! We are here to provide you with different support to ensure that your experience with our products is as smooth as possible. We offer several communication channels to cater to different preferences and needs.

<https://forum.seeedstudio.com/>
<https://www.seeedstudio.com/contacts>

<https://discord.gg/eWkprNDMU7>
<https://github.com/Seeed-Studio/wiki-documents/discussions/69>
