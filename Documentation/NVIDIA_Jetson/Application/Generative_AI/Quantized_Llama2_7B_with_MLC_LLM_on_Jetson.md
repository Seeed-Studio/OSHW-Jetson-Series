# Quantized Llama2-7B with MLC LLM on Jetson

## Introduction

In recent years, large language models such as GPT-3 have revolutionized natural language processing tasks. However, most of these models are trained on large-scale datasets, which require powerful computing resources and are not suitable for deployment on edge devices. To address this issue, researchers have developed quantization techniques to compress large models into smaller ones without sacrificing performance.

In this project, we introduce a quantized version of [Llama2-7B](https://huggingface.co/meta-llama/Llama-2-7b-hf), a large language model trained on 1.5TB of data, and deploy it on the Jetson Orin. We also leverage the [Machine Learning Compiler Large Language Modle](https://llm.mlc.ai)(MLC LLM) to accelerate the inference speed of the model. By deploying the quantized Llama2-7B with MLC LLM on the [Jetson Orin NX](https://www.seeedstudio.com/reComputer-J4012-p-5586.html), developers can build powerful natural language processing applications that deliver high accuracy and low latency on edge devices.

![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/A608/MLC_LLM.gif)

## Hardware components



   reComputer(Or other devices based on Jetson)


      ![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/A608/recomputerj4012.jpg)



    [Get One Now 🖱️](https://www.seeedstudio.com/reComputer-J4012-p-5586.html)




## Install dependencies

```shell
sudo apt-get update && sudo apt-get install git python3-pip
```

```shell
git clone --depth=1 https://github.com/dusty-nv/jetson-containers
```

```shell
cd jetson-containers pip3 install -r requirements.txt
```

```shell
cd ./data && git clone https://github.com/LJ-Hao/MLC-LLM-on-Jetson-Nano.git && cd ..
```

## Install and run contiainer

### first step: install image

```shell
./run.sh --env HUGGINGFACE_TOKEN=<YOUR-ACCESS-TOKEN> $(./autotag mlc) /bin/bash -c 'ln -s $(huggingface-downloader meta-llama/Llama-2-7b-chat-hf) /data/models/mlc/dist/models/Llama-2-7b-chat-hf'
```

use ```sudo docker images``` to check wether the image is installed or not

![pir](https://files.seeedstudio.com/wiki/reComputer-Jetson/A608/docker_image.png)

### second step: Install Llama2-7b-chat-hf and Use MLC quantify the model

```shell
./run.sh $(./autotag mlc) \
python3 -m mlc_llm.build \
--model Llama-2-7b-chat-hf \
--quantization q4f16_ft \
--artifact-path /data/models/mlc/dist \
--max-seq-len 4096 \
--target cuda \
--use-cuda-graph \
--use-flash-attn-mqa
```

### Thrid step: Run and enter docker

```shell
./run.sh <YOUR IMAGE NAME>
#for me dustynv/mlc:51fb0f4-builder-r35.4.1 check result of first step
```

![pir](https://files.seeedstudio.com/wiki/reComputer-Jetson/A608/docker_run.png)

## Let's run it

### run Llama without quanifing without MLC LLM quantified

```shell
cd /data/MLC-LLM-on-Jetson && python3 Llama-2-7b-chat-hf.py
```

![pir](https://files.seeedstudio.com/wiki/reComputer-Jetson/A608/Llama-2-7b-chat-hf.png)

you can see without quanifing with MLC, Jetson Nano 16GB can load the model but cant not run.

### run Llama with quanifing with MLC LLM quantified

```shell
cd /data/MLC-LLM-on-Jetson && python3 Llama-2-7b-chat-hf-q4f16_ft.py
```

here is the result:
![pir](https://files.seeedstudio.com/wiki/reComputer-Jetson/A608/Llama-2-7b-chat-hf-q4f16_ft.png)

## Video of running Llama with MLC on Jetson Orin NX 16GB

> Embedded media: <https://www.youtube.com/embed/hyhh0Tc6g9Q>

## Project Outlook

In this project, we have demonstrated how to deploy a quantized version of Llama2-7B with MLC LLM on the Jetson Orin. With the powerful computing capabilities of the Jetson Orin, developers can build natural language processing applications that deliver high accuracy and low latency on edge devices. In the future, we will continue to explore the potential of deploying large language models on edge devices and develop more efficient and optimized deployment methods.
