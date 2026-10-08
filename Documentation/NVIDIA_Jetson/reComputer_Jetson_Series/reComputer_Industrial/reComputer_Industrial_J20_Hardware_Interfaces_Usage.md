# reComputer Industrial J20 Hardware and Interfaces Usage

This wiki introduces the various different hardware and interfaces on the reComputer Industrial J2012, J2011 and how to use them to expand your project ideas.

## Disassemble reComputer Industrial

First of all,it is better to disassemble the outer enclosure to access all the interfaces. Unscrew the 4 screws located at the back as follows in order to disassemble reComputer Industrial

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/98.png)

## CSI Cameras

reComputer Industrial is equipped with **2x 2-lane 15pin MIPI CSI camera connectors** and the below cameras are supported

- IMX219 cameras

  - [Raspberry Pi Camera V2](https://www.seeedstudio.com/Raspberry-Pi-Camera-Module-V2.html)
  - [IMX219-130 8MP Camera with 130° FOV](https://www.seeedstudio.com/IMX219-130-Camera-130-FOV-Applicable-for-Jetson-Nano-p-4606.html)
  - [IMX219-160 8MP Camera with 160° FOV](https://www.seeedstudio.com/IMX219-160-Camera-160-FOV-Applicable-for-Jetson-Nano-p-4603.html)
  - [IMX219-200 8MP Camera with 200° FOV](https://www.seeedstudio.com/IMX219-200-Camera-200-FOV-Applicable-for-Jetson-Nano-p-4609.html)
  - [IMX219-77 8MP Camera with 77° FOV](https://www.seeedstudio.com/IMX219-77-Camera-77-FOV-Applicable-for-Jetson-Nano-p-4608.html)
  - [IMX219 M12/CS mount CMOS Camera Module](https://www.seeedstudio.com/IMX-219-CMOS-camera-module-M12-and-CS-camera-available-p-5372.html)
  - [IMX219-83 8MP 3D Stereo Camera Module](https://www.seeedstudio.com/IMX219-83-Stereo-Camera-8MP-Binocular-Camera-Module-Depth-Vision-Applicable-for-Jetson-Nano-p-4610.html)
  - [IMX219-77IR 8MP IR Night Vision Camera with 77° FOV](https://www.seeedstudio.com/IMX219-77IR-Camera-77-FOV-Infrared-Applicable-for-Jetson-Nano-p-4607.html)
  - [IMX219-160IR 8MP Camera with 160° FOV](https://www.seeedstudio.com/IMX219-160IR-Camera160-FOV-Infrared-Applicable-for-Jetson-Nano-p-4602.html)
  - [IMX219 M12/CS mount CMOS Camera Module](https://www.seeedstudio.com/IMX-219-CMOS-camera-module-M12-and-CS-camera-available-p-5372.html)

- IMX477 cameras

  - [Raspberry Pi High Quality Camera](https://www.seeedstudio.com/Raspberry-Pi-High-Quality-Cam-p-4463.html)
  - [Raspberry Pi HQ Camera - M12 mount](https://www.seeedstudio.com/Raspberry-Pi-HQ-Camera-M12-mount-p-5578.html)
  - [High Quality Camera for Raspberry Pi](https://www.seeedstudio.com/High-Quality-Camera-For-Raspberry-Pi-Compute-Module-Jetson-Nano-p-4729.html)

### Connection Overview

Here the 2 CSI camera connectors are marked as **CAM0 and CAM1**. You can either connect one camera to any connector out of the 2 or connect 2 cameras to both the connectors at the same time.

- **Step 1:** Gently pull out the black color lock on the CSI connector

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/5.png)

- **Step 2:** Insert the 15-pin ribbon cable into the connector making sure the gold fingers are facing downwards

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/6.png)

- **Step 3:** Push in the black color lock to lock the ribbon cable in place

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/10.png)

### Usage

First you need to configure the board to load the appropriate driver for the specific camera that you will be using. For this JetPack system has an in-built tool to support IMX219 an IMX477 cameras.

- **Step 1:** Open the terminal and execute the following

```sh
sudo /opt/nvidia/jetson-io/jetson-io.py
```

- **Step 2:** Select **Configure Jetson Nano CSI Connector**

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/119.jpg)

- **Step 3:** Select **Configure for compatible hardware**

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/120.jpg)

- **Step 4:** Select the camera that you want to use

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/121.jpg)

- **Step 5:** Select **Save pin changes**

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/122.jpg)

- **Step 6:** Select **Save and reboot to reconfigure pins**

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/123.jpg)

- **Step 7:** Press any key on the keyboard and the device will reboot with the applied camera configuration

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/124.jpg)

You can use CSI cameras in 2 different methods. Follow the below commands according to the camera connector

- Method 1:

For CAM0 port

```sh
nvgstcapture-1.0 sensor-id=0
```

For CAM1 port

```sh
nvgstcapture-1.0 sensor-id=1
```

> [!NOTE]
> If you want to change further settings of the camera, you can type **"nvgstcapture-1.0 --help"** to access all the configurable options available

- Method 2:

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

reComputer Industrial is equipped with 2 different ways to connect to an RTC battery

### Connection Overview

- Method 1:

Connect a **3V CR1220 coin cell battery** to the RTC socket on the board as shown below. Make sure the **positive (+)** end of the battery is facing upwards

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/11.jpg)

- Method 2:

Connect a **3V CR2302 coin cell battery with JST connector** to the 2-pin 1.25mm JST socket on the board as shown below

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/12.jpg)

### Usage

- **Step 1:** Connect an RTC battery as mentioned above

- **Step 2:** Turn on reComputer Industrial

- **Step 3:** On the Ubuntu Desktop, click the drop-down menu at the top right corner, navigate to `Settings > Date & Time`, connect to a network via an Ethernet cable and select **Automatic Date & Time** to obtain the date/ time automatically

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/13.png)

> [!NOTE]
> If you have not connected to internet via Ethernet, you can manually set the date/ time here

- **Step 4:** Open a terminal window, and execute the below command to check the hardware clock time

```sh
sudo hwclock
```

You will see the output something like below which is not the correct date/ time

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/14.png)

- **Step 5:** Change the hardware clock time to the current system clock time by entering the below command

```sh
sudo hwclock --systohc
```

- **Step 6:** Remove any Ethernet cables connected to make sure it will not grab the time from the internet and reboot the board

```sh
sudo reboot
```

- **Step 7:** Check hardware clock time to verify that the date/ time stays the same eventhough the device was powered off

Now we will create a script to always sync the system clock from the hardware clock in each boot.

- **Step 8:** Create a new shell script using any text editor of your preference. Here we use **vi** text editor

```sh
sudo vi /usr/bin/hwtosys.sh
```

- **Step 9:** Enter **insert mode** by pressing **i**, copy and paste the following content inside the file

```sh
#!/bin/bash

sudo hwclock --hctosys
```

- **Step 10:** Make the script executable

```sh
sudo chmod +x /usr/bin/hwtosys.sh
```

- **Step 11:** Create a systemd file

```sh
sudo nano /lib/systemd/system/hwtosys.service
```

- **Step 12:** Add the following inside the file

```sh
[Unit]
Description=Change system clock from hardware clock

[Service]
ExecStart=/usr/bin/hwtosys.sh

[Install]
WantedBy=multi-user.target
```

- **Step 13:** Reload systemctl daemon

```sh
sudo systemctl daemon-reload
```

- **Step 14:** Enable the newly created service to start on boot and start the service

```sh
sudo systemctl enable hwtosys.service
sudo systemctl start hwtosys.service
```

- **Step 15:** Verify the script is up and running as a systemd service

```sh
sudo systemctl status hwtosys.service
```

- **Step 16:** Reboot the board and you will the system clock is now in sync with the hardware clock

## M.2 Key M

Out of the box, reComputer Industrial includes a 128GB SSD connected to the M.2 Key M slot, which is pre-installed with JetPack system.

### Connection Overview

If you want to remove the included SSD and install a new one, you can follow the steps below. Here we only recommend to use Seeed SSDs with [128GB](https://www.seeedstudio.com/M-2-2280-SSD-128GB-p-5332.html), [256GB](https://www.seeedstudio.com/NVMe-M-2-2280-SSD-256GB-p-5333.html) and [512GB](https://www.seeedstudio.com/NVMe-M-2-2280-SSD-512GB-p-5334.html) storage because we have only tested those SSDs. Further this interface supports PCIe Gen4.0 SSDs.

- **Step 1:** Remove the pre-installed SSD screw

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/15.png)

- **Step 2:** Remove the SSD by sliding away from the SSD connector

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/16.png)

- **Step 3:** Insert a new SSD and tighten back the screw

### Usage

We will explain how to do a simple benchmark on the connected SSD

- **Step 1:** Check the write speed by executing the below command

```sh
sudo dd if=/dev/zero of=/home/nvidia/test bs=1M count=512 conv=fdatasync
```

- **Step 2:** Check the read speed by executing the below commands. Make sure to execute this after executing the above command for write speed.

```sh
sudo sh -c "sync && echo 3 > /proc/sys/vm/drop_caches"
sudo dd if=/home/nvidia/test of=/dev/null bs=1M count=512
```

## mini PCIe

reComputer Industrial comes with a mini PCIe connector that supports 4G and LoRa modules. However, you can only connect either a 4G module or a LoRa module at once.

### 4G Module Connection Overview

Currently this board supports EC25EUXGA and EC20CEHCLG modules.

- **Step 1:** Power off the board if it is already on

- **Step 2:** Remove the included standoff. This standoff is only needed if you are using the M.2 Key B interface

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/110.jpg)

- **Step 3:** Slide in the 4G module to the mini PCIe slot, use the pre-installed screws and screw them to the 2 holes to secure the 4G module in place

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/17.png)

- **Step 4:** Connect an antenna to the the antenna connector labelled as **MAIN**. Here you need to use an IPEX connector

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/18.png)

- **Step 5:** Insert a 4G-enabled nano SIM card to the SIM card slot on the board making sure the gold surface of the SIM card is facing down. Here insert the card all the way in so that it will bounce back after hitting the internal spring and lock in place.

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/19.png)

> [!NOTE]
> If you want to remove the SIM card, push the card in to hit the internal spring so that the SIM will come out of the slot

- **Step 6:** Add a jumper between **SIM_MUX_SEL** and **GND** pins on the **J8 (Control and UART) Header**

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/20.png)

- **Step 6:** Power on the board

### 4G Module Usage - Test Dialing

When using the EC25 module, the module will automatically start and will be ready to use. However, when using the EC20 module, you need to reset the module for it to work

- **Step 1:** If you are using EC25 module, you can skip this step. However if you are using EC20 module, enter the following commands to access GPIO298 pin which is responsible to reset the 4G module

```sh
sudo su
cd /sys/class/gpio
echo 298 > export
cd gpio298
echo out > direction
echo 1 > value
```

For EC25 module, LED2 will light up in green as soon as the board is booted up. For EC20 module, LED2 will light up in green after resetting the module as explained above

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/118.jpg)

- **Step 2:** Install minicom

```sh
sudo apt update
sudo apt install minicom -y
```

- **Step 3:** Enter the serial console of the connected 4G module so that we can enter AT commands and interact with the 4G module

```sh
sudo minicom -D /dev/ttyUSB2 -b 115200
```

- **Step 4:** Press **Ctrl+A** and then press **E** to turn on local echo

- **Step 5:** Enter the command **"AT"** and press enter. If you see the response as "OK", the 4G module is working properly

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/22.jpg)

- **Step 6:** Enter the command **"ATI"** to check the module information

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/23.png)

- **Step 7:** To test the module, enter the below command to call another phone number

```sh
ATD<phone_number>;
```

And you will see the below output

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/24.jpg)

If the entered phone number can receive the call, the module is working as expected

### 4G Module Usage - Connect to Internet

#### EC25 module

If you are using the EC25 module, follow the below steps

- **Step 1:** After opening the serial console of the 4G module as explained above (4G Module Usage - Test Dialing section), execute the following command to connect to the internet. Here replace **YOUR_APN** with the APN of your network provider

```sh
AT+CGDCONT=1,"IP","YOUR_APN"
```

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/89.jpg)

On successful connection, it should output **OK** as you can see from the image above

- **Step 2:** Restart the 4G module by executing the following

```sh
AT+CFUN=1,1
```

Now you will lose connection to the 4G module on the serial terminal

- **Step 3:** Close **minicom** by pressing **CTRL + A** and then **Q**

- **Step 4:** Type **ifconfig** and you will see an IP address on the **usb0** interface

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/93.png)

- **Step 5:** You can try to ping a website as follows to check whether there is internet connectivity

```sh
ping -I usb0 www.bing.com -c 5
```

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/94.png)

#### EC20 module

If you are using the EC20 module, follow the below steps

- **Step 1:** If you have already reset the 4G module as explained in the previous section (4G Module Usage - Test Dialing section) for EC20 module, you can skip this step. However, if you have not yet done it, please do it now

- **Step 2:** Enter the serial console of the 4G module and enter the following command to set to ECM mode

```sh
AT+QCFG="usbnet",1
```

- **Step 3:** Reset the 4G module

- **Step 4:** Inside the 4G module console, execute the following command to connect to the internet. Here replace **YOUR_APN** with the APN of your network provider

```sh
AT+CGDCONT=1,"IP","YOUR_APN"
```

- **Step 6:** Type **ifconfig** and you will see an IP address on the **usb1** interface

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/90.jpg)

- **Step 7:** You can try to ping a URL as follows to check whether there is internet connectivity

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/92.png)

### LoRa Module Connection Overview

Currently this board supports WM1302 SPI module. You can either use [US version](https://www.seeedstudio.com/WM1302-LoRaWAN-Gateway-Module-SPI-US915-SKY66420-p-5455.html) or [EU version](https://www.seeedstudio.com/WM1302-LoRaWAN-Gateway-Module-SPI-EU868-p-4889.html) which is available on our Bazaar.

- **Step 1:** Power off the board if is already on

- **Step 2:** Slide in the LoRa module to the mini PCIe slot and use the pre-installed screws and screw them to the 2 holes to secure the 4G module in place

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/25.png)

- **Step 3:** Connect an antenna to the the antenna connector. Here you need to use an IPEX connector

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/26.png)

> [!NOTE]
> Make sure there is no jumper between **SIM_MUX_SEL** and **GND** pins on the **J8 (Control and UART) Header**. This jumper is only needed when using 4G modules

- **Step 4:** Power on the board

### LoRa Module Usage - Testing LoRa RF

When the LoRa module is connected, you will see the green and blue LEDs on the module light up

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/27.png)

- **Step 1:** Enter the below command to check whether the LoRa module is detected by the system

```sh
i2cdetect -r -y 7
```

If you see the below output, the module is detected by the system

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/29.png)

- **Step 2:** Enter the below commands to compile and build the LoRa signals transmitting tool

```sh
git clone https://github.com/lakshanthad/sx1302_hal
cd sx1302_hal
make
cd libloragw
cp ../tools/reset_lgw.sh .
sudo ./test_loragw_hal_tx -r 1250 -m LORA -f 867.1 -s 12 -b 125 -n 1000 -z 100 --dig 3 --pa 0 --pwid 13 -d /dev/spidev2.0
```

If you see the below result and the LED on the LoRa module turns RED, that means the module is trasmitting RF signals successfully

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/78.jpg)

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/28.png)

To stop transmitting, you can press **CTRL + C** on the keyboard.

### LoRa Module Usage - Connect to TTN

Now we will connect to TTN (The Things Network) and use the reComputer Industrial as a TTN LoRaWAN gateway

- **Step 1:** Enter the below to make the packet forwarder ready

```sh
cd ..
cd packet_forwarder
cp ../tools/reset_lgw.sh .
```

- **Step 2:** Run the following according to the LoRa module you are using. Here we have tested SPI US915 version

```sh
sudo ./lora_pkt_fwd -c global_conf.json.sx1250.US915
```

However, the commands for different other modules are as follows

```sh
# USB 915
sudo ./lora_pkt_fwd -c global_conf.json.sx1250.US915.USB

# SPI EU868
sudo ./lora_pkt_fwd -c global_conf.json.sx1250.EU868

# USB EU868
sudo ./lora_pkt_fwd -c global_conf.json.sx1250.EU868.USB
```

After running the above command, you will see the below output with last line showing the **concentrator EUI** information. Please keep this information because we will use it later when setting up the gateway with TTN

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/79.jpg)

- **Step 3:** Visit [this URL](https://console.cloud.thethings.network) to enter the TTN console and select a region of your choice

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/80.png)

- **Step 4:** Login if you already have an account, or sign up for a new account if you do not have one

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/81.png)

- **Step 5:** Click **Go to gateways**

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/82.png)

- **Step 6:** Click **+ Register gateway**

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/83.png)

- **Step 7:** Enter the **Concentrator EUI** that you obtained before inside the **Gateway EUI** section and click **Confirm**

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/84.jpg)

- **Step 8:** Enter the **Frequency plan** according to the LoRa module you are using. Here we are using US915 verison of the module and therefore have selected **United Stated 902-928 MHz, FSB 2 (used by TTN)**. After that click **Register gateway**

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/85.jpg)

> [!NOTE]
> The **Gateway ID** has been filled automatically for you. However, you can change it to anything you prefer. **Gateway name** is not a must to fill. However, you can fill it as well according to your preference

- **Step 9:** Make note of the **Gateway Server Address** on the main homepage of the gateway

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/86.jpg)

- **Step 9:** On the reTerminal Industrial, edit the **global_conf_json** file that we used along with the **lora_pkt_fwd** command. Here you need to change the **gateway_ID**, **server_address**, **serv_port_up** and **serv_port_down** options as follows

  - gateway_ID: Concentrator EUI from device
  - server_address: Gateway Server Address from TTN
  - serv_port_up: 1700
  - serv_port_down: 1700

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/87.png)

- **Step 10:** Rerun the packet forwarder

```sh
sudo ./lora_pkt_fwd -c global_conf.json.sx1250.US915
```

If you see the below output, that means the device has successfully connected with TTN

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/88.jpg)

## M.2 Key B

reComputer Industrial comes with a M.2 Key B connector that supports 4G and 5G modules. Currently we have tested **SIM8202G-M2 5G module**

### 5G Module Connection Overview

- **Step 1:** Power off the board if it is already on

- **Step 2:** Make sure the standoff is in place and then remove the top screw on the standoff

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/111.jpg)

- **Step 2:** Slide in the 5G module to the M.2 Key B slot and screw in the standoff screw to secure the 5G module in place (talk about standoff)

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/112.jpg)

- **Step 3:** Connect 4 antennas to the the antenna connectors on the module. Here you need to use an IPEX 4 connector

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/113.jpg)

- **Step 4:** Insert a 5G-enabled nano SIM card to the SIM card slot on the board making sure the gold surface of the SIM card is facing down. Here insert the card all the way in so that it will bounce back after hitting the internal spring and lock in place.

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/19.png)

> [!NOTE]
> If you want to remove the SIM card, push the card in to hit the internal spring so that the SIM will come out of the slot

- **Step 5:** Power on the board

### 5G Module Usage - Test Dialing

When using the SIM8202G-M2 5G module, the module will not automatically start. So we first need to toggle a few GPIOs to make it start

- **Step 1:** Enter the following to start the 5G module

```sh
sudo su
cd /sys/class/gpio
echo 298 > export
cd gpio298
echo out > direction
echo 0 > value

cd..
echo 330 > export
cd PEE.02
echo out > direction
echo 1 > value

cd..
echo 319 > export
cd PCC.02
echo out > direction
echo 0 > value
```

Once the above is executed, LED2 will light up in green as below

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/117.jpg)

- **Step 2:** Install minicom

```sh
sudo apt update
sudo apt install minicom -y
```

- **Step 3:** Enter the serial console of the connected 5G module so that we can enter AT commands and interact with the 5G module

```sh
sudo minicom -D /dev/ttyUSB2 -b 115200
```

- **Step 4:** Enter the command **"AT"** and press enter. If you see the response as "OK", the 5G module is working properly

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/107.png)

- **Step 6:** Enter the command **"ATI"** to check the module information

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/108.png)

- **Step 7:** To test the module, enter the below command to call another phone number

```sh
ATD<phone_number>;
```

And you will see the below output

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/109.png)

### 5G Module Usage - Connect to Internet

Coming soon

## DI/ DO

reComputer Industrial supports 4 digital input and 4 digital output channels, all of which are optically isolated to effectively protect the mainboard from voltage spikes or other electrical disturbances. There is also a CAN interface on this same connector which we will discuss later in this wiki

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/37.png)

### DI/ DO Pin Assignment Table



      Type
      Label Name
      Schematic Signal
      Module Pin Number
      BGA Number
      GPIO Number
      V/A Limits
      Note




      Input
      DI1
      DI_1_GPIO01
      118
      PQ.05
      440
      12V/ 20mA current in total
      12V Digital Input, ground signal needs to<br>be connected to GND_DI (Pin2/4/6)


      DI2
      DI_2_GPIO09
      211
      PS.04
      453


      DI3
      DI_3_GPIO11
      216
      PQ.06
      441


      DI4
      DI_4_GPIO13
      228
      PN.01
      419


      Output
      DO1
      DO_1_GPIO
      193
      PT.06
      463
      40V/40mA load per pin
      Digital output, maximum withstand<br>voltage 40V, ground signal needs to be<br>connected to GND_DO(Pin8/10)


      DO2
      DO_2_GPIO
      195
      PT.07
      464


      DO3
      DO_3_GPIO
      197
      PU.00
      465


      DO4
      DO_4_GPIO
      199
      PT.05
      462


      CAN
      CH
      /
      CAN bus with standard differential signals, <br>ground signal needs to be connected to GND_ISO (Pin 12)


      CL


      Ground
      GND_DI
      /
      The reference ground signal for the 12V Digital<br>Input, which is also the return path for the DI


      GND_DO
      The reference ground signal of the digital output, which is also the return path of the DO


      CG
      The reference ground signal for CAN



### Connection Overview for DI

You can make the connection for DI by following the diagram below. It is better to add a resistor in series for the DI line. Here we have tested with a 4.7kΩ resistor connected to the DI1 pin.

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/38.png)

### Usage for DI

You need to input a voltage of 12V on the DI line in order to get detected as an input

- **Step 1:** Make the connetions as shown above to **DI1 pin** and input **12V**

- **Step 2:** Open the GPIO for DI1 as follows

```sh
sudo su
cd /sys/class/gpio
echo 440 > export
cd PQ.05
```

> [!NOTE]
> You can refer the **DI/ DO Pin Assignment Table** to find the GPIO number and BGA number. In the above example, for DI1 pin, GPIO number is 440 and BGA number is PQ.05

- **Step 3:** Execute the following to check the status

```sh
cat value
```

If it outputs 0, that means there is 12V input. If it outputs 1, that means there is no input voltage.

### Connection Overview for DO

You can make the connection for DO by following the diagram below. It is better to add a resistor in series for the DO line. Here we have tested with a 4.7kΩ resistor

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/39.png)

### Usage for DO

Here you need to connect a load as mentioned in the above diagram. The easiest way to test this would be to connect a multimeter if you have access to one, or else connect a load that requires less than 40V maximum voltage

- **Step 1:** Make the connetions as shown above to **DO1 pin** and input **40V as max**

- **Step 2:** Open the GPIO for D01 as follows

```sh
sudo su
cd /sys/class/gpio
echo 463 > export
cd PT.06
echo out > direction
```

> [!NOTE]
> You can refer the **DI/ DO Pin Assignment Table** to find the GPIO number and BGA number. In the above example, for DO1 pin, GPIO number is 463 and BGA number is PT.06

- **Step 3:** Execute the following to turn on the pin

```sh
echo 1 > value
```

If the load is turned on or the multimeter outputs the voltage that you have input, the test it is functioning properly.

## CAN

reComputer Industrial features a CAN interface that supports the CAN FD (Controller Area Network Flexible Data-Rate) protocol at 5Mbps. The CAN interface is isolated using capacitive isolation, which provides excellent EMI protection and ensures reliable communication in industrial and automation applications. A terminal resistor of 120Ω has been installed by default and you can toggle this resistor ON and OFF using GPIO.

Note: The CAN interface uses an isolated power supply, which means that the ground signal for external devices connected to the CAN interface should be connected to the CG pin

### Connection Overview with USB to CAN Adapter

To test and interface with CAN bus, connect a USB to CAN adapter to the CAN connectors on the board as shown below

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/40.png)

Here we have used [USB to CAN Analyzer Adapter with USB Cable](https://www.seeedstudio.com/USB-CAN-Analyzer-p-2888.html) available on our Bazaar.

### Usage with USB to CAN Adapter

- **Step 1:** Download the driver for the USB to CAN adapter you are using from the manufacturer's website and install it. In our case, according to the adapter that we used, the drivers can be found [here](https://github.com/SeeedDocument/USB-CAN-Analyzer/tree/master/res/Driver/driver%20for%20USBCAN(CHS40)/windows-driver)

- **Step 2:** Some adapters also come with the necessary software for the PC in order to communicate with the CAN device. In our case, according to the adapter that we used, we have downloaded and installed the software which can be found [here](https://github.com/SeeedDocument/USB-CAN-Analyzer/tree/master/res/Program)

- **Step 3:** Open a terminal window on the reComputer Industrial and execute the following commands to configure and enable the CAN interface

```sh
sudo modprobe mttcan
sudo ip link set can0 type can bitrate 125000
sudo ip link set can0 up
```

- **Step 4:** Type **ifconfig** on the terminal and you will see the CAN interface in enabled

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/41.png)

- **Step 5:** Open the CAN software that you have installed before. In this case, we will open the software that we installed according to the CAN adapter that we are using

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/42.jpg)

- **Step 6:** Connect the USB to CAN adapter to the PC and open **Device Manager** by searching it on windows search bar. Now you will see the connected adapter under **Ports (COM & LPT)**. Make a note of the serial port listed here. According to the below image, the serial port is **COM9**

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/43.png)

- **Step 7:** Open the CAN software, click **Refresh** next to **COM** section, click the drop-down-menu and select the serial port according to the connected adapter. Keep the **COM bps** at default and click **Open**

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/44.jpg)

- **Step 8:** Keep the **Mode** and **CAN bps** at default, change the **Type** to **Standard frame** and click **Set and Start**

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/45.png)

- **Step 9:** On reComputer Industrial, execute the following command to send a CAN signal to the PC

```sh
cansend can0 123#abcdabcd
```

Now you will see the above signal received by the software as shown below

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/46.png)

- **Step 10:** On reComputer Industrial, execute the following command to wait for receiving CAN signals from the PC

```sh
candump can0 &
```

- **Step 11:** On the CAN software, click **Send a single frame**

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/47.png)

Now you will see it received by reComputer Industrial as follows

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/50.png)

### Connection Overview with reTerminal DM

If you have access to a [reTerminal DM](https://www.seeedstudio.com/reTerminal-DM-p-5616.html), you can communicate with it directly because reTerminal DM also has a CAN interface.

Refer to the below image to connect reComputer Industrial and reTerminal DM via CAN

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/49.png)

### Usage with reTerminal DM

- **Step 1:** Before using reTerminal DM, visit [this wiki](https://wiki.seeedstudio.com/reterminal-dm) to get started with reTerminal DM

- **Step 2:** Open a terminal window on the reComputer Industrial and execute the following commands to configure and enable the CAN interface

```sh
sudo modprobe mttcan
sudo ip link set can0 type can bitrate 125000
sudo ip link set can0 up
```

- **Step 3:** Open a terminal window on the reTerminal DM and execute the following commands to configure and enable the CAN interface

```sh
sudo modprobe mttcan
sudo ip link set can0 type can bitrate 125000
sudo ip link set can0 up
```

- **Step 4:** Open a terminal window on the reTerminal DM and execute the following commands to configure and enable the CAN interface

```sh
sudo modprobe mttcan
sudo ip link set can0 type can bitrate 125000
sudo ip link set can0 up
```

- **Step 5:** If you type **ifconfig** on both devices, you will see the CAN interfaces are enabled

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/41.png)

- **Step 6:** On the reTerminal DM, execute the following to wait for receiving CAN signals from the reComputer Industrial

```sh
candump can0 &
```

- **Step 7:** On the reComputer Industrial, execute the following command to send a CAN signal to the reTerminal Industrial

```sh
cansend can0 123#abcdabcd
```

Now you will see it received by reTerminal DM as follows

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/50.png)

- **Step 8:** Repeat **step 6 and step 7** but interchanging the devices. Use reTerminal DM to send CAN signals and use reComputer Industrial to receive them

## RS232/ RS422/ RS485 interfaces

reComputer Industrial has a DB9 connector which supports RS232, RS422 and RS485 communication protocols and there is a DIP switch panel onboard to switch between the different interface options

You can see the DIP switch panel as below:

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/51.png)

> [!NOTE]
> Make sure to remove the yellow plastic cover before using the DIP switch panel

And the below table explains the different modes based on the DIP switch positions




      MODE_0
      MODE_1
      MODE_2
      Mode
      Status




      ![Image](https://files.seeedstudio.com/wiki/reComputer-Industrial/52.png)
      0
      0
      0
      RS-422 Full Duplex
      1T/1R RS-422


      ![Image](https://files.seeedstudio.com/wiki/reComputer-Industrial/53.png)
      0
      0
      1
      Pure RS-232
      3T/5R RS-232


      ![Image](https://files.seeedstudio.com/wiki/reComputer-Industrial/54.png)
      0
      1
      0
      RS-485 Half Duplex
      1T/1R RS-485 ,TX ENABLE Low Active


      ![Image](https://files.seeedstudio.com/wiki/reComputer-Industrial/55.png)
      0
      1
      1
      RS-485 Half Duplex
      1T/1R RS-485 ,TX ENABLE High Active


      ![Image](https://files.seeedstudio.com/wiki/reComputer-Industrial/56.png)
      1
      0
      0
      RS-422 Full Duplex
      1T/1R RS-422 with termination resistor


      ![Image](https://files.seeedstudio.com/wiki/reComputer-Industrial/57.png)
      1
      0
      1
      Pure RS-232
      1T/1R RS-232 co-exists with RS485


      application without the need for the bus


      switch IC (for special usage).


      ![Image](https://files.seeedstudio.com/wiki/reComputer-Industrial/58.png)
      1
      1
      0
      RS-485 Half Duplex
      1T/1R RS-485 with termination resistor


      TX ENABLE Low Active


      ![Image](https://files.seeedstudio.com/wiki/reComputer-Industrial/59.png)
      1
      1
      1
      Low Power
      All I/O pins are High Impedance


      Shutdown



> [!NOTE]
> Out of the box, the default mode of the switches will be set to RS485 with 010 from factory

The above table takes into account the first three switches of the DIP switch panel. However, the fourth switch is responsible to toggle the slew rate which is directly related to the data rate




      Status
      Note




      ![Image](https://files.seeedstudio.com/wiki/reComputer-Industrial/62.png)
      1
      SLEW= Vcc<br>This RS232/RS422/RS485 Multiprotocol Transceiver limits the communication rateas follows :<br>RS-232: MaximumData Rate is 1.5Mbps<br>RS-485/RS-422; MaximumData Rate is 10Mbps<br>The actual Maximum Data Rate depends on the Jetson SO Mused


      ![Image](https://files.seeedstudio.com/wiki/reComputer-Industrial/63.png)
      0
      SLEW = GND<br>RS-232: Maximum Data Rate is 250Kbps<br>RS-485/RS-422: Maximum Data Rate is 250kbps



Here we will be using USB to RS232, RS485 and RS422 adapters in order to test the interfaces. So before moving on, you need to install a serial terminal application on your PC. Here we recommend you to install **Putty** which is easy to setup and use.

- **Step 1:** Visit [this website](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) and download Putty according to your PC architecture

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/60.png)

Here we have selected Putty according to the PC that we used which is a X86 windows 64-bit machine

- **Step 2:** Open the downloaded setup and go through the prompts to install the application

### General Connection Overview

You can refer to the pin numbering of DB9 connector and the table to make the connections

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/61.png)



      MODE
      001/101
      000/100
      010/011/110




      PIN
      RS232
      RS422
      RS485


      1

      TXD-
      Data-


      2
      RXD
      TXD+
      Data+


      3
      TXD
      RXD+



      4

      RXD-



      5
      GND
      GND
      GND


      6





      7
      RTS




      8
      CTS




      9






### RS232 Connection Overview

Here you can use a USB to RS232 adapter to test the interface. We have used [UGREEN USB to RS232 Adapter](https://www.amazon.com/UGREEN-Converter-Adapter-Chipset-Windows/dp/B00QUZY4UG?th=1) for our testing.

- **Step 1:** Turn off the board

- **Step 2:** Here we have 2 options to set the DIP switches. Either in 001 mode or 101 mode. The switch positions for each mode is shown below

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/64.png)

- **Step 3:** Connect the USB to RS232 adapter to the DB9 connector. Here we have connected the adapter that we have mentioned above

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/68.jpg)

- **Step 4:** Connect the other end to one of the USB ports on your PC

- **Step 5:** Turn on the board

### RS232 Usage

- **Step 1:** You may need to install a driver for the adapter that you are using or windows will automatically install the driver for you. Go to Device Manager by typing **Device Manager** inside windows search and check whether you can see the conenected adapter as a COM device.

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/67.jpg)

- **Step 2:** If you cannot see the adapter, you need to install the driver according to the adapter that you are using. You can generally find these drivers on the manufacturer website. For the adapter that we are using, you can [this page](https://www.ugreen.com/pages/download), search for **20201** as the model number and download the driver accordingly

- **Step 3:** Open Putty on the PC, select the **Terminal** section set the following

  - Local echo: Force on
  - Local line editing: Force on

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/69.png)

- **Step 4:** Select **Session**, under **Coonection type**, select **Serial**, set the serial port number according to what you see on **Device Manager**, keep the Speed as default (9600) and click **Open**

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/71.jpg)

- **Step 4:** On the reTerminal Industrial terminal window, type the following to send a signal from the reComputer to the PC

```sh
sudo chmod 777 /dev/ttyTHS0
sudo echo "RS232 message from reComputer Industrial" > /dev/ttyTHS0
```

Now you will see this message displayed on Putty

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/72.jpg)

- **Step 5:** On the reTerminal Industrial terminal window, type the following to wait for receiving signals from the PC

```sh
sudo cat /dev/ttyTHS0
```

- **Step 6:** On Putty, type anything, press **ENTER** and it will be displayed on the reComputer Industrial terminal window

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/73.png)

### RS422 Connection Overview

Here you can use a USB to RS422 adapter to test the interface. We have used [DTech USB to RS485 Adapter](https://www.amazon.com/Adapter-Serial-Terminal-Ferrite-Windows/dp/B08SM5MX8K) for our testing.

- **Step 1:** Turn off the board

- **Step 2:** Here we have 2 options to set the DIP switches. Either in 000 mode or 100 mode. The switch positions for each mode is shown below

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/65.png)

- **Step 3:** Connect the USB to RS422 adapter to the DB9 connector using Jumper wires as shown below. Here we have connected the adapter that we have mentioned above

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/74.png)

- **Step 4:** Connect the other end to one of the USB ports on your PC

- **Step 5:** Turn on the board

### RS422 Usage

- **Step 1:** You may need to install a driver for the adapter that you are using or windows will automatically install the driver for you. Go to Device Manager by typing **Device Manager** inside windows search and check whether you can see the connected adapter as a COM device.

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/75.png)

- **Step 2:** If you cannot see the adapter, you need to install the driver according to the adapter that you are using. You can generally find these drivers on the manufacturer website. For the adapter that we are using, you can [this page](https://www.dtechelectronics.com/front/downloads/downloadssearch/user_downloadscat_id/0/search_value/rs485)

- **Step 3:** Open Putty on the PC, select the **Terminal** section set the following

  - Local echo: Force on
  - Local line editing: Force on

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/69.png)

- **Step 4:** Select **Session**, under **Coonection type**, select **Serial**, set the serial port number according to what you see on **Device Manager**, keep the Speed as default (9600) and click **Open**

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/76.png)

- **Step 4:** On the reTerminal Industrial terminal window, type the following to send a signal from the reComputer to the PC

```sh
sudo chmod 777 /dev/ttyTHS0
sudo echo "RS422 message from reComputer Industrial" > /dev/ttyTHS0
```

Now you will see this message displayed on Putty

- **Step 5:** On the reTerminal Industrial terminal window, type the following to wait for receiving signals from the PC

```sh
sudo cat /dev/ttyTHS0
```

- **Step 6:** On Putty, type anything, press **ENTER** and it will be displayed on the reComputer Industrial terminal window

### RS485 Connection Overview

Here you can use a USB to RS422 adapter to test the interface. We have used [DTech USB to RS485 Adapter](https://www.amazon.com/Adapter-Serial-Terminal-Ferrite-Windows/dp/B08SM5MX8K) for our testing.

- **Step 1:** Turn off the board

- **Step 2:** Here we have 3 options to set the DIP switches. Either in 010 mode or 011 mode or 110 mode. The switch positions for each mode is shown below

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/66.png)

- **Step 3:** Connect the USB to RS422 adapter to the DB9 connector using Jumper wires as shown below. Here we have connected the adapter that we have mentioned above

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/77.png)

- **Step 4:** Connect the other end to one of the USB ports on your PC

- **Step 5:** Turn on the board

### RS485 Usage

- **Step 1:** You may need to install a driver for the adapter that you are using or windows will automatically install the driver for you. Go to Device Manager by typing **Device Manager** inside windows search and check whether you can see the conenected adapter as a COM device.

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/75.png)

- **Step 2:** If you cannot see the adapter, you need to install the driver according to the adapter that you are using. You can generally find these drivers on the manufacturer website. For the adapter that we are using, you can [this page](https://www.dtechelectronics.com/front/downloads/downloadssearch/user_downloadscat_id/0/search_value/rs485)

- **Step 3:** Open Putty on the PC, select the **Terminal** section set the following

  - Local echo: Force on
  - Local line editing: Force on

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/69.png)

- **Step 4:** Select **Session**, under **Coonection type**, select **Serial**, set the serial port number according to what you see on **Device Manager**, keep the Speed as default (9600) and click **Open**

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/76.png)

- **Step 4:** On the reTerminal Industrial terminal window, type the following to send a signal from the reComputer to the PC

```sh
sudo su
cd /sys/class/gpio
echo 447 > export
cd PR.04
echo out > direction
echo 0 > value
echo "RS485 message from reComputer Industrial" > /dev/ttyTHS0
```

Now you will see this message displayed on Putty

- **Step 5:** On the reTerminal Industrial terminal window, type the following to wait for receiving signals from the PC

```sh
sudo su
cd /sys/class/gpio
echo 447 > export
cd PR.04
echo out > direction
echo 1 > value
cat /dev/ttyTHS0
```

- **Step 6:** On Putty, type anything, press **ENTER** and it will be displayed on the reComputer Industrial terminal window

## Gigabit Ethernet Connectors

There are two Gigabit Ethernet (10/100/1000M) Connectors on the reComputer Industrial and they function in different ways

- The leftmost connector is directy connected to the Jetson module and is able to provide PoE functionality with **PSE 802.3 af, 15W** specification. This means you can connect a PoE IP camera or any other PoE device to this port to provide power to the connected device.
- The other connector is connected via a PCIe to Ethernet (LAN7430-I/Y9X) module

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/36.png)

There are 2 LEDs (green and yellow) on each Ethernet port which indicates the following

- Green LED: ON only when connected to 1000M network
- Yellow LED: Shows the network activity status

## USB

reComputer Industrial comes with 3x USB3.2 connectors onboard and has the following features:

- On the dual stacked USB connectors, the upper and lower USB ports share a current-limiting IC, with a total power supply capacity of 2.1A maximum output current (single can also be 2.1A). If over 2.1A, it will enter the over-current protection state.
- On the single USB connector next to the dual stacked USB connectors, it has a total power supply capacity of 2.1A maximum output current. If over 2.1A, it will enter the over-current protection state.
- Orin NX module comes with 3 USB3.2, only one of which is used in reComputer and converted to 3 ways. (USB3.1 TYPE-A x2 - J4 and USB3.1 TYPE-Ax1 -J3).
- Only supports USB Host, not Device mode
- Provide 5V 2.1A
- Hot-swappable

### Usage

We will explain how to do a simple benchmark on a connected USB flash drive

- **Step 1:** Check the write speed by executing the below command

```sh
sudo dd if=/dev/zero of=/dev/$1 bs=100M count=10 conv=fdatasync
```

- **Step 2:** Check the read speed by executing the below commands. Make sure to execute this after executing the above command for write speed.

```sh
sudo sh -c "sync && echo 3 > /proc/sys/vm/drop_caches"
sudo dd if=/dev/$1 of=/dev/null bs=100M count=10
```

## Configurable LED

There is a Green color LED located on the board as shown below. By default it is acting as the LED which shows the device is running properly. However, you can program this LED to turn ON and OFF by the system as well

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/21.png)

### Usage

- **Step 1:** Enter the following commands on a terminal window to access the Green color LED

```sh
sudo -i
cd /sys/class/gpio
echo 318 > export
cd PCC.01
echo out > direction
```

- **Step 2:** Turn OFF the LED

```sh
echo 0 > value
```

- **Step 3:** Turn ON the LED

```sh
echo 1 > value
```

If you have finished using the LED, you can execute the following

```sh
cd ..
echo 318 > unexport
```

## Monitor System Performance

We can use **jetson stats** application to monitor the temperatures of the system components and check other system details such as

- View CPU, GPU, RAM utilizations
- Change power modes
- Set to max clocks
- Check JetPack information

- **Step 1:** On the reComputer Industrial terminal windows, type the following

```sh
sudo apt update
sudo apt install python3-pip -y
sudo pip3 install jetson-stats
```

- **Step 2:** Reboot the board

```sh
sudo reboot
```

- **Step 3:** Type the following on the terminal

```sh
jtop
```

Now **jtop** application will open as follows

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/30.png)

- **Step 4:** Here you can cycle through the different pages of the applications and explore all the features!

## WiFi and Bluetooth

reComputer Industrial does not come with WiFi and Bluetooth out-of-the-box. But there is a reserved section on the PCB so that a WiFi/ Bluetooth module can be soldered to the board. Here we have reserved the space to support a **BL-M8723DU1** module.

### Connection Overview

- **Step 1:** If you want to solder the **BL-M8723DU1** module by yourself, you can solder it. But we do not recommend this because if you damage the board in the process, the warranty will be void. What we recommend is to use our professional service to help you solder this module onto the board and you can send an email to order@seeed.cc with your request.

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/31.jpg)

- **Step 2:** Connect two antennas to the two antenna connectors on the board for WiFi and Bluetooth. Here you need to use an IPEX connector

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/32.png)

### Usage

- **Step 1:** Turn on the board and once the device boots into Ubuntu Desktop, click on the drop-down menu at the top right corner, navigate to `Settings > Wi-Fi` and toggle the button on the title bar to enable WiFi. After that select a WiFi network, enter the required password and connect to it

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/33.png)

- **Step 2:** On the same window, choose **Bluetooth** and toggle the button on the title bar to enable Bluetooth. After that select a Bluetooth device to connect to it

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/34.png)

## TPM

reComputer Industrial comes with a TPM interface to connect an external TPM module. Here we have tested with a Infineon SLB9670 based TPM2.0 Module.

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/114.jpg)

### Connection Overview

Connect the TPM module to the TPM connector as shown below

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/115.jpg)

### Usage

Check whether the TPM module is loaded properly by executing the below commands

```sh
sudo dmesg | grep TPM
ls /dev/tpm* -l
```

And you will see the output as follows

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/116.png)

## Max Performance on reComputer Industrial

If you want to enable maximum performance on the reComputer Industrial, please follow the below instructions

- **Step 1:** Enter the below command to enable the maximum power mode

```sh
sudo nvpmodel -m 0
```

![image](https://files.seeedstudio.com/wiki/reComputer-Industrial/35.jpg)

Here it will ask to type **YES** in order to reboot the board

- **Step 2:** Once the board is booted, enter the following command to set the CPU clocks to the maximum frequency

```sh
sudo jetson_clocks
```

## GPIO Table

You can access the GPIO table of the reComputer Industrial to get familiar with all the pin mappings.

Execute the following inside a terminal to access it

```sh
sudo cat /sys/kernel/debug/gpio
```

And you will see the output as follows

```sh
gpiochip3: GPIOs 289-304, parent: i2c/1-0021, 1-0021, can sleep:
 gpio-289 (wl_dis              |gpio_xten_pin@0     ) out hi
 gpio-290 (hst_wake_wl         |gpio_xten_pin@1     ) out hi
 gpio-291 (wl_wake_hst         |gpio_xten_pin@2     ) out hi ACTIVE LOW
 gpio-292 (bt_dis              |gpio_xten_pin@3     ) out hi
 gpio-293 (hst_wake_bt         |gpio_xten_pin@4     ) out hi
 gpio-294 (bt_wake_hst         |gpio_xten_pin@5     ) out hi ACTIVE LOW
 gpio-295 (spi0_rst_3v3        |gpio_xten_pin@6     ) out lo ACTIVE LOW
 gpio-296 (gpio_pin7           |gpio_xten_pin@7     ) out lo ACTIVE LOW
 gpio-297 (can_120R_en         )
 gpio-298 (M2B_PCIe_rst        )
 gpio-299 (USB_HUB_rst         |gpio_xten_pin@10    ) out hi
 gpio-300 (PCIe_ETH_rst        )
 gpio-301 (M2B_WOWWAN          |gpio_xten_pin@12    ) out hi ACTIVE LOW
 gpio-302 (M2B_DPR_3V3         |gpio_xten_pin@13    ) out hi ACTIVE LOW
 gpio-303 (SIM_MUX_SEL         |gpio_xten_pin@14    ) out hi ACTIVE LOW
 gpio-304 (gpio_pin15          |gpio_xten_pin@15    ) out hi ACTIVE LOW

gpiochip2: GPIOs 305-334, parent: platform/c2f0000.gpio, tegra194-gpio-aon:
 gpio-305 (PAA.00              )
 gpio-306 (PAA.01              )
 gpio-307 (PAA.02              )
 gpio-308 (PAA.03              )
 gpio-309 (PAA.04              )
 gpio-310 (PAA.05              )
 gpio-311 (PAA.06              )
 gpio-312 (PAA.07              )
 gpio-313 (PBB.00              )
 gpio-314 (PBB.01              )
 gpio-315 (PBB.02              )
 gpio-316 (PBB.03              )
 gpio-317 (PCC.00              )
 gpio-318 (PCC.01              |pwr                 ) out hi
 gpio-319 (PCC.02              )
 gpio-320 (PCC.03              |mux                 ) out hi
 gpio-321 (PCC.04              )
 gpio-322 (PCC.05              )
 gpio-323 (PCC.06              )
 gpio-324 (PCC.07              )
 gpio-325 (PDD.00              )
 gpio-326 (PDD.01              )
 gpio-327 (PDD.02              )
 gpio-328 (PEE.00              )
 gpio-329 (PEE.01              )
 gpio-330 (PEE.02              )
 gpio-331 (PEE.03              )
 gpio-332 (PEE.04              |power-key           ) in  hi IRQ ACTIVE LOW
 gpio-333 (PEE.05              )
 gpio-334 (PEE.06              )
gpiochip1: GPIOs 335-503, parent: platform/2200000.gpio, tegra194-gpio:
 gpio-335 (PA.00               )
 gpio-336 (PA.01               )
 gpio-337 (PA.02               )
 gpio-338 (PA.03               )
 gpio-339 (PA.04               )
 gpio-340 (PA.05               )
 gpio-341 (PA.06               )
 gpio-342 (PA.07               )
 gpio-343 (PB.00               )
 gpio-344 (PB.01               )
 gpio-345 (PC.00               )
 gpio-346 (PC.01               )
 gpio-347 (PC.02               )
 gpio-348 (PC.03               )
 gpio-349 (PC.04               )
 gpio-350 (PC.05               )
 gpio-351 (PC.06               )
 gpio-352 (PC.07               )
 gpio-353 (PD.00               )
 gpio-354 (PD.01               )
 gpio-355 (PD.02               )
 gpio-356 (PD.03               )
 gpio-357 (PE.00               )
 gpio-358 (PE.01               )
 gpio-359 (PE.02               )
 gpio-360 (PE.03               )
 gpio-361 (PE.04               )
 gpio-362 (PE.05               )
 gpio-363 (PE.06               )
 gpio-364 (PE.07               )
 gpio-365 (PF.00               )
 gpio-366 (PF.01               )
 gpio-367 (PF.02               )
 gpio-368 (PF.03               )
 gpio-369 (PF.04               )
 gpio-370 (PF.05               )
 gpio-371 (PG.00               |force-recovery      ) in  hi IRQ ACTIVE LOW
 gpio-372 (PG.01               )
 gpio-373 (PG.02               |fixed-regulators:reg) out lo
 gpio-374 (PG.03               |wifi-enable         ) out hi
 gpio-375 (PG.04               )
 gpio-376 (PG.05               )
 gpio-377 (PG.06               )
 gpio-378 (PG.07               )
 gpio-379 (PH.00               )
 gpio-380 (PH.01               )
 gpio-381 (PH.02               )
 gpio-382 (PH.03               )
 gpio-383 (PH.04               )
 gpio-384 (PH.05               )
 gpio-385 (PH.06               )
 gpio-386 (PH.07               )
 gpio-387 (PI.00               )
 gpio-388 (PI.01               )
 gpio-389 (PI.02               )
 gpio-390 (PI.03               )
 gpio-391 (PI.04               )
 gpio-392 (PJ.00               )
 gpio-393 (PJ.01               )
 gpio-394 (PJ.02               )
 gpio-395 (PJ.03               )
 gpio-396 (PJ.04               )
 gpio-397 (PJ.05               )
 gpio-398 (PK.00               )
 gpio-399 (PK.01               )
 gpio-400 (PK.02               )
 gpio-401 (PK.03               )
 gpio-402 (PK.04               )
 gpio-403 (PK.05               )
 gpio-404 (PK.06               )
 gpio-405 (PK.07               )
 gpio-406 (PL.00               )
 gpio-407 (PL.01               )
 gpio-408 (PL.02               )
 gpio-409 (PL.03               )
 gpio-410 (PM.00               )
 gpio-411 (PM.01               |hdmi2.0_hpd         ) in  lo IRQ
 gpio-412 (PM.02               )
 gpio-413 (PM.03               )
 gpio-414 (PM.04               )
 gpio-415 (PM.05               )
 gpio-416 (PM.06               )
 gpio-417 (PM.07               )
 gpio-418 (PN.00               |fixed-regulators:reg) out lo
 gpio-419 (PN.01               )
 gpio-420 (PN.02               )
 gpio-421 (PO.00               )
 gpio-422 (PO.01               )
 gpio-423 (PO.02               )
 gpio-424 (PO.03               )
 gpio-425 (PO.04               )
 gpio-426 (PO.05               )
 gpio-427 (PP.00               )
 gpio-428 (PP.01               )
 gpio-429 (PP.02               )
 gpio-430 (PP.03               )
 gpio-431 (PP.04               )
 gpio-432 (PP.05               )
 gpio-433 (PP.06               )
 gpio-434 (PP.07               )
 gpio-435 (PQ.00               )
 gpio-436 (PQ.01               )
 gpio-437 (PQ.02               )
 gpio-438 (PQ.03               )
 gpio-439 (PQ.04               )
 gpio-440 (PQ.05               )
 gpio-441 (PQ.06               )
 gpio-442 (PQ.07               )
 gpio-443 (PR.00               )
 gpio-444 (PR.01               |phy_reset           ) out hi
 gpio-445 (PR.02               )
 gpio-446 (PR.03               )
 gpio-447 (PR.04               )
 gpio-448 (PR.05               )
 gpio-449 (PS.00               )
 gpio-450 (PS.01               )
 gpio-451 (PS.02               )
 gpio-452 (PS.03               )
 gpio-453 (PS.04               )
 gpio-454 (PS.05               )
 gpio-455 (PS.06               )
 gpio-456 (PS.07               )
 gpio-457 (PT.00               )
 gpio-458 (PT.01               )
 gpio-459 (PT.02               )
 gpio-460 (PT.03               )
 gpio-461 (PT.04               )
 gpio-462 (PT.05               )
 gpio-463 (PT.06               )
 gpio-464 (PT.07               )
 gpio-465 (PU.00               )
 gpio-466 (PV.00               )
 gpio-467 (PV.01               )
 gpio-468 (PV.02               )
 gpio-469 (PV.03               )
 gpio-470 (PV.04               )
 gpio-471 (PV.05               )
 gpio-472 (PV.06               )
 gpio-473 (PV.07               )
 gpio-474 (PW.00               )
 gpio-475 (PW.01               )
 gpio-476 (PX.00               )
 gpio-477 (PX.01               )
 gpio-478 (PX.02               )
 gpio-479 (PX.03               )
 gpio-480 (PX.04               )
 gpio-481 (PX.05               )
 gpio-482 (PX.06               )
 gpio-483 (PX.07               )
 gpio-484 (PY.00               )
 gpio-485 (PY.01               )
 gpio-486 (PY.02               )
 gpio-487 (PY.03               )
 gpio-488 (PY.04               )
 gpio-489 (PY.05               )
 gpio-490 (PY.06               )
 gpio-491 (PY.07               )
 gpio-492 (PZ.00               )
 gpio-493 (PZ.01               |vbus                ) in  hi IRQ ACTIVE LOW
 gpio-494 (PZ.02               )
 gpio-495 (PZ.03               )
 gpio-496 (PZ.04               )
 gpio-497 (PZ.05               )
 gpio-498 (PZ.06               |cs_gpio             ) out lo
 gpio-499 (PZ.07               |cs_gpio             ) out hi
 gpio-500 (PFF.00              )
 gpio-501 (PFF.01              )
 gpio-502 (PGG.00              )
 gpio-503 (PGG.01              )

gpiochip0: GPIOs 504-511, parent: i2c/4-003c, max77620-gpio, can sleep:
 gpio-510 (                    |gpio_default        ) in  hi
 gpio-511 (                    |gpio_default        ) in  hi
```

## Tech Support

Please do not hesitate to submit issues into our [forum](https://forum.seeedstudio.com/).

  <br><a href="https://www.seeedstudio.com/act-4.html?utm_source=wiki&utm_medium=wikibanner&utm_campaign=newproducts" target="_blank">![image](https://files.seeedstudio.com/wiki/Wiki_Banner/new_product.jpg)</a>
