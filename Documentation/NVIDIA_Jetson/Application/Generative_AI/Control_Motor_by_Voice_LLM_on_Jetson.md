# Control Motor by Voice LLM on Jetson

## Introduction

This wiki builds an end-to-end voice-controlled motor system based on the Jetson platform (reComputer Robotics J4012), integrating speech recognition, edge large language model (LLM) intent understanding, and hardware control to enable natural human-machine interaction—users can control MyActuator X Series Motors with simple voice commands (e.g., "Rotate 90 degrees clockwise").

## Prerequisites
- reComputer Robotics J4012
- reSpeaker XVF3800
- MyActuator X Series Motors


        reComputer Robotics J4012
        reSpeaker XVF3800
        MyActuator X Series Motors




                ![image](https://media-cdn.seeedstudio.com/media/catalog/product/cache/bb49d3ec4ee05b6f018e93f896b8a25d/1/-/1-114110310-recomputer-robotics_2.jpg)




                ![image](https://media-cdn.seeedstudio.com/media/catalog/product/cache/bb49d3ec4ee05b6f018e93f896b8a25d/1/-/1-respeaker-xvf3800-4-mic-array-with-xiao-esp32s3.jpg)




                ![image](https://media-cdn.seeedstudio.com/media/catalog/product/cache/bb49d3ec4ee05b6f018e93f896b8a25d/i/m/image-motor.png)






                [Get One Now 🖱️](https://www.seeedstudio.com/reComputer-Robotics-J4012-p-6505.html)




                [Get One Now 🖱️](https://www.seeedstudio.com/ReSpeaker-XVF3800-4-Mic-Array-With-XIAO-ESP32S3-p-6489.html)




                [Get One Now 🖱️](https://www.seeedstudio.com/Myactuator-X4-P36-Planetary-Actuator-p-6469.html)




## Hardware Connection

    ![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/voice_control/hardware_connect.jfif)

## Getting Started

The workflow of the entire system involves three steps:

1. ASR: The microphone captures audio commands from the user and converts them into text using Whisper.
2. Function Calling: The large language model generates motor control parameters that meet the requirements based on the user's input instructions.
3. Motor Control: The appropriate control program is called to drive the motor to rotate to the specified position.

Next, we will explain the implementation of each step in detail.

### Install Whisper Server

First, we need to install the Whisper service to enable ASR functionality. Please open a terminal window on the Jetson device and run the following command.

```bash
git clone https://github.com/jjjadand/whisper-stable4curl
cd whisper-stable4curl
export PATH=/usr/local/cuda-12.6/bin${PATH:+:${PATH}}
export LD_LIBRARY_PATH=/usr/local/cuda-12.6/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
cmake --build build -j --config Release
```

If everything goes well, you will see the following logs in the terminal window.

    ![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/voice_control/whisper.png)

Then we launch the Whisper inference service:

```bash
./build/bin/whisper-stream -m ./models/ggml-base.en-q5_1.bin -t 8 --step 0 --length 7000 -vth 0.7 --keep 1200
```

    ![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/voice_control/launch_whisper.png)

### Install Ollama

Ollama is an extremely user-friendly edge computing LLM inference framework that can be deployed on Jetson with just a single command. Open a new terminal window on your Jetson device and execute:

```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama pull qwen2.5
```

> [!NOTE]
> Here, we use the Qwen 2.5 large language model to understand the user's intent.

### Install Motor Control Script

Execute the following command to start the motor control script:

```bash
git clone https://github.com/yuyoujiang/voice_control.git
cd voice_control
sudo ip link set can0 type can bitrate 1000000
sudo ip link set can0 up
python app.py
```

    ![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/voice_control/motor_control.png)

## Effect Demonstration


> Embedded media: <https://www.youtube.com/embed/ORv8x0aSXfQ>

## Tech Support & Product Discussion

Thank you for choosing our products! We are here to provide you with different support to ensure that your experience with our products is as smooth as possible. We offer several communication channels to cater to different preferences and needs.

<https://forum.seeedstudio.com/>
<https://www.seeedstudio.com/contacts>

<https://discord.gg/eWkprNDMU7>
<https://github.com/Seeed-Studio/wiki-documents/discussions/69>
