# Connect Device

Seeed Jetson DevelopTool connects to your Jetson device in two ways depending on the task:

| Connection Type | Used For |
|-----------------|----------|
| **USB (Recovery Mode)** | Firmware flashing via Flash Center |
| **Ethernet / SSH** | Device Management, Remote Dev, App Market, Skills, PC Network Sharing |

## USB Connection (Recovery Mode)

Recovery mode is required for flashing firmware. To enter Recovery mode:

1. Power off the Jetson device.
2. Hold the **Recovery** button on the device.
3. While holding Recovery, connect the USB-C cable between the device and your host PC (or power on the device).
4. Release the Recovery button after 2 seconds.

In the DevelopTool, open **Flash Center** and click **Detect Device** to confirm the USB connection is recognized.

> [!TIP]
> On Linux, you can verify the device appears with:
>
> ```bash
> lsusb | grep NVIDIA
> ```
>
> You should see an entry like `NVIDIA Corp. APX`.

> [!WARNING]
> On Windows, USB passthrough via WSL2 requires the `usbipd` tool. Native Linux is recommended for reliable flashing.

## Ethernet / SSH Connection

For all non-flashing features, the DevelopTool connects to Jetson over SSH via Ethernet (or Wi-Fi if configured).

![image](https://files.seeedstudio.com/wiki/Seeed-Jetson-DevelopTool/ui-device-connection.png)

**Steps:**

1. Connect Jetson and the host PC to the same network, or use a direct Ethernet cable with [PC Network Sharing](https://wiki.seeedstudio.com/jetson_developtool_remote_development/) enabled.
2. In the DevelopTool, open the **Remote Dev** tab.
3. Enter the Jetson's IP address, SSH username, and password in the **Device Connection** panel.
4. Click **Connect**.

![image](https://files.seeedstudio.com/wiki/Seeed-Jetson-DevelopTool/connect-device-connection.png)

Once connected, the device status panel shows real-time CPU, GPU, memory, and temperature information.

> [!TIP]
> If you don't know your Jetson's IP address, use the [Jetson Init](https://wiki.seeedstudio.com/jetson_developtool_remote_development/) serial wizard on first boot to configure the network and display the assigned IP.

## Tech Support & Product Discussion

Thank you for choosing our products! We are here to provide you with different support to ensure that your experience with our products is as smooth as possible. We offer several communication channels to cater to different preferences and needs.

<https://forum.seeedstudio.com/>
<https://www.seeedstudio.com/contacts>

<https://discord.gg/eWkprNDMU7>
<https://github.com/Seeed-Studio/wiki-documents/discussions/69>
