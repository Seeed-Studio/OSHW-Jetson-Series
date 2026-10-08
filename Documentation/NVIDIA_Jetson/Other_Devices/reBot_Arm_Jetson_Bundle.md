# reBot Arm B601 × NVIDIA Jetson Getting Started

## Introduction

An All-in-One Embodied AI Development Platform for the New Era of Physical AI.
As generative AI evolves from simply “understanding the world” to actively “interacting with the world,” robotics development is entering a new era: Physical AI.
To help developers, researchers, and educators accelerate their journey into Embodied AI, Seeed Studio combines the fully open-source reBot Arm B601 with the cutting-edge NVIDIA Jetson Developer Kit to create a powerful next-generation robotics development bundle.

This bundle delivers not only precise robotic manipulation capabilities, but also the massive AI computing power required for running multimodal AI models, vision-language models (VLMs), and real-time robotic inference locally at the edge.
It is a complete platform for building the next wave of intelligent robots — from learning and research to rapid prototyping and deployment.


         reBot Arm B601 DM
         reBot Arm B601 RS




                ![image](https://media-cdn.seeedstudio.com/media/catalog/product/cache/bb49d3ec4ee05b6f018e93f896b8a25d/i/m/img_v3_0210p_67d75fe6-a1fe-40a9-b025-ac92efb1bbbg_1.jpg)




                ![image](https://media-cdn.seeedstudio.com/media/catalog/product/cache/bb49d3ec4ee05b6f018e93f896b8a25d/0/-/0-100019336--rebot-arm-b601-rs-assembled-kit-with-gripper--rebot-arm-b601-rs.jpg)







                    [Quick Start](https://wiki.seeedstudio.com/rebot_b601_dm_getting_started/)


                    [Get One Now 🖱️](https://www.seeedstudio.com/reBot-Arm-B601-DM-Bundle.html)






                    [Quick Start](https://wiki.seeedstudio.com/rebot_b601_rs_getting_started/)


                    [Get One Now 🖱️](https://www.seeedstudio.com/reBot-Arm-B601-RS-Assembled-Kit-with-Gripper-p-6865.html)





         NVIDIA® Jetson AGX Thor™ Developer Kit
         reComputer Classic J3011




                ![image](https://media-cdn.seeedstudio.com/media/catalog/product/cache/bb49d3ec4ee05b6f018e93f896b8a25d/i/m/image-kit-3.png)




                ![image](https://media-cdn.seeedstudio.com/media/catalog/product/cache/bb49d3ec4ee05b6f018e93f896b8a25d/1/1/110110147.jpg)







                    [Quick Start](https://docs.nvidia.com/jetson/agx-thor-devkit/user-guide/latest/quick_start.html)


                    [Get One Now 🖱️](https://www.seeedstudio.com/NVIDIA-Jetson-AGX-Thor-Developer-Kit-p-9965.html)






                    [Quick Start](https://wiki.seeedstudio.com/reComputer_J30_40_with_Jetson_getting_start/)


                    [Get One Now 🖱️](https://www.seeedstudio.com/reComputer-J3011-p-5590.html)





> [!WARNING]
> Here, we use the NVIDIA Jetson Thor as an example to demonstrate how to quickly control the reBot Arm B601 robotic arm with Jetson. You can also choose other Jetson devices based on your specific needs.

## Why This Bundle?

A Complete Embodied AI Development Platform

Traditional robotics development often comes with several limitations:

1. Closed hardware ecosystems
2. Insufficient AI computing power
3. Fragmented software stacks
4. High development barriers
5. Difficulty validating real-world Physical AI scenarios

The reBot Arm × Jetson Bundle is designed to solve these challenges.

With this bundle, you get:

1. A fully open-source 6+1 DoF robotic arm platform
2. NVIDIA’s flagship edge AI computing platform powered by GPU
3. Native support for ROS1, ROS2, Isaac Sim, and LeRobot
4. Ready for multimodal AI and generative AI workflows
5. A unified environment for education, research, and AI robotics prototyping

## Getting Started

### Hardware Connection

1. Refer to [this guide](https://wiki.seeedstudio.com/rebot_b601_dm_getting_started/) to assemble the robotic arm.
2. Use a USB-to-CAN adapter to connect the robotic arm to the NVIDIA Jetson via the Type-C interface.

### One-Click Install Arm Driver

Open the terminal window on the Jetson and run the following command.

```bash
uv pip install motorbridge
```

    ![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/rebot_arm_bundle/install_driver.png)

### WebUI

run this command on Nvidia Jetson:

```bash
motorbridge-gateway --bind 127.0.0.1:9002 --vendor damiao --transport dm-serial --serial-port /dev/ttyACM0 --serial-baud 921600 --dt-ms 20
```

Then, Open `https://motorbridge.github.io/motorbridge-studio/` in your browser, and you will see the following page. From this interface, you can adjust motor parameters, check the status of the robotic arm, and perform other operations.

    ![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/rebot_arm_bundle/webui.png)

## Application

    

![LeRobot for reBot Arm B601-DM](https://files.seeedstudio.com/wiki/reComputer-Jetson/rebot_arm_bundle/lerobot.png)

[Getting Started with reBot Arm B601-DM in LeRobot](https://wiki.seeedstudio.com/rebot_arm_b601_dm_lerobot/)


    

![Visual Grasping Demo for reBot Arm B601-DM](https://raw.githubusercontent.com/Seeed-Projects/reBot-DevArm/main/media/v1.0.png)

[reBot Arm B601-DM Visual Grasping Demo](https://wiki.seeedstudio.com/rebot_arm_b601_dm_grasping_demo/)


    

![Control reBot Arm with NemoClaw on Nvidia Jetson Thor](https://files.seeedstudio.com/wiki/reComputer-Jetson/rebot_arm_nemoclaw/robot_webui.png)

[Control reBot Arm with NemoClaw on Nvidia Jetson Thor](https://wiki.seeedstudio.com/control_rebot_arm_with_nemoclaw_on_nvidia_jetson_thor/)


    

![Voice Control reBot Arm B601 by Nvidia Jetson Thor](https://files.seeedstudio.com/wiki/reComputer-Jetson/voice_controlled_rebot_arm/cover_page.png)

[Voice Control reBot Arm B601 by Nvidia Jetson Thor](https://wiki.seeedstudio.com/voice_control_rebot_arm/)


    

![reBot Arm B601-RS ROS2 Integration](https://files.seeedstudio.com/wiki/robotics/projects/rebot_arm/RS5_56.png)

[reBot Arm B601-RS ROS2 Integration](https://wiki.seeedstudio.com/rebot_arm_b601_rs_ros2_integration/)


    

![Simulating reBotArm through Isaacsim](https://files.seeedstudio.com/wiki/robotics/projects/rebot_arm/reBot_Arm_RS_isaacsim.jpg)

[Simulating reBotArm through Isaacsim](https://wiki.seeedstudio.com/rebot_arm_b601_rs_isaacsim/)



## Tech Support & Product Discussion

Thank you for choosing our products! We are here to provide you with different support to ensure that your experience with our products is as smooth as possible. We offer several communication channels to cater to different preferences and needs.

<https://forum.seeedstudio.com/>
<https://www.seeedstudio.com/contacts>

<https://discord.gg/eWkprNDMU7>
<https://github.com/Seeed-Studio/wiki-documents/discussions/69>
