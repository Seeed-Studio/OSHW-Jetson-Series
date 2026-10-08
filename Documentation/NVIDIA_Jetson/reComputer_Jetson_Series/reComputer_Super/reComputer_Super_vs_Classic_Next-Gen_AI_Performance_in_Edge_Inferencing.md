# reComputer Super vs Classic Next-Gen AI Performance in Edge Inferencing

![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/reComputer-super/super.png)

[Get One Now 🖱️](https://www.seeedstudio.com/reComputer-Super-Bundle.html)

## Introduction

The reComputer Super Series supercharges the reComputer Classic, delivering up to a 1.7x boost of 157 TOPS in AI performance. This wiki compares the performance differences between the reComputer Super and reComputer Classic in AI text generation and AI video processing. Using the <a href="https://www.seeedstudio.com/NVIDIA-Jetson-Orin-NX-Module-16GB-p-5524.html" target="_blank">NVIDIA Jetson Orin NX 16GB module</a> as the test platform, it clearly demonstrates that the reComputer Super delivers superior performance compared to the reComputer Classic.

## AI Text Generation

In this section, we use Ollama to load the deepseek-r1:7b model and compare the inference speed of the model in different devices. It is evident that the reComputer Super has a improvement in inference speed and GPU frequency to the reComputer Classic.

> [!NOTE]
> The main steps for deploying this model are:
>
> **Step 1.** Install jetson-containers.
>
> **Step 2.** Enter the Docker container to run the Ollama service.
>
> **Step 3.** Pull the deepseek-r1:7b model from Ollama.

> Embedded media: <https://www.youtube.com/embed/nD1w-odV-ZU>

To facilitate the demonstration, we input "tell me a story." into the terminal and asked DeepSeek to generate a short story for us. Due to the randomness of the generation results produced by the model, the results we obtain will generally not be the same. When we can measure the performance of the device's inference based on the speed at which the model generates tokens.(As demonstrated in the video, the eval rate indicator is used)

> [!NOTE]
> If you also want to deploy Ollama onto your Jetson device, please refer to [this tutorial](https://www.jetson-ai-lab.com/tutorial_ollama.html) to learn how to quickly deploy it on Nvidia Jetson.

## AI Video Processing

In this section, we deployed the object detection model YOLOv11 on two devices and compared the performance differences between them when processing video inputs.The results indicate that the reComputer Super is capable of processing approximately 2.37 times more images per second than the reComputer Classic.

> [!NOTE]
> Refer to [this repository](https://github.com/wang-xinyu/tensorrtx/tree/master/yolo11) can deploy YOLOv11 on your devices like us.
> The main steps for deploying this model are:
>
> **Step 1.** Clone this [GitHub repository](https://github.com/wang-xinyu/tensorrtx/tree/master).
>
> **Step 2.** Download the pre-trained weight file yolo11n.pt from [ultralytics](https://github.com/ultralytics/ultralytics).
>
> **Step 3.** Follow [this repository](https://github.com/wang-xinyu/tensorrtx/tree/master/yolo11) to compile the model and run the inference.
>
> **Step 4.** We refer to yolo11_det_trt.py script in [this repository](https://github.com/wang-xinyu/tensorrtx/tree/master/yolo11) to run the inference.

> Embedded media: <https://www.youtube.com/embed/ELbltFieez4>

> [!NOTE]
> The Average FPS shown in the terminal reflects the pure inference speed of the model, directly indicating the difference in device computing power, so the reComputer Super shows a significantly higher FPS. However, the real-time FPS displayed in the top-left corner of the display window represents the frame rate of the entire processing pipeline, including image capture, preprocessing, inference, post-processing, and display. This FPS is affected by multiple factors such as camera frame rate, display refresh rate, and program frame rate limits, causing the displayed FPS on both devices to be similar and masking the difference in inference performance. Therefore, device performance should be evaluated based on the average inference FPS output in the terminal rather than relying solely on the real-time displayed FPS.

## References

- https://www.jetson-ai-lab.com/tutorial_ollama.html
- https://www.deepseek.com/
- https://wiki.seeedstudio.com/deploy_deepseek_on_jetson/
- https://www.seeedstudio.com/edge-ai/generative-ai
- https://github.com/ultralytics/ultralytics
- https://github.com/wang-xinyu/tensorrtx?tab=readme-ov-file

## Tech Support & Product Discussion

Thank you for choosing our products! We are here to provide you with different support to ensure that your experience with our products is as smooth as possible. We offer several communication channels to cater to different preferences and needs.

<https://forum.seeedstudio.com/>
<https://www.seeedstudio.com/contacts>

<https://discord.gg/eWkprNDMU7>
<https://github.com/Seeed-Studio/wiki-documents/discussions/69>
