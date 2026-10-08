# Generative AI with reComputer-Jetson®

<a href="https://github.com/Seeed-Projects/jetson-examples">
        ![image](https://files.seeedstudio.com/wiki/reComputer/deploy-genai-on-jetson.png)
    </a>

[**Generative AI**](https://www.seeedstudio.com/edge-ai/generative-ai) is an artificial intelligence technology that can generate new data, such as images, text, or audio, by learning from existing data. **Nvidia Jetson** is an edge AI platform developed by NVIDIA, featuring high-performance processing capabilities and low-power design, suitable for various embedded and IoT devices. It supports deep learning, computer vision, and other AI applications, offering powerful computing capabilities and a rich set of development tools. The combination of Generative AI and Jetson enables efficient local real-time generation and inference on edge devices.

## Text Generation

Text generation is a technology that uses deep learning and large language model to generate natural language text. These models are trained on massive datasets, allowing them to learn the vocabulary, grammar, and semantic structure of language. They can produce fluent and coherent text, not only limited to answering questions or engaging in conversations but also including tasks like writing articles, creating stories, generating code, and translating languages. Here, we are deploying text generation algorithms on Jetson to create our own local chatbot.



            Local AI Assistant
            Local Voice Chatbot





                    ![image](https://files.seeedstudio.com/wiki/reComputer/Application/local-ai-assistant/ai-assistant.png)




                    ![image](https://files.seeedstudio.com/wiki/reComputer/Application/Local_Voice_Chatbot/workflow.png)





            Set up a local knowledge base on Jetson devices with ollama and AnythingLLM.
            Building a locally-operated voice chatbot with Nvidia Riva and Meta Llama2.



            [📚 Learn More](https://wiki.seeedstudio.com/local_ai_ssistant/)
            [📚 Learn More](https://wiki.seeedstudio.com/Local_Voice_Chatbot/)



## Image Generation

Image generation, by interpreting input text descriptions, allows models to produce high-quality images that match the descriptions. This technology has broad applications in fields such as artistic creation, advertising design, and game development, enabling the automated generation of visual content that meets user needs.



            Run a Local LLM Text-to-Image





                    ![image](https://files.seeedstudio.com/wiki/wiki-ranger/Contributions/Nvidia_Jetson_recomputer_LLM_texto-to-image/28_dreamshaperxl_image_result.png)





             Deploy the image generation model on Jetson and evaluate its inference performance.





                    [📚 Learn More](https://wiki.seeedstudio.com/How_to_run_local_llm_text_to_image_on_reComputer/)





## Audio Generation

Audio generation can produce high-quality, realistic audio, including speech, music, and sound effects, using neural networks. By training on extensive datasets, these models learn to replicate natural sound patterns and nuances, enabling applications such as speech synthesis, automated music composition, and sound effect creation.



            Speech Subtitle Generation
            Deploy Whisper on NVIDIA Jetson Orin





                    ![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/A608/recoder.gif)




                    ![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/A608/Real-Time-Whisper.gif)





              Speech Subtitle Generation on Jetson, which can offer real-time speech-to-subtitle services while avoiding information leakage on the internet.
             Deploying Whisper on the Jetson Orin to build robust, efficient STT applications.



            [📚 Learn More](https://wiki.seeedstudio.com/Real%20Time%20Subtitle%20Recoder%20on%20Nvidia%20Jetson/)


                    [📚 Learn More](https://wiki.seeedstudio.com/Edge/NVIDIA_Jetson/Application/Generative_AI/Whisper_on_Jetson_for_Real_Time_Speech_to_Text/)





## Multimodal Generation

Multimodal generation technology combines various forms of data, such as text, images, and sound, to create content that integrates multiple types of information. This technology uses deep learning models to process and fuse data from different modalities, resulting in more expressive and diverse content. For example, text-to-image models can generate corresponding images based on textual descriptions, while speech synthesis models can produce speech from text and simultaneously generate related images. Multimodal generation shows broad application prospects in virtual reality, augmented reality, and multimedia content creation.




                Run VLM on reComputer






                    ![image](https://files.seeedstudio.com/wiki/reComputer/Application/vlm/vlmgif.gif)






                  This wiki provides a tutorial on how to run VLM on reComputer J4012 Jetson Orin NX with Jetson Platform Services.






                    [📚 Learn More](https://wiki.seeedstudio.com/run_vlm_on_recomputer/)





## Retrieval Augmented Generation

RAG (Retrieval-Augmented Generation) is a technology that combines retrieval mechanisms with generation models. The RAG model not only uses a generative model to produce responses but also incorporates information retrieval techniques to enhance the accuracy and richness of the generated content by retrieving relevant information from large databases. This technology excels in applications such as question-answering systems, intelligent search, and content generation. By leveraging retrieved information, RAG models can generate more detailed and information-rich responses, thereby improving the quality and relevance of the generated content.




                Local AI Assistant


                Local RAG with LlamaIndex






                    ![image](https://files.seeedstudio.com/wiki/reComputer/Application/local-ai-assistant/ai-assistant.png)




                    ![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/A608/RAG-MLC-Jetson.gif)






                 Set up a local knowledge base on Jetson devices with ollama and AnythingLLM.


                 With this local RAG project, it can protect your data privacy and provide you with low-latency communication experience.






                    [📚 Learn More](https://wiki.seeedstudio.com/local_ai_ssistant/)




                    [📚 Learn More](https://wiki.seeedstudio.com/Local_RAG_based_on_Jetson_with_LlamaIndex/)





## Others




                Fine-tune LLM on Jetson


                Quantized LLM with MLC


                Zero-Shot Detection






                    ![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/Llama-Factory/run.gif)




                    ![image](https://files.seeedstudio.com/wiki/reComputer-Jetson/A608/MLC_LLM.gif)




                    ![image](https://files.seeedstudio.com/wiki/reComputer/Application/zero_shot_detection/fig1.gif)






                 Deploy Llama-Factory on Nvidia Jetson and use Llama-Factory to train a large language model.


                 Deploying the quantized Llama2-7B with MLC LLM on the Jetson Orin NX.


                 The Zero Shot Detection AI service exposes REST API endpoints to control stream input and objects to detect.






                    [📚 Learn More](https://wiki.seeedstudio.com/Finetune_LLM_on_Jetson/)




                    [📚 Learn More](https://wiki.seeedstudio.com/Quantized_Llama2_7B_with_MLC_LLM_on_Jetson/)




                    [📚 Learn More](https://wiki.seeedstudio.com/run_zero_shot_detection_on_recomputer/)






                Format Output with Langchain






                    ![image](https://files.seeedstudio.com/wiki/reComputer/Application/Format_LLM_Opt/format_llm_opt.gif)






                 Use Langchain to format the output of large language models and deploy it on edge computing devices.






                    [📚 Learn More](https://wiki.seeedstudio.com/How_to_Format_the_Output_of_LLM_Using_Langchain_on_Jetson/)





## Tech Support & Product Discussion

Thank you for choosing our products! We are here to provide you with different support to ensure that your experience with our products is as smooth as possible. We offer several communication channels to cater to different preferences and needs.

    <https://forum.seeedstudio.com/>
    <https://www.seeedstudio.com/contacts>

    <https://discord.gg/eWkprNDMU7>
    <https://github.com/Seeed-Studio/wiki-documents/discussions/69>
