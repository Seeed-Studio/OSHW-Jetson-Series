<!-- ---
name:
category:
bzurl:
prodimagename:
surveyurl:
sku:
tags:
--- -->

# Jetson Xavier AGX H01 Kit Driver Installation

![image](https://files.seeedstudio.com/wiki/recomputerzhongwen/first_1.png)

    [Get One Now 🖱️](https://www.seeedstudio.com/Jetson-Xavier-AGX-H01-Kit-p-5283.html)

This wiki will show you how to install driver to Jetson Xavier AGX H01 Kit. There are server ways to accomplish that.

## Install Jetson Xavier AGX H01 with Command Line

This is the installation through command lines, with stabilized steps.

### Materials Required

- Ubuntu Host PC
- Jetson Xavier AGX H01
- Type C data transmission cable

### Driver Installation

Before will install the driver, it is required to set the board into the Force Recovery Model.

#### Force Recovery Model

There is a recovery button on the board, which is in the middle of three buttons. Hold the recovery button and then power it up, which will enter the Force Recovery Model.

![image](https://files.seeedstudio.com/wiki/recomputerzhongwen/driver1.png)

Connect Jetson Xavier AGX H01 with the Ubuntu host PC with a Type-C data transmit cable.

![image](https://files.seeedstudio.com/wiki/recomputerzhongwen/driver.png)

#### Driver Required

We provide different versions of drivers for different versions of Jetpack system, for your convenience to install.



      JetPack Version
      Driver Required
      Jetson Linux Archive




      4.4
      <a href="../../../../../../reComputer%20Jetson%20carrier%20board/Jetson%20Xavier%20AGX%20H01/Firmware/H01_Driver_for_4.4.zip">Click to Download</a>
      <a href="https://developer.nvidia.com/embedded/linux-tegra-r32.4.3">NVIDIA L4T 32.4.3</a>


      4.6.1
      <a href="../../../../../../reComputer%20Jetson%20carrier%20board/Jetson%20Xavier%20AGX%20H01/Firmware/H01_Driver.zip">Click to Download</a>
      <a href="https://developer.nvidia.com/embedded/linux-tegra-r3271">NVIDIA L4T 32.7.1</a>


      5.0.1
      <a href="../../../../../../reComputer%20Jetson%20carrier%20board/Jetson%20Xavier%20AGX%20H01/Firmware/H01_Driver_for_5.0.1.zip">Click to Download</a>
      <a href="https://developer.nvidia.com/embedded/jetson-linux-r3411">NVIDIA L4T 34.1.1</a>


      5.0.2
      <a href="../../../../../../reComputer%20Jetson%20carrier%20board/Jetson%20Xavier%20AGX%20H01/Firmware/H01_Driver_for_5.0.2.zip">Click to Download</a>
      <a href="https://developer.nvidia.com/embedded/jetson-linux-r351">NVIDIA L4T 35.1</a>


      5.1
      <a href="../../../../../../reComputer%20Jetson%20carrier%20board/Jetson%20Xavier%20AGX%20H01/Firmware/H01_Driver_for_5.1.rar" target="_blank" rel="noopener noreferrer">Click to Download</a>
      <a href="https://developer.nvidia.com/embedded/jetson-linux-r3521" target="_blank" rel="noopener noreferrer">NVIDIA L4T 35.2.1</a>


      5.1.1
      <a href="../../../../../../reComputer%20Jetson%20carrier%20board/Jetson%20Xavier%20AGX%20H01/Firmware/H01_Driver_for_5.1.1.zip" target="_blank" rel="noopener noreferrer">Click to Download</a>
      <a href="https://developer.nvidia.com/embedded/jetson-linux-r3531" target="_blank" rel="noopener noreferrer">NVIDIA L4T 35.3.1</a>


      5.1.2
      <a href="../../../../../../reComputer%20Jetson%20carrier%20board/Jetson%20Xavier%20AGX%20H01/Firmware/H01_Driver_for_5.1.2.zip" target="_blank" rel="noopener noreferrer">Click to Download</a>
      <a href="https://developer.nvidia.com/embedded/jetson-linux-r3541" target="_blank" rel="noopener noreferrer">NVIDIA L4T 35.4.1</a>



#### Getting Started

The example here is using **NVIDIA L4T 32.7.1** to install **Jetpack 4.6.1** on the Jetson AGX H01.

- **Step 1**. [Download](https://developer.nvidia.com/embedded/linux-tegra-r3271) the drivers on the host PC form NVIDIA. The required 32.7.1 drivers are shown below:

![image](https://files.seeedstudio.com/wiki/H01Driver/h01driver4.png)

- **Step 2**. [Download](../../../reComputer%20Jetson%20carrier%20board/Jetson%20Xavier%20AGX%20H01/Firmware/H01_Driver.zip) additional required installation files **H01_Drivers** on the host PC.

Move downloaded files at **Step 1** into the same folder with **H01_Drivers**. Now you will see three unzipped files in the same folder.

![image](https://files.seeedstudio.com/wiki/H01Driver/h01drivera.png)

- **Step 3**. Unzip the file of **AGX_H01_Drivers.zip**.

![image](https://files.seeedstudio.com/wiki/H01Driver/h01driver1b.png)

- **Step 4**. Open terminal in the folder and unzip the rest files. Execute the command below:

```
tar xf Jetson_Linux_R32.7.1_aarch64.tbz2
cd Linux_for_tegra/rootfs
sudo tar xfp ../../Tegra_Linux_Sample-Root-Filesystem_R32.7.1_aarch64.tbz2
cd ..
sudo  ./apply_binaries.sh
```

![image](https://files.seeedstudio.com/wiki/H01Driver/h01driver5.png)

!!!Note
    If you donwnload files in somewhere else, make sure you add the path to the files. Like example here is "/Desktop/AGX/". If you directly open the terminal in the file, the path will be automatically added.

The command lines should be like:

![image](https://files.seeedstudio.com/wiki/recomputerzhongwen/agx0.png)

- **Step 5**. Move back and copy & paste the file from downloaded **H01_Driver** file to the unzipped file **Jetson_Linux_R32.6.1_aarch64.tbz2**.

![image](https://files.seeedstudio.com/wiki/H01Driver/h01driver6.png)

Here are the commands below:

```
cd ..
cp -a -f H01_Driver/Linux_for_Tegra/kernel Linux_for_Tegra/
cd Linux_for_Tegra/
sudo ./flash.sh jetson-xavier mmcblk0p1
```

The flash will be running and the progress is like:

![image](https://files.seeedstudio.com/wiki/recomputerzhongwen/agx2.png)

The final result shoule be like:

![image](https://files.seeedstudio.com/wiki/recomputerzhongwen/agx3.png)

## Tech Support & Product Discussion

Thank you for choosing our products! We are here to provide you with different support to ensure that your experience with our products is as smooth as possible. We offer several communication channels to cater to different preferences and needs.

<https://forum.seeedstudio.com/>
<https://www.seeedstudio.com/contacts>

<https://discord.gg/eWkprNDMU7>
<https://github.com/Seeed-Studio/wiki-documents/discussions/69>
