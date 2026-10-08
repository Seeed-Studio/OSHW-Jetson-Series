# Create Backup and Restore on reComputer

## Introduction

reComputer  is a powerful and compact intelligent edge box to bring up to 275TOPS modern AI performance to the edge.When you have configured and installed the software and environment necessary for your business on recomputer, and need to replicate the project from another new recomputer, reinstalling the software is not efficient. Therefore, this wiki page will use [reComputer J3011](https://www.seeedstudio.com/reComputer-J3011B-p-6405.html) to introduce how to back up your existing software and environment on the recomputer series, making it convenient for you to restore and transplant it to the new recomputer.

> [!NOTE]
> Our testing platform is reComputer J3011, JetPack 5.1.3 and JetPack 6.2 are provided for reference. Please select the appropriate section based on your JetPack version.

## Prerequisite

- Ubuntu Host Computer
- USB Type-C data transmission cable
- reComputer J3011 (with JetPack 5.1.3 or JetPack 6.2 OS)

> [!NOTE]
> Installed and configured necessary software and applications on your reComputer. Ensure these modifications do not impair the device's boot functionality. It's recommended to reboot the device after making changes to confirm stability.
>
> ![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/reComputer_backup/jtop.png)
> Like the screenshot above, we installed the jtop software, where we can use these commands on the terminal directly.
> <a id="Recovery"></a>

## JetPack 5.1.3
### Backing Up the System

**Step 1.** Setting the device into recovery mode refer to this [wiki page](https://wiki.seeedstudio.com/reComputer_J4012_Flash_Jetpack/#enter-force-recovery-mode).

**Step 2.** Obtain the JetPack BSP corresponding to your Jetson module. For JetPack 5.1.3, download the Jetson Linux R35.5.0 BSP from [NVIDIA's official site.](https://developer.nvidia.com/embedded/jetson-linux-r3550)
![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/reComputer_backup/download_bsp.jpg)

**Step 3.** Extract the BSP file to access the Linux_for_Tegra directory.

```bash
tar -xvzf jetson-linux-*.tbz2
# For Jetpack 5.1.3: tar -xvzf Jetson_Linux_R35.5.0_aarch64.tbz2
```

![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/reComputer_backup/zip.jpg)

**Step 4.** Copy the contents of Linux_for_Tegra to your JetPack flashing package directory (e.g., mfi_recomputer-orin).
> [!NOTE]
> "flashing package directory" is the directory file used during the process of flashing the system.

Use the `-rn` options to preserve existing files:

```bash
sudo cp -rn Linux_for_Tegra/* mfi_recomputer-orin
```

**Step 5.** Navigate to your JetPack flashing package directory:

```bash
cd /path/to/mfi_recomputer-orin
```

**Step 6.** Execute the backup script, specifying your storage device and desired backup name:

```bash
sudo ./tools/backup_restore/l4t_backup_restore.sh -e nvme0n1 -b recomputer-orin
```

> [!NOTE]
> -b `<target_board>` replace with your device
>

> [!NOTE]
> you can navigate  to your Jepack flashing package directory and find a `xxx.conf` file.
> `xxx` is your  `<target_board>`
>
> ```bash
> ls | grep *.conf
> ```
>
> ![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/reComputer_backup/conf_file1.jpg)

![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/reComputer_backup/backup_start.png)

wait patiently until it finished.
If all goes well, you will see something similar to the screenshot below in the terminal:

![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/reComputer_backup/success_back1.png)

> [!NOTE]
> During this process, your device may reboot many times like the flashing  process, you are not recommended to use virtual machines or WSL  because it might lose connection and cause the backup/restore process  failed.   You may encounter some missing files; you can open the `recomputer-orin.conf` and remove the file that didn’t exist.
> Usually  these are temporary device tree overlay object files; they don't affect the  backup and restore results. But if you made modifications to BSP, you will  need to merge your overlay files.

### Restoring the System

**Step 1.** Insert a new, empty [SSD](https://www.seeedstudio.com/M-2-2280-SSD-128GB-p-5332.html) into your reComputer.

![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/reComputer_backup/new_ssd.jpg)

**Step 2.** Enter force recovery mode as [previously described.](#Recovery)

**Step 3.** On your host system, navigate to your JetPack flashing package directory and execute the restore command on host:

```bash
sudo ./tools/backup_restore/l4t_backup_restore.sh -e nvme0n1 -r recomputer-orin
```

If all goes well, you will see something similar to the screenshot below in the terminal:
![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/reComputer_backup/finish_store1.png)

**Step 4.** Power up the jetson device, use the username and password we previously set. And test some software we previously installed. If it worked, then our restore is successful.
![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/reComputer_backup/jtop2.png)
Because we had installed jtop in our previous system, we can directly launch jtop in the terminal of the new system.

> [!NOTE]
> Additionally, following cases have been tested for backup and restore:
>
> - Restore the backup to original SSD.
> - Restore the backup to different SSD.
> - Restore the backup to same carrier board, with Jetson module in same  batch, different SSDs.
>

## JetPack 6.2
### Backing Up the System

For JetPack 6.2 (L4T 36.4.3), the backup process requires downloading the compiled Seeed BSP firmware and compiling the source code before performing the backup.

**Step 1.** Download the compiled Seeed BSP firmware: [L4T-36.4.3](https://files.seeedstudio.com/wiki/reComputer-Jetson/reComputer_backup/L4T36-4-3_plus.tar)

**Step 2.** Extract the downloaded package and generate the necessary content using the following commands in your PC terminal:

```bash
sudo tar xpf L4T36-4-3_plus.tar
# For example: sudo tar xpf L4T36-4-3_plus.tar

cd Linux_for_Tegra/
sudo ./apply_binaries.sh
cd ..
```

**Step 3.** Set up environment variables in the extracted directory (where the tar.gz package is located):

```bash
export ARCH=arm64
export CROSS_COMPILE="$PWD/aarch64--glibc--stable-2022.08-1/bin/aarch64-buildroot-linux-gnu-"
export PATH="$PWD/aarch64--glibc--stable-2022.08-1/bin:$PATH"
export INSTALL_MOD_PATH="$PWD/Linux_for_Tegra/rootfs/"
```

**Step 4.** Navigate to the source directory and compile the source code (this process will take some time):

```bash
cd Linux_for_Tegra/source
./nvbuild.sh
```

**Step 5.** After compilation is complete, copy and install the compiled components:

```bash
./do_copy.sh
./nvbuild.sh -i
```

**Step 6.** The working directory is now prepared. Navigate to the `Linux_for_Tegra/` directory,Setting the device into recovery mode refer to this [wiki page](https://wiki.seeedstudio.com/reComputer_J4012_Flash_Jetpack/#enter-force-recovery-mode) and execute the backup script:

```bash
cd ../
sudo ./tools/backup_restore/l4t_backup_restore.sh -e nvme0n1 -b recomputer-orin-j401
```

> [!NOTE]
> -b `<target_board>` replace with your device. For JetPack 6.2, the default target board is `recomputer-orin-j401`.

Wait patiently until it finishes. If all goes well, you will see a success message in the terminal.

> [!NOTE]
> During this process, your device may reboot many times like the flashing process, you are not recommended to use virtual machines or WSL because it might lose connection and cause the backup/restore process failed.

### Restoring the System

**Step 1.** Insert a new, empty [SSD](https://www.seeedstudio.com/M-2-2280-SSD-128GB-p-5332.html) into your reComputer.

**Step 2.** Enter force recovery mode as [previously described.](#Recovery)

**Step 3.** On your host system, navigate to your `Linux_for_Tegra/` directory and execute the restore command on host:

```bash
sudo ./tools/backup_restore/l4t_backup_restore.sh -e nvme0n1 -r recomputer-orin-j401
```

If all goes well, you will see a success message in the terminal.

**Step 4.** Power up the Jetson device, use the username and password we previously set. And test some software we previously installed. If it worked, then our restore is successful.

> [!NOTE]
> Additionally, following cases have been tested for backup and restore:
>
> - Restore the backup to original SSD.
> - Restore the backup to different SSD.
> - Restore the backup to same carrier board, with Jetson module in same batch, different SSDs.

## Resources

- [Flash JetPack OS to J401 Carrier Board](https://wiki.seeedstudio.com/reComputer_J4012_Flash_Jetpack/)
- [reComputer J30x Datasheet](../../../reComputer%20Jetson%20carrier%20board/reComputer%20J301-J401/Datasheet/reComputer-J301x-datasheet.pdf)
- [reComputer J40x Datasheet](../../../reComputer%20Jetson%20carrier%20board/reComputer%20J401/Datasheet/reComputer-J401x-datasheet.pdf)
- [reComputer J30/J40 Schematic](../../../reComputer%20Jetson%20carrier%20board/reComputer%20J401/Schematic/reComputer_J401_SCH_V1.0.pdf)
- [reComputer J30/J40 3D File](../../../reComputer%20Jetson%20carrier%20board/reComputer%20J401/3D%20Model/reComputer-J4012.stp)
- [Seeed Jetson Serials Catalog](../../../reComputer%20Jetson%20carrier%20board/Common/Datasheet/Seeed-NVIDIA_Jetson_Catalog_V1.4.pdf)
- [Seeed Studio Edge AI Success Stories](../../../reComputer%20Jetson%20carrier%20board/Common/Datasheet/Seeed_NVIDIA_Jetson_Success_Cases_and_Examples.pdf)
- [Seeed Jetson Serials Comparision](https://www.seeedstudio.com/blog/nvidia-jetson-comparison-nano-tx2-nx-xavier-nx-agx-orin/)
- [Seeed Jetson Devices One Page](../../../reComputer%20Jetson%20carrier%20board/Common/Datasheet/Seeed-Jetson-one-pager.pdf)
- [Jetson examples](https://github.com/Seeed-Projects/jetson-examples)
- [reComputer-Jetson-for-Beginners](https://github.com/Seeed-Projects/reComputer-Jetson-for-Beginners)

## Tech Support & Product Discussion

Thank you for choosing our products! We are here to provide you with different support to ensure that your experience with our products is as smooth as possible. We offer several communication channels to cater to different preferences and needs.

<https://forum.seeedstudio.com/>
<https://www.seeedstudio.com/contacts>

<https://discord.gg/eWkprNDMU7>
<https://github.com/Seeed-Studio/wiki-documents/discussions/69>
