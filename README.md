# Open Source Hardware - NVIDIA Jetson Baseboard
Copyright (c) [Seeed Studio](https://www.seeedstudio.com/). All rights reserved.

<div style={{textAlign:'center'}}><img src="https://files.seeedstudio.com/OSHW_Jetson/Jetson_Platform.png" style={{width:1200, height:'auto'}}/></div>

## Overview

This project contains the open hardware design files for the Seeed Studio's NVIDIA Jetson hardware series, including reComputer, ans reServer carrier boards based on **Jetson Nano, Jetson Xavier NX, and Jetson Orin**. 

It includes the BRD, DSN circuit design source files, and visualized PDF schematic files for the following five carrier boards: [reComputer industrial J201](https://www.seeedstudio.com/reComputer-Industrial-J2012-p-5685.html), [reComputer J202](https://www.seeedstudio.com/reComputer-J202-Carrier-Board-for-Jetson-Xavier-NX-p-5397.html), [reComputer J401](https://www.seeedstudio.com/reComputer-J401-Carrier-Board-for-Jetson-Orin-NX-Orin-Nano-p-5636.html), [reServer industrial J401](https://www.seeedstudio.com/reServer-industrial-J4012-p-5747.html), and [reServer J2032](https://www.seeedstudio.com/reServer-Jetson-20-1-H2-p-5337.html).


The design files were preapared in Cadence **Allegro 17.4**.

## Project structure 
The main directory contains subdirectories for reComputer and reServer hardware open-source files, a **LICENSE** file, and a **README** file. The subdirectories reComputer and reServer provide the **BRD**, **DSN** circuit design source files, and visualized **PDF** schematic files for the following five carrier boards. 

Specifically, 
- the **BRD** and **PDF** files are placed in the **/Layout** subdirectory, 
- the **DSN** files in the **/Schematic** subdirectory.

```markdown
├── reComputer Jetson baseboard
│
│ ├── reComputer industrial J201
│ │   ├── README.md
│ │   ├── Layout
│ │   │   └── reComputer Industrial J201_V1.2.brd
│ │   └── Schematic
│ │       ├── reComputer Industrial J201_V1.2.DSN
│ │       └── reComputer Industrial J201_V1.2.pdf
│ │
│ ├── reComputer J202 
│ │   ├── README.md
│ │   ├── Layout
│ │   │   └── reComputer J202_V1.0.brd
│ │   └── Schematic
│ │       ├── reComputer J202_V1.0.DSN
│ │       └── reComputer J202_V1.0.pdf
│ │
│ └── reComputer J401
│     ├── README.md
│     ├── Layout
│     │   └── reComputer J401_V1.0.brd
│     └── Schematic
│         ├── reComputer J401_V1.0.DSN
│         └── reComputer J401_V1.0.pdf
│
├── reServer Jetson baseboard
│ │
│ ├── reServer industrial J401
│ │   ├── README.md
│ │   ├── Layout
│ │   │   └── reServer Industrial J401 Carrier Board v11.brd
│ │   └── Schematic
│ │       ├── reServer Industrial J401 Carrier Board v11.DSN
│ │       └── reServer Industrial J401 Carrier Board v11.pdf
│ │
│ ├── reServer J2032
│     ├── README.md
│     ├── Layout
│     │   └── reServer J2032_V1.brd
│     └── Schematic
│         ├── reServer J2032_V1.DSN
│         └── reServer J2032 V1.pdf
│
├── README.md
├── LICENSE.md
```
## Documentation
For more information on the carrier board, please refer to the following links:
- **[Wiki]** [reComputer J202 carrier board](https://wiki.seeedstudio.com/reComputer_J2021_J202_Flash_Jetpack/);
- **[Wiki]** [reComputer J401 carrier board](https://wiki.seeedstudio.com/J401_carrierboard_Hardware_Interfaces_Usage/);
- **[Wiki]** [reComputer Industrial Getting Started](https://wiki.seeedstudio.com/reComputer_Industrial_Getting_Started/);
- **[Wiki]** [reServer Industrial Getting Started](https://wiki.seeedstudio.com/reServer_Industrial_Getting_Started/);
- **[Wiki]** [reServer J2032 Getting Started](https://wiki.seeedstudio.com/reServer_J2032_Getting_Started/);

- **[🛒Buy]** [reComputer industrial J201](https://www.seeedstudio.com/reComputer-Industrial-J2012-p-5685.html);
- **[🛒Buy]**[reComputer J202](https://www.seeedstudio.com/reComputer-J202-Carrier-Board-for-Jetson-Xavier-NX-p-5397.html);
- **[🛒Buy]**[reComputer J401](https://www.seeedstudio.com/reComputer-J401-Carrier-Board-for-Jetson-Orin-NX-Orin-Nano-p-5636.html);
- **[🛒Buy]**[reServer industrial J401](https://www.seeedstudio.com/reServer-industrial-J4012-p-5747.html);
- **[🛒Buy]**[reServer J2032](https://www.seeedstudio.com/reServer-Jetson-20-1-H2-p-5337.html);



## Customization 
Seeed Agile ODM Service empowers device makers and integrators with our customizable services tailored to their specific hardware needs. Learn more at **https://www.seeedstudio.com/odm**

### Seeed ODM Custom Design for NVIDIA Jetson includes:
- **Modify form factors;**
- **Image flashing;**
- **Customize logo**

## Licensing
This project is published under the [Apache-2.0](./LICENSE) license.