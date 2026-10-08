# Use IMX477 Camera with A603 Jetson Carrier Board

## Jetpack 5.1.2

If you need to use the IMX477 camera, please download [this driver package](https://szseeedstudio-my.sharepoint.cn/:u:/g/personal/youjiang_yu_szseeedstudio_partner_onmschina_cn/ERJdh3pvdYZOqJWugsnMJKEBMkGXtU8ngY03kJeLDWSkLw?e=TuLWmL) and follow [this tutorial](https://wiki.seeedstudio.com/reComputer_A603_Flash_System/) to reflash the Jetpack system.

> [!WARNING]
> Please note that you need to use the BSP for [ **JP5.1.2** ](https://developer.nvidia.com/embedded/jetson-linux-r3541).

## Jetpack 6.0

If you need to use the IMX477 camera, please download [this driver package](https://szseeedstudio-my.sharepoint.cn/:u:/g/personal/youjiang_yu_szseeedstudio_partner_onmschina_cn/ETIsoZ25I69KsSiA6TweK4UBVfo7gBrvPyKX9pJ68J8oIA?e=a9uumE) and follow [this tutorial](https://wiki.seeedstudio.com/reComputer_A603_Flash_System/) to reflash the Jetpack system.

> [!WARNING]
> Please note that you need to use the BSP for [ **JP6.0** ](https://developer.nvidia.com/embedded/jetson-linux-r363).

After the system flashing is completed, connect the CSI camera and use the following command to start the camera:

```bash
nvgstcapture-1.0 --sensor-id=0
```

![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/A608/camera.png)

## Jetpack 6.2

If you need to use the IMX477 camera, please download [this driver package](https://seeedstudio88-my.sharepoint.com/:u:/g/personal/youjiang_yu_seeedstudio88_onmicrosoft_com/IQC58VP43oyWQY48K__qIXBsAfz5meLpWtldH6SML_BgvCE?e=dXXvuK) and follow [this tutorial](https://wiki.seeedstudio.com/reComputer_A603_Flash_System/) to reflash the Jetpack system.

> [!WARNING]
> Please note that you need to use the BSP for [ **JP6.2** ](https://developer.nvidia.com/embedded/jetson-linux-r3643).

## Tech Support & Product Discussion

Thank you for choosing our products! We are here to provide you with different support to ensure that your experience with our products is as smooth as possible. We offer several communication channels to cater to different preferences and needs.

<https://forum.seeedstudio.com/>
<https://www.seeedstudio.com/contacts>

<https://discord.gg/eWkprNDMU7>
<https://github.com/Seeed-Studio/wiki-documents/discussions/69>
