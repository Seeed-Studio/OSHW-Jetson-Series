# Getting Started with Scailable on NVIDIA® Jetson Devices

![image](https://files.seeedstudio.com/wiki/Scailable/wiki-thumb-4.gif)

## What is Scailable?

[Scailable](https://scailable.net) provides a platform for creating and managing Edge AI solutions at scale. With Scailable, you can simply configure any supported edge device (such as a router, gateway, or IPC) to turn it into a "smart" device. Smart devices can run advanced Artificial Intelligence (AI) and Machine Learning (ML) models on input data, such as a video stream, to turn the input into something meaningful, such as a count of the number of cars in the video.

## Why Scailable on NVIDIA Jetson?

NVIDIA Jetson platform is a great candidate to run Scailable because, as an Edge AI device including NVIDIA SoMs, it is able to give a better inference performance after deploying various AI pipelines over-the-air at scale to these devices.

This wiki will walkthrough how you can easily install Scailable AI Manager on the NVIDIA Jetson platform and use Scailable Platform to remotely configure and manage your AI solution at scale.

## Prerequisites

- NVIDIA Jetson device running NVIDIA JetPack 5.0+ and connected to the internet

  - We have tested this wiki with [reComputer J4012](https://www.seeedstudio.com/reComputer-J4012-p-5586.html) running [JetPack 5.1.1](https://developer.nvidia.com/embedded/jetpack-sdk-511). If you want to explore more NVIDIA Jetson devices offered by Seeed, please visit [this page](../../../../reComputer%20Jetson%20carrier%20board/Common/Datasheet/NVIDIA-Jetson-Devices-and-carrier-boards-comparision.pdf).
- Host PC with Windows, Linux or Mac and connected to the internet

## Install Scailable AI Manager

**Step 1:** Execute the below command to install Scailable AI Manager on the Jetson Orin device

```sh
sudo bash -ic "$(wget -q -O - https://get.sclbl.net)"
```

> [!NOTE]
> During the installation, you need to enter "y" to the prompt which asks you to enable JetPack 5 support.

![image](https://files.seeedstudio.com/wiki/Scailable/2.jpg
)

**Step 2:** You can enter the IP address of the Jetson device followed by **:8081** on a web browser or simply enter the URL that you will see on the command line as follows

![image](https://files.seeedstudio.com/wiki/Scailable/4.jpg
)

## Register for Scailable account

**Step 1:** Once the Scailable AI Manager shows up, register the device by giving it a name and click the **Register** button

![image](https://files.seeedstudio.com/wiki/Scailable/1.jpg
)

**Step 3:** Confirm the device name that you created before, click **Register** and click **Return to device**

![image](https://files.seeedstudio.com/wiki/Scailable/7.jpg
)

If everything went well, you will see all the status check are successful under the **Status** tab as follows

![image](https://files.seeedstudio.com/wiki/Scailable/8.jpg
)

## Run AI Application

Scailable comes pre-loaded with many different AI models for you to try out. However, if you want to use your own AI model, you can import it as well.

**Step 1:** Under the **Model** tab, inside **First Model** section, click **Assign Model**

![image](https://files.seeedstudio.com/wiki/Scailable/9.jpg
)

**Step 2:** Here you can either add your own model by clicking on **add a model** or use a pre-built model. Here we will choose **Scailable Models**

![image](https://files.seeedstudio.com/wiki/Scailable/10.jpg
)

**Step 3:** As an example, we will choose **People counter within a region** model. Click **Use this model**

![image](https://files.seeedstudio.com/wiki/Scailable/12.png
)

Now you will see the model is selected

![image](https://files.seeedstudio.com/wiki/Scailable/13.png
)

**Step 4:** Under **Input** tab, select **Video driver** for the Input driver

![image](https://files.seeedstudio.com/wiki/Scailable/14.png
)

Here you can select either a video stream, image or example image/ video preloaded with Scailable

![image](https://files.seeedstudio.com/wiki/Scailable/16.png
)

**Step 5:** For example, we will choose a pre-loaded video source that comes with Scailable which is **faces**

![image](https://files.seeedstudio.com/wiki/Scailable/15.jpg
)

**Step 6:** Under **output** tab, keep the settings as default

![image](https://files.seeedstudio.com/wiki/Scailable/17.png
)

**Step 7:** Under **Options** tab, keep the settings as default

![image](https://files.seeedstudio.com/wiki/Scailable/18.png
)

**Step 7:** Under **Test** tab, click **Test configuration**

![image](https://files.seeedstudio.com/wiki/Scailable/19.png
)

You will see the following output if it is successful

![image](https://files.seeedstudio.com/wiki/Scailable/20.png
)

**Step 8:** Under **Run** tab, click **Run Model**

![image](https://files.seeedstudio.com/wiki/Scailable/21.png
)

You will see the following output if it is running successfully

![image](https://files.seeedstudio.com/wiki/Scailable/22.png
)

**Step 9:** Click **View live visualization** to preview inference results locally

![image](https://files.seeedstudio.com/wiki/Scailable/23.png
)

![image](https://files.seeedstudio.com/wiki/Scailable/25.png
)

**Step 10:** Click **View output in cloud** to download the results in CSV or JSON formats

![image](https://files.seeedstudio.com/wiki/Scailable/26.png
)

![image](https://files.seeedstudio.com/wiki/Scailable/27.png
)

## Deploy AI Models at Scale

Using Scailable, you can deploy a single model to multiple devices at scale with ease

**Step 1:** Visit [this webpage](https://admin.sclbl.net/login), login to your Scailable account and you will see the dashboard as follows

![image](https://files.seeedstudio.com/wiki/Scailable/32.png
)

**Step 2:** Once you click **DEVICES**, you will see all your devices connected with your Scailable account

![image](https://files.seeedstudio.com/wiki/Scailable/28.png
)

**Step 3:** Select all the devices by clicking on the check box, enter a name for the device group and click **Save new groups**

![image](https://files.seeedstudio.com/wiki/Scailable/29.png
)

**Step 4:** Click **Assign a model to all devices in group**

![image](https://files.seeedstudio.com/wiki/Scailable/30.png
)

**Step 5:** Choose a model as we did before and the model will be deployed to all the devices in the group remotely

Upon successfully deploying the model remotely, you will see the following output

![image](https://files.seeedstudio.com/wiki/Scailable/31.jpg
)

## Learn more

Scailable offers very detailed and comprehensive documentation. So it is highly recommended to check them [here](https://docs.scailable.net).

## Tech Support & Product Discussion

Thank you for choosing our products! We are here to provide you with different support to ensure that your experience with our products is as smooth as possible. We offer several communication channels to cater to different preferences and needs.

<https://forum.seeedstudio.com/>
<https://www.seeedstudio.com/contacts>

<https://discord.gg/eWkprNDMU7>
<https://github.com/Seeed-Studio/wiki-documents/discussions/69>
