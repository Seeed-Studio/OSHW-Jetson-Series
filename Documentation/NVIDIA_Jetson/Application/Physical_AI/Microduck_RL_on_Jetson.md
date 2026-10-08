# Microduck RL on Jetson

  ![Microduck reinforcement learning on Jetson](https://files.seeedstudio.com/wiki/micro_duck-jetson/microduck_jetson_rl_cover.png)

This demo builds a complete robot-learning workflow for **Microduck** on a **Seeed reComputer powered by NVIDIA Jetson Orin NX 16GB**. It covers GPU environment deployment, PPO training with MuJoCo, visualization of local checkpoints, keyboard-controlled inference with official ONNX policies, and the development of new custom motions.

The verified reference platform uses **JetPack 7.2**, **Ubuntu 24.04**, **CUDA 13.2**, **Python 3.12**, and **MuJoCo 3.10**. This tutorial is based on the [`jjjadand/microduck_rl`](https://github.com/jjjadand/microduck_rl) repository, which contains the source code, deployment script, official ONNX policies, and Jetson-trained checkpoints used throughout the guide.

  <a href="https://github.com/jjjadand/microduck_rl" target="_blank" rel="noopener noreferrer">
    Open the Microduck RL Repository ↗
  </a>

## Hardware Options

The tutorial was reproduced on Jetson Orin NX 16GB. The following Seeed Studio systems provide suitable Jetson platforms for following the workflow. The reComputer Classic J5011 offers additional GPU and memory capacity, while exact training throughput depends on the selected power mode and number of parallel environments.



      ![reComputer Super J4012 with Jetson Orin NX 16GB](https://media-cdn.seeedstudio.com/media/catalog/product/cache/bb49d3ec4ee05b6f018e93f896b8a25d/2/-/2-114110311-recomputer-super-j3010_1.jpg)


      reComputer Super J4012
      NVIDIA Jetson Orin NX 16GB

        [Get One Now 🖱️](https://www.seeedstudio.com/reComputer-Super-J4012-p-6443.html)






      ![reComputer Classic J5011 with Jetson AGX Orin 32GB](https://media-cdn.seeedstudio.com/media/catalog/product/cache/bb49d3ec4ee05b6f018e93f896b8a25d/2/-/2-100006184-recomputer-classic-j5011_1.jpg)


      reComputer Classic J5011
      NVIDIA Jetson AGX Orin 32GB

        [Get One Now 🖱️](https://www.seeedstudio.com/reComputer-Classic-J5011-p-6880.html)




## Choose a Chapter

Click a card to open the corresponding chapter. Only this landing page is listed in the Physical AI sidebar; the three chapters remain focused pages accessed from here.

  <a href="/ai_robotics_microduck_rl_jetson_environment/">
    01
    Deploy the Environment
    Prepare JetPack 7.2, deploy the CUDA-enabled Python environment, understand the project directories, and verify GPU training.
    OPEN CHAPTER ➜
  </a>

  <a href="/ai_robotics_microduck_rl_official_policies/">
    02
    Train and Run Official Motions
    Run a training smoke test, visualize a PT checkpoint, launch the official multi-policy ONNX demo, and control it from the keyboard.
    OPEN CHAPTER ➜
  </a>

  <a href="/ai_robotics_microduck_rl_custom_motion_training/">
    03
    Create a Custom Motion
    Select a task template, define motion phases and rewards, register a new task, test it in MuJoCo, train it, and export ONNX.
    OPEN CHAPTER ➜
  </a>

## What You Will Reproduce

- A CUDA-enabled Microduck training environment on Jetson Orin NX.
- PPO training with parallel MuJoCo environments.
- Native and browser-based simulation visualization.
- Official ONNX inference for walking, standing, sit/stand, ground pick, roulade, kicking, and roller motions.
- Keyboard command input and live behavior switching.
- A reusable workflow for creating a custom phase-based motion such as a bow.

## Demo Architecture

```text
Jetson Orin NX
├── JetPack 7.2 / CUDA 13.2
├── uv project environment
├── mjlab + MuJoCo Warp + rsl_rl
├── Microduck task configurations
├── PPO checkpoint (.pt)
└── Exported policy (.onnx)
     ├── MuJoCo inference rehearsal
     └── Microduck runtime deployment
```

> [!TIP]
> For the fastest validation, deploy the environment, run the 64-environment five-iteration smoke test, and then launch the official ONNX keyboard demo. You can complete the custom-motion chapter afterward.
