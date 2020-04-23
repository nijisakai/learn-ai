# 人工智能课程介绍

## [北京师范大学智慧学习研究院](http://sli.bnu.edu.cn/)

智慧学习研究院（Smart Learning Institute以下简称SLI）是北京师范大学下设的综合性科学研究、技术开发和教育教学实验平台。主要任务包括：在重点产品开发及项目研究的关键环节上取得实质性突破，形成可大规模推广的智慧学习解决方案；建构智慧学习理论，探索信息技术与教育双向融合的方法与途径，形成一批具有国际影响的学术成果；建立智慧学习实验区和实验校，发展基于大数据的教育教学研究模式；通过双聘机制和企业导师制，探索产学研结合的教育信息化高端人才培养机制。


## [元卓计划](http://yuanzhuo.bnu.edu.cn/page/about)

元卓计划由北京师范大学发起，旨在培养青少年利用原创算法解决真实问题的能力，建立产学研协同机制，推动人工智能企业科技成果向教育教学转化，助力我国成为世界主要人工智能创新中心。

## 概述

- 本项目包含一个[在线文档](https://course.playwithai.com)以及配套的教学材料（PPT、教案、学习单）。

- 包含6个有所关联、逐步递进的项目构成的章节。分别涉及物联网、机器人、机器视觉、语音识别和控制等内容。

- 包含背景知识学习、环境准备和资源下载部分。

本课程通过6个有所关联、逐步递进的章节，探究人工智能的基本原理，了解人工智能、机器学习基本概念，参与计算机视觉、语音技术等人工智能领域相关项目，利用人工智能解决学习和生活中的实际问题。

课程涉及人工智能基本概念、计算机视觉、语音技术、机器人等内容。通过一系列动手实验，制作小车和机器人，完成物体检测、自动追踪、无人驾驶、机器人姿态模仿、语音助手等项目。

课程包含详细的在线操作文档、配套代码、小车及机器人3D打印零件及全部硬件器材，学生无需自行准备任何设备，即可顺利完成全部项目。

完成课程学习后，将会对人工智能的基本概念有一定了解；对图像分类，目标检测，自然语言处理、语音识别等技术有直观体会；掌握开源硬件的基本操作，并通过开源硬件构建人工智能应用。

## 分章节介绍

### 第1章 基础知识

- 介绍：
学习者通过学习本章内容，将熟悉掌握一些必备的相关技能。如Python基础，Linux常见命令操作，开源硬件的基础操作等。为后续的项目学习打好基础。

![智能小白](https://md.hass.live/%E6%99%BA%E8%83%BD%E5%B0%8F%E7%99%BD.png)

### 第2章 人工智能体验

- 介绍：
通过本章内容，学生对人工智能的数学基础、概率论和博弈论、人工智能在图形图像和语言处理、电子游戏及其他领域的应用有感性认识。

![atari](https://md.hass.live/niji/2019-12-10-1.jpg)

![微信截图_20190717113637](https://md.hass.live/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20190717113637.png)

使用在线的积木编程（google blockly/scratch）来控制

![微信截图_20190826220833](https://md.hass.live/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20190826220833.png)

![微信截图_20190717113246](https://md.hass.live/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20190717113246.png)

- 涉及软硬件：
PC或树莓派（Raspberry Pi）或NVIDIA Jetson Nano

### 第3章 智能车“小白”

- 介绍：
主要使用ESP8266提供Web服务，来控制电机、舵机、传感器等，实现远程遥控、远程视频监控、巡线、避障、控制机械臂抓取等功能
可以通过积木编程的方式来对小车的功能进行编程
![微信截图_20190717105254](https://md.hass.live/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20190717105254.png)
![微信截图_20190717105447](https://md.hass.live/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20190717105447.png)
![微信截图_20190717105521](https://md.hass.live/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20190717105521.png)
![成果照片](https://md.hass.live/%E6%88%90%E6%9E%9C%E7%85%A7%E7%89%87.jpg)
![微信截图_20190717110028](https://md.hass.live/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20190717110028.png)
![微信截图_20190717110254](https://md.hass.live/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20190717110254.png)
- 涉及软硬件：
ESP8266，ESP32-CAM，小车套件（可3D打印），舵机，灰度传感器、超声波传感器等
自行开发的物联网控制平台，MIT App Inventor

### 第4章 自动追踪小车“大白”

- 介绍：
从机器视觉出发，让学生理解机器视觉的相关概念和原理，辨别OpenCV和深度学习的异同点。
使用OpenCV来处理视觉信号，并通过蓝牙或串口来将处理过的视觉信号发送给小车，从而实现物体追踪，人脸追踪，智能机械臂抓取等功能
学生通过使用Python，完成信息采集：爬虫、多文件处理；信息处理：训练采集的数据，形成分类器，从而让计算机视觉系统能够对特定的物体进行分辨
![第4章](https://md.hass.live/%E7%AC%AC4%E7%AB%A0.png)
- 涉及软硬件：
树莓派、Arduino、舵机、USB摄像头、小车套件、3D打印机、电磁传感器、蓝牙接收器
OpenCV、Python

### 第5章 无人驾驶小车“老白”

- 介绍：
采用深度学习的方式，通过采集无人驾驶的数据，并进行训练，来实现无人驾驶的功能
![微信图片_20190414123456](https://md.hass.live/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20190414123456.jpg)
![微信图片_20181028095310](https://md.hass.live/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20181028095310.jpg)
![微信图片_2018102809531022](https://md.hass.live/track.jpg)
- 涉及软硬件：
树莓派、摄像头、小车套件
Python

### 第6章 机器人“小绿”

- 介绍：
组装一个机器人，作为物联网的一个节点，实现多种物联网功能，包括网页遥控：通过自行开发的物联网平台来对它进行遥控；语音助手：可以通过自己训练的热词来进行唤醒、通过语音来控制机器人执行各种动作；控制其他设备：比如控制前几个章节的小车，读取各种传感器的数据等；人脸解锁：通过实时的人脸识别和红外线发射装置，实现人脸解锁，也可以通过Google Assistant、Siri、Alexa等远程控制；实时姿态模仿：通过单目摄像头拍摄实时画面，采用OpenPose姿态识别软件进行处理，将关节姿态数据通过蓝牙或串口传递给机器人，机器人进行实时的姿态模仿。
![第6章](https://md.hass.live/%E7%AC%AC6%E7%AB%A0.jpg)
![微信截图_20190717112931](https://md.hass.live/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20190717112931.png)
- 涉及软硬件：
树莓派、ESP8266、麦克风阵列、舵机、3D打印机、摄像头等
