# J1010 Boot From SD Card

## Getting Started

We need to read these two articles before we start. Make sure the J1010 system is burned in correctly and that the sd card driver is installed properly.

- [J1010/J101 Flash Jetpack](https://wiki.seeedstudio.com/reComputer_J1010_J101_Flash_Jetpack/)
- [J101_Enable_SD_Card](https://wiki.seeedstudio.com/J101_Enable_SD_Card/)

## Flashing System from J101 to SD Card

First, we need to clone the script include the tools we need.

```bash
git clone https://github.com/limengdu/bootFromUSB
```

Second , We need to make sure the sd card is in ext4 format, which can be seen visually in the "disk" tool, if it is not ext4 we need to format it and change it to ext4 format.

Click blue are and then click on green area to select "Format Partiton"

![image](https://files.seeedstudio.com/wiki/Boot_NVIDIA_System_from_SD_card_for_Jetson101/disk_fix_1.jpg)

Click on green area to select "Internal disk for use with Linux systems only (Ext4)"
Fill the name want you wannt in "Volume Name" in the yellow area.

![image](https://files.seeedstudio.com/wiki/Boot_NVIDIA_System_from_SD_card_for_Jetson101/disk_fix_2.jpg)

So we can find the format of the sd card has been changed to ext4.

![image](https://files.seeedstudio.com/wiki/Boot_NVIDIA_System_from_SD_card_for_Jetson101/disk_view_1.png)

And then , go to the script directory , execute the following command like this

```bash
cd bootFromUSB
./copyRootToUSB.sh -p /dev/mmcblk1p1
```

Wait a while, only until it finishes automatically, if no error is reported, the burning is done

## Boot Configuration

Once the driver has been successfully installed and configured,we can simply view it via the command like "lsblk" or view device in "/dev".

### Change boot device

We are supposed to change the configuration in "/boot/extlinux/extlinux.conf".

- Boot from sd card

    After we boot from the emmc on the carrier board, we want to modify it to boot from the SD card. We need to make sure that the previous process, including the system burn to the sd card, and the sd card drivers are installed properly. Modify the parameters after root to the address of the device we are booting from. When we have completed our changes, reboot the system.

    **Before reboot Modify "/boot/extlinux/extlinux.conf" After reboot view "/media/seeed/\{xxx-xxx\}/boot/extlinux/extlinux.conf"**

    ![image](https://files.seeedstudio.com/wiki/Boot_NVIDIA_System_from_SD_card_for_Jetson101/config_3.png)

    :::note
    Our configuration file after booting the system from the sd card is "/media/seeed/\{xxx-xxx\}/boot/extlinux/extlinux.conf" and the configuration file after booting the system from the onboard emmc is in "/boot/extlinux/extlinux.conf" . They are the same files from which the device reads the configuration and chooses where to boot the system after power-up, and the relative paths change when the system has finished booting.
    :::

- Boot from board emmc

    We want to change back to booting from emmc after booting from an SD card or we need to change the SD card for some purpose. Then we need to change the device back to boot from emmc first. We should make the following changes.

    **Before reboot Modify "/media/seeed/\{xxx-xxx\}/boot/extlinux/extlinux.conf" After reboot view "/boot/extlinux/extlinux.conf"**

    ![image](https://files.seeedstudio.com/wiki/Boot_NVIDIA_System_from_SD_card_for_Jetson101/config_4.png)

Finally, we find it really works well.

- Boot from emmc

    ![image](https://files.seeedstudio.com/wiki/Boot_NVIDIA_System_from_SD_card_for_Jetson101/lsblk_emmc.png)

- Boot from sd card

    ![image](https://files.seeedstudio.com/wiki/Boot_NVIDIA_System_from_SD_card_for_Jetson101/lsblk_sd.png)

## Tech Support & Product Discussion

Thank you for choosing our products! We are here to provide you with different support to ensure that your experience with our products is as smooth as possible. We offer several communication channels to cater to different preferences and needs.

<https://forum.seeedstudio.com/>
<https://www.seeedstudio.com/contacts>

<https://discord.gg/eWkprNDMU7>
<https://github.com/Seeed-Studio/wiki-documents/discussions/69>
