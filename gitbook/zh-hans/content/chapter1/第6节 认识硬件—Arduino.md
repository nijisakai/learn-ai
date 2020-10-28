# 第6节 认识硬件—Arduino

---

> 简介

### 内容提要

### Arduino UNO

   ![alt arduino](https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1581959664264&di=2551cfc0ee07302a8db66987fc49a378&imgtype=0&src=http%3A%2F%2Fimg.china-scratch.com%2Ftimg%2F180819%2F114J9B39-0.jpg)  

   Arduino UNO 上搭载一块Atmel公司生产的AVR单片机，名称为ATmega328P。详细信息如下表所示  

   |项目|参数
   |:-:|:-:|
   |名称|Arduino UNO (ATmega328P)|
   |工作电压|5V|
   |输入电压|7V~12V|
   |数字I/O引脚数量|14 Pin |
   |PWM通道|6 Pin|
   |模拟I/O引脚数量|6 Pin|
   |所有I/O口电流输出大小|20 mA|
   |Flash大小|32 KB|
   |SRAM|2 KB|
   |EEPROM|1 KB|
   |时钟速度|16 MHz|
   |板载LED灯控制引脚|13号数字I/O口|
   |程序下载接口|USB 标准B型口|
   |外部供电接口|5.2mm DC接口|
   |程序编码与编译环境|Arduino IDE (IDE:集成开发环境)|

   Arduino UNO 的各个接口和功能介绍，如下图所示：
   ![alt arduino](https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=2565738410,899497393&fm=26&gp=0.jpg)  

### 程序烧录过程

1. 在桌面上打开“Arduino IDE” (此集成开发环境已提前配置完整，直接使用即可)，如下图所示：  
![alt arduino ide](https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1581959664268&di=9cc5ddcfdcfcbb695ad6fc53d2aa9551&imgtype=0&src=http%3A%2F%2Fwww.uzzf.com%2Fup%2F2015-7%2F2015073111171442149.png)
2. 将Arduino UNO 通过USB线连接到电脑的USB口上，如下图：
   ![alt usb](http://q6c64umf6.bkt.clouddn.com/usb1.png)  
3. 通过Arduino IDE打开程序代码，如使13号接口连接的LED灯闪烁的程序：Blink  
   ![alt blink](http://q6c64umf6.bkt.clouddn.com/blink.png)  
4. 选择目标开发板：Arduino UNO,如下图：  
   ![alt board](http://q6c64umf6.bkt.clouddn.com/board.png)  
5. 选择开发板所在的物理端口，如下图：  
   ![alt port](http://q6c64umf6.bkt.clouddn.com/port.png)  
6. 点击下载按钮，Arduino IDE 开始编译源程序并把编译结果下载到开发板上；完成后，开发板上13号I/O口连接的LED会每隔一秒亮灭一次，如下图：  
   ![alt download](http://q6c64umf6.bkt.clouddn.com/port.png)

## 2. Arduino Nano

![alt arduino nano](https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=276959582,893697988&fm=26&gp=0.jpg)  

Arduino Nano 与Arduino UNO 同样搭载一块Atmel公司生产的AVR单片机，名称为ATmega328P。只是与Arduino UNO 相比，Arduino Nano在同样搭载了USB程序下载接口，更多一些的I/O口的前提下，体积要小的多，这就为需要小体积控制板的项目提供了更多选择。详细信息如下表所示  

   项目|参数
   :-: | :-:
   |名称|Arduino UNO (ATmega328P)|
   |工作电压|5V|
   |输入电压|7V~12V|
   |特殊接口|原生支持USB接口|
   |数字I/O引脚数量|22 Pin |
   |PWM通道|6 Pin|
   |模拟I/O引脚数量|6 Pin|
   |所有I/O口电流输出大小|40 mA|
   |Flash大小|32 KB|
   |SRAM|2 KB|
   |EEPROM|1 KB|
   |时钟速度|16 MHz|
   |板载LED灯控制引脚|13号数字I/O口|
   |程序下载接口|Micro-USB接口|
   |外部供电接口|5.2mm DC接口|
   |程序编码与编译环境|Arduino IDE (IDE:集成开发环境)|

注：Arduino Nano的程序烧写方法与Arduino UNO 相同。

## 3. Arduino Leonardo

![alt leonardo](https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1581965378734&di=50ff6606d57beebdbb56fd3bf2af85ec&imgtype=0&src=http%3A%2F%2Fwww.yahboom.com%2FPublic%2Fueditor%2Fphp%2Fupload%2Fimage%2F20170428%2F1493367817190630.jpg)  
Arduino Leonardo 是一个搭载ATmega32u4的8位AVR单片机的开发板，其上同样有与Arduino UNO 相同的I/O口，唯一不同的是，ATmega32u4单片机支持原生的USB接口，并且可以通过程序控制，来讲此USB接口模拟成各类电脑USB外设，如鼠标，键盘，游戏手柄等等。详细信息如下图表格所示：
|项目|参数|
:-:|:-:
|名称|Arduino Leonardo (ATmega32u4)|
|工作电压|5V|
|输入电压|7V~12V|
|数字I/O引脚数量|14 Pin |
|PWM通道|6 Pin|
|模拟I/O引脚数量|8 Pin|
|所有I/O口电流输出大小|40 mA|
|Flash大小|32 KB|
|SRAM|2 KB|
|EEPROM|1 KB|
|时钟速度|16 MHz|
|板载LED灯控制引脚|13号数字I/O口|
|程序下载接口|Mini-USB接口|
|外部供电接口|5.2mm DC接口|
|程序编码与编译环境|Arduino IDE (IDE:集成开发环境)|

注：Arduino Leonardo的程序烧写方法与Arduino UNO 相同
