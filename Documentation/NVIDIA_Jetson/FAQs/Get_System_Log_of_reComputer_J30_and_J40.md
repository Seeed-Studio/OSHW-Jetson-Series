# How to get the system log of reComputer J30/J40?

This wiki will use the [reComputer J4012](https://www.seeedstudio.com/reComputer-J4012-p-5586.html) as an example to demonstrate how to retrieve the boot logs of a device via the Jetson serial port.

## Prerequisites

- reComputer J4012/ J4011/ J3010 or J3011
- [USB to Serial (TTL) Module](https://www.seeedstudio.com/CH340G-USB-to-Serial-TTL-Module-Adapter-p-2359.html)
- A computer with a serial port debugging tool installed

> [!NOTE]
> You can download and install a serial port debugging tool according to your personal preference. We recommend using [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html), [XShell](https://www.netsarang.com/en/xshell/) or [MobaXterm](https://mobaxterm.mobatek.net/).
>
> This tutorial uses MobaXterm.

## Hardware Connection

1. Connect the corresponding pins of the J15 interface to the USB2TTL module.
2. Connect the USB2TTL module to the computer with the serial port debugging tool installed.

  ![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/FAQ/hardware_connection.png)

  ![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/FAQ/pin.png)

## Get System Log

**Step1.** Obtain the identification number of the USB2TTL module recognized by the computer.

> [!NOTE]
> If your computer is running Windows, you can find the recognized identification number in the Device Manager.

  ![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/FAQ/com.png)

**Setp2.** Open the serial port debugging tool, configure the serial port number, and set the baud rate to `115200`.

  ![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/FAQ/config_serial.png)

**Setp3.** Power on the Jetson. If everything is working correctly, you should see the system boot logs in the serial port debugging tool window.

> Embedded media: <https://www.youtube.com/embed/rwiKgF91mNE>

## Tech Support & Product Discussion

Thank you for choosing our products! We are here to provide you with different support to ensure that your experience with our products is as smooth as possible. We offer several communication channels to cater to different preferences and needs.

<https://forum.seeedstudio.com/>
<https://www.seeedstudio.com/contacts>

<https://discord.gg/eWkprNDMU7>
<https://github.com/Seeed-Studio/wiki-documents/discussions/69>
