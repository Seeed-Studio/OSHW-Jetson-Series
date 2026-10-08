<!-- ---
name:
category:
bzurl:
prodimagename:
surveyurl:
sku:
tags:
--- -->

# Flash JetPack OS to A205 Carrier Board (NVIDIA Jetson Nano & NVIDIA Jetson Xavier NX supported)

In this wiki, we will show you how to flash Jetpack OS to the A205 Carrier Board which supports both NVIDIA Jetson Nano module and NVIDIA Jetson Xavier module. We here will introduce you two ways to flash the system, and because the A205 Carrier Board is different to the official NVIDIA Jetson Carrier Board, the corresponding driver should be installed as well.

![image](https://files.seeedstudio.com/wiki/reComputer_Carrier_Board/A205/Flash_A205.png)

    [Get One Now 🖱️](https://www.seeedstudio.com/A205-Carrier-Board-for-Jetson-Nano-Xavier-NX-p-5133.html)

## Getting Started

We can use **NVIDIA SDK manager and Linux terminal** to flash the system, or we can easily do this by using the **Linux Terminal**. For people who have Linux knowledge base, we highly recommand using Linux Terminal only.

- [Flashing JetPack OS via NVIDIA SDK manager and Linux terminal](#flashing-jetpack-os-via-nvidia-sdk-manager)
- [Flashing JetPack OS via Linux terminal](#flashing-jetpack-os-via-command-line)

There are still some preparation that we need first:

### Software Preparation

- <a href="https://developer.nvidia.com/login" target="_blank">NVIDIA account</a>
- Linux Host Computer with Ubuntu 18.04 OS (or above)

!!!note
 In this tutorial, we will use Ubuntu 18.04 LTS based system to complete the installation.

### Hardware Preparation (Force Recovery Mode)

Before we can move on to the installation steps, we need to make sure that the board is in the force recovery mode. There are different types of the board, please note the difference.

**Step 1.** First, we need to disconnect power of the board.

**Step 2.** Connect your carrier board and your Linux host PC with a **USB type-C link**

![image](https://files.seeedstudio.com/wiki/reComputer_Carrier_Board/A205/Flash_A2051.png)

**Step 3.** Power up and turn on board while pressing **RECOVERY button (W32)** and then release the button.

![image](https://files.seeedstudio.com/wiki/reComputer_Carrier_Board/A205/Flash_A2052.jpg)

**Step 4.** On the Linux host PC screen, we can right click the mouse to open a Terminal and enter the command `lsusb`. When the returned content has the `NVidia Corp.` in it, it means that your A205 Carrier Board is in force recovery mode and you can proceed to the subsequent operations.

The ID depends on the modules on the carrier board and the information show as below:

- For Jetson Nano: **0955:7f21 NVidia Corp**
- For Jetson Xavier NX: **0955:7e19 NVidia Corp**
- For Jetson TX2 NX: **0955:7c18 NVidia Corp**

![image](https://files.seeedstudio.com/wiki/reComputer-Jetson-Nano/5.png)

## Flashing JetPack OS via NVIDIA SDK Manager

Next we will go through the tutorial about installing the system via NVIDIA SDK Manager. The an NVIDIA SDK Manager all-in-one tool that bundles developer software and provides an end-to-end development environment setup solution for NVIDIA SDKs.

![image](https://files.seeedstudio.com/wiki/reComputer-Jetson-Nano/5_3.png)

### Step 1.  Install NVIDIA SDK Manager on the Linux Host PC

We need to open the browser on the Linux Host PC and <a href="https://developer.nvidia.com/nvidia-sdk-manager" target="_blank">download the NVIDIA SDK Manager</a> from the NVIDIA official website.

![image](https://files.seeedstudio.com/wiki/reComputer_flash_system/reComputerJ2021_J202_Flash_Jetpack1.png)

### Step 2.  Open NVIDIA SDK Manager and login

On the Linux host PC screen, we can right click the mouse and open a Terminal. Then we can type the command below to start the SDK Manager:

`sdkmanager`

![image](https://files.seeedstudio.com/wiki/reComputer_flash_system/reComputer_system_installation1.png)

The first time you use NVIDIA SDK Manager, a web page will pop up prompting you to log in with your previously registered NVIDIA account.

### Step 3.  Select the target device

After logging in, you will be taken to the first screen where the first step of installing. Since we have already connected the board, there will be a window pop up to let you select the hardware device.

The example here is equipping with the **NVIDIA Jetson Nano 4GB module**, so we can choose the first one.

![image](https://files.seeedstudio.com/wiki/reComputer-Jetson-Nano/6.jpg)

There are more selections for you to choose in the first screen:

- The **Jetson** in the Product Category panel need to be selected.
- In the Hardware Configuration panel, we recommend that you **do not select Host Machine**. This will take more time to install the NVIDIA components for your current Ubuntu host. You can choose it if you need.
- In the Target Operating System panel, we can select different **operating system** and **JetPack version**. But be careful the version of JetPack, different modules may support different type of JetPack. We recommand "JetPack 4.6.1" here.
- In the Additional SDKs, since the storage space of eMMC is only 16GB, it will be out of memory if we install DeepStream here.

![image](https://files.seeedstudio.com/wiki/reComputer-Jetson-Nano/7.png)

Click Continue to proceed to the next step.

### Step 4.  Review wanted components

From **Details and License**, you can expand the host components and target components panels to review the components that will be installed on your system.

![image](https://files.seeedstudio.com/wiki/reComputer-Jetson-Nano/8.png)

If you only need to install the system, you can uncheck the SDK component.

![image](https://files.seeedstudio.com/wiki/reComputer-Jetson-Nano/8_1.png)

!!!Tip
    When choosing which components to install, you may want to keep an eye on the capacity used. The built-in eMMC size is only 16GB, please allocate and use this space wisely according to your actual needs.
    ![image](https://files.seeedstudio.com/wiki/reComputer-Jetson-Nano/9.png)
    After actual testing, there is only about 500MB of eMMC space left after installing the full set of SDK components.
    ![image](https://files.seeedstudio.com/wiki/reComputer-Jetson-Nano/10_1.jpg)
    If you want to check how to solve the problem of insufficient capacity, please refer to [Troubleshooting](https://wiki.seeedstudio.com/reComputer_Jetson_Series_Initiation/#q1-the-remaining-space-in-the-emmc-in-the-received-recomputer-jetson-is-only-about-2gb-how-can-i-solve-the-problem-of-insufficient-space).

If you want SDK Manager to download all the files to a location other than the default path, go to the Download & Install Options located at the bottom of the screen, then select the path you wish to use.

And because the A205 carrier board requires a flash drive, please make sure to check the **Download now. Install later.** box first to download the system but not install it.

![image](https://files.seeedstudio.com/wiki/reComputer-Jetson-Nano/60.png)

Select Continue to proceed to the next step.

At this point the system will start downloading to the path of your choice, so we can take advantage of this time to get the driver ready.

### Step 5. Choose Proper Drivers

Now, we need to install the driver as well to make sure each component on the board is working. First we need to choose the driver files in Ubuntu host according to the carrier board and the module.


      Carrier Board
      Jetson Module
      JetPack Version
      L4T Version
      Download Address


      A205
      Jetson Nano eMMC
      4.6
      32.6.1
      <a href="../../../../../../../../reComputer%20Jetson%20carrier%20board/reComputer%20A205/Firmware/A205_jp4.6_nano.zip">Download</a>


      A205
      Jetson Xavier NX eMMC
      4.6
      32.6.1
      <a href="../../../../../../../../reComputer%20Jetson%20carrier%20board/reComputer%20A205/Firmware/A205_jp4.6_nx.zip">Download</a>


      A205
      Jetson TX2NX eMMC
      4.6
      32.6.1
      <a href="../../../../../../../../reComputer%20Jetson%20carrier%20board/reComputer%20A205/Firmware/A205_jp4.6_tx2nx.zip">Download</a>


      A205
      Jetson Xavier NX eMMC
      5.0.2
      35.1.0
      <a href="../../../../../../../../reComputer%20Jetson%20carrier%20board/reComputer%20A205/Firmware/205nx_jp5.0.2.zip">Download</a>



!!!Note
 There are two JetPack 5.0.2 drivers for A205 included in the downloaded files. Both work fine, except that one of them supports **IMX-219 camera** and the other one supports **IMX-477 camera**.

### Step 6. Unzip the Driver in the system folder

!!!Attention
 Please note, make sure that the SDK Manager has completed the download of the system before proceeding with this step!

In the Linux host PC, we need to replace some files in the official image with the downloaded driver package files. Since we are using SDK Manager here, the position(path) of the official image is:

`/home/<username>/nvidia/nvidia_sdk/JetPack_<version num>_Linux_<board name>_TARGETS/Linux_for_Tegra`

### Replace the Files

!!!Attention
 Before replacing the files, you can choose to make a backup of the `.dtb` file that will be replaced in the `kernel` folder and save it temporarily in another path so that you can restore the official download at any time.

We can drag the file into the official one:

![image](https://files.seeedstudio.com/wiki/A20X/12.png)

Or we can execute the following command to replace the files:

```sh
cp -a -f ${Drive package kernel path} ${Officially unpacked Linux_for_Tegra path}
```

!!!Note
    `${}` is the use of environment variables.
 `${Drive package kernel path}` indicates the full path to the kernel image folder
 `${Officially unpacked Linux_for_Tegra path}` indicates the full path to the officially provided folder Linux_for_Tegra folder after the L4T zip package is extracted.

### Step 7. Installing system

As we chose to install the system later earlier, we will need to redo **steps 3 to 4** earlier at this point, which will install the system on the A205 with the driver files already replaced.

![image](https://files.seeedstudio.com/wiki/reComputer-Jetson-Nano/61.png)

Before the installation begins, SDK Manager prompts you to enter your `sudo` password.

![image](https://files.seeedstudio.com/wiki/reComputer-Jetson-Nano/12.png)

SDK Manager supports two options to put your Jetson target into Force Recovery Mode. We understand the operation of Jetson-202 Carrier Board into force recovery mode and have already been in force recovery mode in the previous steps. So we select `Manual setup: set the target to Force Recovery Mode via manual operations`.

You can also choose whether to pre-configure the OEM configuration.

- **Pre-Config**: SDK Manager will flash the target with the predefined configuration, and there is no need to complete the System Configuration Wizard after flashing.
- **Runtime**: No default configuration is set on the target, and you will need to manually complete the System Configuration Wizard after flashing.

Here, we select the default **Pre-Config**.

![image](https://files.seeedstudio.com/wiki/reComputer-Jetson-Nano/13.png)

After that, enter the name and password of the new Jetson system at the bottom, please keep them in mind.

When ready, click `Flash` to continue.

The display shows the progress of the download and installation of the software. Please wait patiently for the installation to complete.

![image](https://files.seeedstudio.com/wiki/reComputer-Jetson-Nano/14.png)

### (Optional)Step 7. Install the SDK components

If you checked the installation of the component in the previous **step 4**, you will need to go through this step.

After a moment, you will be able to see a new window pop up in the NVIDIA SDK Manager, prompting you that you need to connect to your device via IP address. It means the system has been alreadly installed and the components installing will be proceeded.

![image](https://files.seeedstudio.com/wiki/reComputer-Jetson-Nano/15.png)

In this case, we can **pull out the jumper** and restart the board. Then we need to connect the board to a monitor via HDMI, enter the password you entered in **step 4**, and log in to the main interface.

At this point you need to connect the board to the same LAN as the Linux host PC and determine the **IP address** of the Jetson by using the command `ifconfig`.

Go back to the Linux host PC and enter the IP address you just obtained. NVIDIA SDK Manager will try to connect to the Jetson device and proceed to complete the installation of the next SDK components.

![image](https://files.seeedstudio.com/wiki/reComputer-Jetson-Nano/16.png)

When you see the following window appear, the installation has been done. But we still need to install the driver so we should remain the board in the **Force Recovery Mode**.

![image](https://files.seeedstudio.com/wiki/reComputer-Jetson-Nano/17.png)

After the flash you can fully apply the board.

## Flashing JetPack OS via Command Line

Thanks to the freedom to customize the BSP(NVIDIA Linux Driver Package), flashing JetPack OS via command line can be very easy for the Linux knowledge base users.

![image](https://files.seeedstudio.com/wiki/reComputer-Jetson-Nano/17_3.png)

### Step 1. Download the proper NVIDIA Linux Driver Package

On the **Linux host PC**, we need to open a browser and go the <a href="https://developer.nvidia.com/embedded/jetson-linux-archive" target="_blank">Jetson Linux Archive</a>. First we should check if the version of Jetson Linux is supported.

![image](https://files.seeedstudio.com/wiki/reComputer_flash_system/reComputer_Jetson_Series_sdk1.png)

Once you find the proper version, click to go to the downloaded page. Find and click the "L4T Driver Package (BSP)" and "Sample Root Filesystem" to download the driver files. The names of the files are like `Tegra_Linux_Sample-Root-Filesystem_Rxx.x.x_aarch64.tbz2` and `Jetson-210_Linux_Rxx.x.x_aarch64.tbz2`.

![image](https://files.seeedstudio.com/wiki/reComputer_flash_system/A205_Flash_Jetpack.png)

As the example, we choose the NVIDIA L4T 32.7.1 version since it is included as part of JetPack4.6.1 and supports the Jetson Nano module. The names of the files:

- Tegra_Linux_Sample-Root-Filesystem_R32.7.2_aarch64.tbz2
- Jetson-210_Linux_R32.7.2_aarch64.tbz2

### Step 2.  Unzip Package Files and Assemble the Rootfs via Command Line

On the Linux host PC, we should find a folder and store the package files we download before. Then open a command line window(Terminal) at the folder and use the command line below to unzip the files and assemble the rootfs:

```sh
tar xf ${L4T_RELEASE_PACKAGE}
cd Linux_for_Tegra/rootfs/
sudo tar xpf ../../${SAMPLE_FS_PACKAGE}
```

!!!Note
    `${}` is where you put the names of the files.

*As the example of **NVIDIA L4T 32.7.1**, the downloaded files are stored in `/Desktop/L4T_Drivers`, so under the '/Desktop/L4T_Drivers' path we open the command line window(Terminal) and execute the following command.

```sh
tar xf Jetson-210_Linux_R32.7.1_aarch64.tbz2
cd Linux_for_Tegra/rootfs/
sudo tar xpf ../../Tegra_Linux_Sample-Root-Filesystem_R32.7.1_aarch64.tbz2
```

### Step 3. Choose Proper Drivers

After we unzip the package, we need to install the driver as well to make sure each component on the board is working. First we need to choose the driver files in Ubuntu host according to the carrier board and the module.


      Carrier Board
      Jetson Module
      JetPack Version
      L4T Version
      Download Address


      A205
      Jetson Nano eMMC
      4.6
      32.6.1
      <a href="../../../../../../../../reComputer%20Jetson%20carrier%20board/reComputer%20A205/Firmware/A205_jp4.6_nano.zip">Download</a>


      A205
      Jetson Xavier NX eMMC
      4.6
      32.6.1
      <a href="../../../../../../../../reComputer%20Jetson%20carrier%20board/reComputer%20A205/Firmware/A205_jp4.6_nx.zip">Download</a>


      A205
      Jetson TX2NX eMMC
      4.6
      32.6.1
      <a href="../../../../../../../../reComputer%20Jetson%20carrier%20board/reComputer%20A205/Firmware/A205_jp4.6_tx2nx.zip">Download</a>


      A205
      Jetson Xavier NX eMMC
      5.0.2
      35.1.0
      <a href="../../../../../../../../reComputer%20Jetson%20carrier%20board/reComputer%20A205/Firmware/205nx_jp5.0.2.zip">Download</a>



!!!Note
 There are two JetPack 5.0.2 drivers for A205 included in the downloaded files. Both work fine, except that one of them supports **IMX-219 camera** and the other one supports **IMX-477 camera**.

### Step 4. Unzip the Driver in the file

We can drag the file into the official one:

![image](https://files.seeedstudio.com/wiki/A20X/12.png)

Or we can execute the following command to replace the files:

```sh
cp -a -f ${Drive package kernel path} ${Officially unpacked Linux_for_Tegra path}
```

!!!Note
    `${}` is the use of environment variables.
 `${Drive package kernel path}` indicates the full path to the kernel image folder
 `${Officially unpacked Linux_for_Tegra path}` indicates the full path to the officially provided folder Linux_for_Tegra folder after the L4T zip package is extracted.

### Step 5.  Flash the System to the Board

In the example we use NVIDIA Jetson Nano module and we can directly flash the system into the board execute following command:

```sh
sudo ./apply_binaries.sh
sudo ./flash.sh ${BOARD} mmcblk0p1
```

!!!Note
    `${BOARD}` is the use of environment variables, the information of it should be the name of your module in the carrier board. You can check <a href="https://files.seeedstudio.com/wiki/A20X/6.png" target="_blank">here</a> for the full knowledge.

![image](https://files.seeedstudio.com/wiki/reComputer-Jetson-Nano/19.png)

!!!Tip
    Flashing L4T takes about 10 minutes, or more under a slow host computer.

After the flash you can fully apply the board.

## Troubleshooting

### Troubleshooting Installation with NVIDIA SDK Manager

There are many causes of various installation errors. Below is a checklist of common installation issues, which may help you recover from a broken installation.

1. Review the summary table to identify which component failed.

    a. Expand the group with the "Error" status.

    b. When you find the failed component, click the details icon to the right of Install Error to be redirected to the Terminal tab, which will display the exact error.

![image](https://files.seeedstudio.com/wiki/reComputer-Jetson-Nano/31.png)

2. If the error is related to an environment issue, such as a broken apt repository or missing prerequisite, try to fix it manually, then click the Retry Failed Items button.

![image](https://files.seeedstudio.com/wiki/reComputer-Jetson-Nano/32.png)

3. Retrying the installation is also available in two other ways:

    a. From **Flashing to eMMC with SDK Manager -- Step 3**, use the Repair/Uninstall button to get to the Manage NVIDIA SDKs page. If needed, expand the SDK that has the "Broken" status, then click Repair for the relevant part (Host or Target).

![image](https://files.seeedstudio.com/wiki/reComputer-Jetson-Nano/33.png)

4. At **Flashing to eMMC with SDK Manager -- Step 3**, select the required SDK and run through the installation again.

5. Finally, try to uninstall and reinstall the relevant SDK.

### Troubleshooting installation using the command line

The command line installation method is relatively simple, and is often prone to error in scenarios where force recovery mode is used.

If you encounter the error shown below in **Flashing to eMMC with command-line -- Step 2**, you probably did not succeed in getting the Board into force recovery mode. Please pay special attention, do not enter force recovery mode with the Carrier Board powered on, as this is not valid.

![image](https://files.seeedstudio.com/wiki/reComputer-Jetson-Nano/34.jpg)

If you can't get into the system in **Flashing to eMMC with command-line -- Step 3** and are stuck on the boot up display command line, you probably did not exit force recovery mode. Likewise, it is not valid for you to unplug the jumper to exit force recovery mode while the Carrier Board is powered up, this all needs to be done while you are powered down.

![image](https://files.seeedstudio.com/wiki/reComputer-Jetson-Nano/35.jpg)

!!!Note
    If more storage space is needed, we can use SD card to expand the capacity, or burn the system on SD card, you can refer to our recommended solution [Flash System on SD card](https://wiki.seeedstudio.com/J101_Enable_SD_Card/)

## Tech Support & Product Discussion

Thank you for choosing our products! We are here to provide you with different support to ensure that your experience with our products is as smooth as possible. We offer several communication channels to cater to different preferences and needs.

<https://forum.seeedstudio.com/>
<https://www.seeedstudio.com/contacts>

<https://discord.gg/eWkprNDMU7>
<https://github.com/Seeed-Studio/wiki-documents/discussions/69>
