# 人工智能课程文档-课程活动部分

 <font size=5>目录</font>

<!-- @import "[TOC]" {cmd="toc" depthFrom=2 depthTo=3 orderedList=false }-->
<!-- code_chunk_output -->

* [**环境准备**](#环境准备)
	* [Anaconda](#anaconda)
	* [VSCode](#vscode)
	* [CP2102驱动](#cp2102驱动)
	* [Arduino IDE.](#arduino-ide)
	* [其他](#其他)
	* [下载课程所需文件](#下载课程所需文件)
* [**Chapter 1 物联网与机器人**](#chapter-1-物联网与机器人)
* [**Part 1 使用esp8266开发板读取和控制传感器、舵机和电机**](#part-1-使用esp8266开发板读取和控制传感器-舵机和电机)
	* [Part 1.1 使用esp8266在网页上读取传感器数据](#part-11-使用esp8266在网页上读取传感器数据)
	* [Part 1.2 WiFi遥控小车](#part-12-wifi遥控小车)
	* [Part 1.3 使用esp8266通过WiFi控制机械臂舵机](#part-13-使用esp8266通过wifi控制机械臂舵机)
	* [Part 1.4 esp32网络摄像头与人脸识别](#part-14-esp32网络摄像头与人脸识别)
	* [Part 1.5 综合与进阶](#part-15-综合与进阶)
	* [尾声](#尾声)
* [**Part 2 物联网开源平台HomeAssistant创意应用**](#part-2-物联网开源平台homeassistant创意应用)
	* [Part 2.1 HomeAssistant安装](#part-21-homeassistant安装)
	* [Part 2.2 HomeAssistant控制esp8266彩色灯](#part-22-homeassistant控制esp8266彩色灯)
	* [Part 2.3 HomeAssistant进行人脸识别和语音播报](#part-23-homeassistant进行人脸识别和语音播报)
* [**Part 3 进阶项目-物联网机器人小绿**](#part-3-进阶项目-物联网机器人小绿)
	* [Part 3.1 组装一个小绿](#part-31-组装一个小绿)
	* [Part 3.2 让小绿开口说话](#part-32-让小绿开口说话)
	* [Part 3.3 让小绿听你指挥](#part-33-让小绿听你指挥)
	* [Part 3.4 使用Google Blockly来控制小绿](#part-34-使用google-blockly来控制小绿)
* [**Chapter 2 人工智能与机器人**](#chapter-2-人工智能与机器人)
* [**Part 1 人工智能算法相关案例体验**](#part-1-人工智能算法相关案例体验)
	* [Part 1.1 Tensorflow训练自定义图片分类器](#part-11-tensorflow训练自定义图片分类器)
	* [Part 1.2 使用RNN来生成古诗词](#part-12-使用rnn来生成古诗词)
	* [Part 1.3 训练一个简单的游戏AI（Deep Q Network）](#part-13-训练一个简单的游戏aideep-q-network)
	* [Part 1.4 使用进化算法来训练超级马里奥](#part-14-使用进化算法来训练超级马里奥)
* [**Part 2 自动追踪小车**](#part-2-自动追踪小车)
	* [Part 2.1 环境准备与硬件搭建](#part-21-环境准备与硬件搭建)
	* [Part 2.2 OpenCV机械臂自动抓取特定形状物体](#part-22-opencv机械臂自动抓取特定形状物体)
	* [Part 2.3 OpenCV分类器训练，让小车追踪特定物体](#part-23-opencv分类器训练让小车追踪特定物体)
* [**Part 3 无人驾驶小车**](#part-3-无人驾驶小车)
	* [Part 3.1 环境准备与硬件搭建](#part-31-环境准备与硬件搭建)
	* [Part 3.2 电机和摄像头驱动测试](#part-32-电机和摄像头驱动测试)
	* [Part 3.3 无人驾驶数据采集及训练](#part-33-无人驾驶数据采集及训练)
	* [Part 3.4 开始无人驾驶](#part-34-开始无人驾驶)

<!-- /code_chunk_output -->

## **环境准备**

环境准备相关所有相关软件，**请[点击这里](ftp://home.hass.live)来下载**  
所需的用户名和密码均为`sli`  
也可以选择在下方提供的官方网址下载  
推荐按顺序依次安装以下软件，以避免因依赖问题报错。

### Anaconda

Anaconda是一个Python环境管理软件。在Windows，Mac、Linux上均可以方便安装。  
下载链接：<https://www.anaconda.com/distribution>
![Xnip2019-04-30_10-37-45](https://md.hass.live/Xnip2019-04-30_10-37-45.png)
选择适合自己的操作系统，并选择Python 3.7版本。

#### 基本命令

> **创建环境**

```bash
# conda create -n 环境名字
例如：  
# conda create -n py27 python=2.7
表示创建一个名字为py27，运行python2.7的虚拟环境。  
后面的python=2.7是可选输入。  
不输入时默认环境是python3。
```

> **进入环境**

```bash
# conda activate 环境名字
例如：  
# conda activate py27
```

> **安装指定包**  

```bash
# conda install 包名  
例如：安装OpenCV
# conda install opencv
```

> **其他命令**  

```bash
退出环境
# conda deactivate 环境名字  
列出环境
# conda-env list
删除环境
# conda-env remove -n 环境名字
```

#### setup

1.下载安装Anaconda  
2.在开始菜单找到Anaconda Prompt并进入  
3.创建并进入环境 (python版本为默认的3.x)  
4.在新环境中安装TensorFlow和OpenCV（若电脑有独立显卡应安装GPU版本的TensorFlow）

```bash
# conda create -n myenv //创建一个名字为myenv的虚拟环境
# conda activate myenv //激活myenv虚拟环境
# conda install tensorflow  //无独立显卡的电脑使用这条命令
# conda install tensorflow-gpu  //有独立显卡的电脑使用这条命令
# conda install opencv //安装opencv
# conda install git //安装git命令
```

### VSCode

VSCode是微软出品的免费代码编辑软件。在Windows，Mac、Linux上均可以方便安装。  
下载链接：<https://code.visualstudio.com>

#### setup

1. 下载安装VSCode  
2. 安装插件“Settings Sync”  
![2019-04-29 21.49.44](https://md.hass.live/2019-04-29%2021.49.44.gif)
3. 输入`Shift` + `Alt` + `D`,输入GitHub Token和Gist Token([点击获取](http://lab.playwithai.com:8999/))，即可从服务端同步设置。免去自己配置的麻烦。

### CP2102驱动

这个驱动用于使用USB串口连接esp8266  
注意选择对应的操作系统和版本进行下载和安装
下载链接: <https://www.silabs.com/products/development-tools/software/usb-to-uart-bridge-vcp-drivers>

### Arduino IDE.

*[IDE.]:Integrated Development Environment,集成开发环境

Arduino IDE 是针对Arduino控制板的编程和下载平台。在Windows，Mac、Linux上均可以方便安装。  
Arduino项目文件的后缀是*.ino。项目文件应在与项目名相同的文件夹中。
下载链接：<https://www.arduino.cc/en/Main/Software>

#### setup

1. 下载安装Arduino IDE  
2. 在`文件`--`首选项`--`附加开发板管理器网址`一栏中输入<https://arduino.esp8266.com/stable/package_esp8266com_index.json>，重启IDE
![arduino-config-1](https://md.hass.live/arduino-config-1.png)
3. 在`工具`--`开发板`--`开发板管理器`中搜索esp8266,点击对应项进行安装  
![2019-04-29 22.10.50](https://md.hass.live/2019-04-29%2022.10.50.gif)
4. 打开链接<https://github.com/esp8266/arduino-esp8266fs-plugin/releases/tag/0.4.0>,选择.zip文件下载，将解压后的文件夹复制到`Arduino安装目录/tools`文件夹。然后重启IDE。
![arduino-config-2](https://md.hass.live/arduinoconfig2.png?imageView2/0/interlace/1/q/46|imageslim)
默认的路径应该是这样：`C:\Program Files (x86)\Arduino\tools\esp8266FS\tool\esp8266fs.jar`
如果安装成功，会在`工具`菜单下看到下图选项。
<center><img src=https://md.hass.live/Xnip2019-05-05_18-39-45.png?imageView2/0/interlace/1/q/46|imageslim></center>

5. 设置开发板和端口
<center><img src=https://md.hass.live/Xnip2019-05-05_16-49-07.png?imageView2/0/interlace/1/q/46|imageslim></center>

### 其他

路由器设置SSID名字为**AI**，密码为**raspberry**  
路由器管理地址设置为<https://192.168.0.1>或默认地址
Xshell（Windows）、FinalShell（macOS）、Google Chrome、VNC Viewer等

### 下载课程所需文件

macOS用户打开`终端`
Windows用户打开`Anaconda Prompt`  

macOS用户执行`git clone https://github.com/nijisakai/learn-ai.git ~/Desktop/ai/`  
文件被下载到桌面下面的ai文件夹

Windows用户执行`git clone https://github.com/nijisakai/learn-ai.git C:/ai`  
文件被下载到C盘根目录下面的ai文件夹

---

## **Chapter 1 物联网与机器人**

    本章内容是关于使用可编程的开源硬件，将功能点进行分解，并最终实现综合项目。
    主要包括
     1. 使用物联网开发板来读取和控制传感器、灯和舵机等设备
     2. 安装和配置物联网平台，实现语音控制和人脸解锁
     3. 自主设计制作一个融合了多种功能的基于3D打印物联网机器人或小车。

## **Part 1 使用esp8266开发板读取和控制传感器、舵机和电机**

    esp8266是一个价格低廉的开发板，包含WiFi模块和GPIO，可以连接传感器、舵机、马达等各种设备。使用Arduino IDE进行开发编程。可通过网络、串口和蓝牙等多种方式进行通信。

### Part 1.1 使用esp8266在网页上读取传感器数据

    这部分让你熟悉操作esp8266的步骤。是第一章的基础。
    包括功能提出和实现，硬件连接，上传的参数调节和html文件在本地服务器中的打开，传感器数据的实时呈现等。
    这部分主要包括两种传感器的读取，为温湿度传感器和超声波传感器。

#### **硬件部分**

##### 硬件清单

* esp8266主板
* 温湿度传感器（型号为DHT11或DHT22）
* 超声波传感器（型号为HC-SR04）
* 杜邦线、数据线

##### 硬件连接

<center><img src=https://md.hass.live/Xnip2019-05-05_11-52-46.png?imageView2/0/interlace/1/q/46|imageslim></center>

<center><img src=https://md.hass.live/Xnip2019-05-05_12-02-00.png?imageView2/0/interlace/1/q/46|imageslim></center>

#### **算法及程序**

##### 操作步骤

1. 打开`ai`文件夹，打开路径`chapter1/part1/esp8266_projects/esp8266_dht11_https`
2. 将esp8266通过数据线连接到电脑
3. 使用Arduino IDE打开文件`esp8266_dht11_https.ino`
4. 记得把前面的[环境准备](#setup-2)部分再次确认，将环境正确配置，然后点击上传按钮进行上传

<center><img src=https://md.hass.live/Xnip2019-05-05_17-24-20.png?imageView2/0/interlace/1/q/46|imageslim></center>

5. 打开[路由器管理地址](http://192.168.0.1)，esp8266此时应该已经加入到了局域网中，查看esp8266获取到的路由器地址。  

6. 在浏览器中打开esp8266获取到的局域网地址，查看温湿度传感器的读数。

7. 连接另一个esp8266开发板，打开路径`chapter1/part1/esp8266_projects/esp8266_ultrasonic_https`,再次执行2-6步骤来使用超声波传感器。

##### 代码详解

* 温湿度传感器

```arduino {.line-numbers}
//两个反斜杠代表单行注释，这后面的文字不会被执行

/*
  被星号和反斜杠包围的部分可以进行多行注释
*/

/*使用多行注释符

  Arduino程序包含了两个主要的方法，分别是
  void setup()和void loop()
  方法后面写一对{},在这里面写方法的具体内容。看起来像是这样：
  void setup(){
    自己规定的语句
    自己规定的语句
    自己规定的语句
  }
  void loop(){
    自己规定的语句
    自己规定的语句
    自己规定的语句
  }
*/


//使用 #include来引用一些附加的功能。
#include <esp8266WiFi.h>
#include <esp8266WebServer.h>
#include "DHT.h"




/////////////////////////////////////////////
////////////////下面的部分请你配置//////////////
/////////////////////////////////////////////

// 1️⃣选择使用哪一种DHT传感器。通过去掉前面的注释符来使语句生效
#define DHTTYPE DHT11   // DHT 11
//#define DHTTYPE DHT21   // DHT 21 (AM2301)
//#define DHTTYPE DHT22   // DHT 22  (AM2302), AM2321

// 2️⃣把引号里的内容替换为自己路由器的用户名和密码
const char* ssid = "AI";  // 输入路由器用户名
const char* password = "raspberry";  //输入路由器密码

// 3️⃣把DHT传感器的Data接口连接到D8。此处与硬件连线对应即可
uint8_t DHTPin = D8;

// 4️⃣默认为80端口，如果改为其他端口，访问的时候在最后加上（:端口名）
esp8266WebServer server(80);

/////////////////////////////////////////////
////////////////上面的部分请你配置//////////////
/////////////////////////////////////////////

// 初始化你连接的DHT传感器
DHT dht(DHTPin, DHTTYPE);
//定义两个float变量来读取温湿度
float Temperature; //温度
float Humidity; //湿度


//开始最后的准备工作
void setup() {
  Serial.begin(115200);
  delay(100);
  
  pinMode(DHTPin, INPUT);
  dht.begin();

  Serial.println("Connecting to ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);

  //检查连接是否正常
  while (WiFi.status() != WL_CONNECTED) {
  delay(1000);
  Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected..!");
  Serial.print("Got IP: ");  Serial.println(WiFi.localIP());

  server.on("/", handle_OnConnect);
  server.onNotFound(handle_NotFound);

  server.begin();
  Serial.println("http server started");
}

void handle_OnConnect() {
  Temperature = dht.readTemperature();
  Humidity = dht.readHumidity();
  server.send(200, "text/html", SendHTML(Temperature,Humidity));
}

void handle_NotFound(){
  server.send(404, "text/plain", "Not found");
}

String SendHTML(float Temperaturestat,float Humiditystat){
  String ptr = "<!DOCTYPE html> <html>\n";
  ptr +="<head><meta charset=\"UTF-8\"><meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0, user-scalable=no\">\n";
  ptr +="<title>esp8266 DHT11</title>\n";

  ptr +="<script>\n";
  ptr +="setInterval(loadDoc,200);\n";
  ptr +="function loadDoc() {\n";
  ptr +="var xhttps = new XMLhttpsRequest();\n";
  ptr +="xhttps.onreadystatechange = function() {\n";
  ptr +="if (this.readyState == 4 && this.status == 200) {\n";
  ptr +="document.getElementById(\"webpage\").innerHTML =this.responseText}\n";
  ptr +="};\n";
  ptr +="xhttps.open(\"GET\", \"/\", true);\n";
  ptr +="xhttps.send();\n";
  ptr +="}\n";
  ptr +="</script>\n";
  ptr +="</head>\n";
  ptr +="<body>\n";
  ptr +="<div id=\"webpage\">\n";

  ptr +="<p>温度: ";
  ptr +=(int)Temperaturestat;
  ptr +="°C</p>";
  ptr +="<p>湿度: ";
  ptr +=(int)Humiditystat;
  ptr +="%</p>";
  
  ptr +="</div>\n";
  ptr +="</body>\n";
  ptr +="</html>\n";
  return ptr;
}

//所有准备工作就绪，开始工作
void loop() {
  server.handleClient();
}
```

* 超声波传感器

```arduino {.line-numbers}
#include <Arduino.h>
#include <esp8266WiFi.h>
#include <esp8266WiFiMulti.h>
#include <esp8266httpsClient.h>
#include <esp8266WebServer.h>
// utlrasonic pinout
#define ULTRASONIC_TRIG_PIN     5   // pin TRIG to D1
#define ULTRASONIC_ECHO_PIN     4   // pin ECHO to D2

const char* wifi_ssid = "AI";             // SSID
const char* wifi_password = "raspberry";         // WIFI
esp8266WebServer server(80);
esp8266WiFiMulti WiFiMulti;

void setup() {
  Serial.begin(115200);
  Serial.println("*****************************************************");
  Serial.println("********** Program Start : Connect Ultrasonic HC-SR04 + esp8266 to AskSensors over http");
  Serial.println("Wait for WiFi... ");
  Serial.print("********** connecting to WIFI : ");
  Serial.println(wifi_ssid);
  WiFi.begin(wifi_ssid, wifi_password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("-> WiFi connected");
  Serial.println("-> IP address: ");
  Serial.println(WiFi.localIP());
  // ultraonic setup
  pinMode(ULTRASONIC_TRIG_PIN, OUTPUT);
  pinMode(ULTRASONIC_ECHO_PIN, INPUT);
  server.on("/", handle_OnConnect);
  server.onNotFound(handle_NotFound);
  server.begin(); 
}

void handle_OnConnect() {
  long duration, distance;
  digitalWrite(ULTRASONIC_TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(ULTRASONIC_TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(ULTRASONIC_TRIG_PIN, LOW);
  duration = pulseIn(ULTRASONIC_ECHO_PIN, HIGH);
  distance = (duration/2) / 29.1;
  server.send(200, "text/html", SendHTML(distance));
}

void handle_NotFound(){
  server.send(404, "text/plain", "Not found");
}

String SendHTML(long distance){
  String ptr = "<!DOCTYPE html> <html>\n";
  ptr +="<head><meta charset=\"UTF-8\"><meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0, user-scalable=no\">\n";
  ptr +="<title>esp8266 DHT11</title>\n";

  ptr +="<script>\n";
  ptr +="setInterval(loadDoc,200);\n";
  ptr +="function loadDoc() {\n";
  ptr +="var xhttps = new XMLhttpsRequest();\n";
  ptr +="xhttps.onreadystatechange = function() {\n";
  ptr +="if (this.readyState == 4 && this.status == 200) {\n";
  ptr +="document.getElementById(\"webpage\").innerHTML =this.responseText}\n";
  ptr +="};\n";
  ptr +="xhttps.open(\"GET\", \"/\", true);\n";
  ptr +="xhttps.send();\n";
  ptr +="}\n";
  ptr +="</script>\n";
  ptr +="</head>\n";
  ptr +="<body>\n";
  ptr +="<div id=\"webpage\">\n";
  
  ptr +="<p>距离: ";
  ptr +=(float)distance;
  ptr +="厘米</p>";

  ptr +="</div>\n";
  ptr +="</body>\n";
  ptr +="</html>\n";
  return ptr;
}


void loop() {
  server.handleClient();
}
```

### Part 1.2 WiFi遥控小车

    使用esp8266，通过网页端发送命令，遥控一辆小车。

#### **硬件部分**

##### 硬件清单

* esp8266主板
* 电机扩展板 esp12E Motor Shield
* 小车套件(3D打印的底盘和夹层，电机，车轮，铜柱等)
* 杜邦线，数据线

##### 硬件连接

<center><img src=https://md.hass.live/Xnip2019-05-05_11-51-26.png?imageView2/0/interlace/1/q/46|imageslim></center>

#### **算法及程序**

##### 操作步骤

1. 打开`ai`文件夹，打开路径`chapter1/part1/esp8266_projects/esp8266_wificar_https`
2. 将esp8266通过数据线连接到电脑
3. 使用Arduino IDE打开文件`esp8266_wificar_https.ino`
4. 记得把前面的[环境准备](#setup-2)部分再次确认，将环境正确配置，然后点击上传按钮进行上传

<center><img src=https://md.hass.live/Xnip2019-05-05_17-24-20.png></center>

5. 点击`工具`菜单，选择`ESP8266 Sketch Data Upload`,会自动将项目目录下的data文件夹上传到esp8266开发板上。

6. 打开[路由器管理地址](http://192.168.0.1)，esp8266此时应该已经加入到了局域网中，查看esp8266获取到的路由器地址。  

7. 将esp8266与电脑连接断开，连接到移动电源上。

8. 在浏览器中打开esp8266获取到的局域网地址，通过点击上下左右按钮或键盘的光标键来控制小车。

##### 代码详解

* WiFi小车程序

```arduino {.line-numbers}
#include <esp8266WiFi.h>
#include <WiFiClient.h>
#include <esp8266WebServer.h>
#include <esp8266mDNS.h>
#include <FS.h>
#define Motor_AE D1      //Motor A/B,E enable,D Direction
#define Motor_AD D3

#define Motor_BE D2
#define Motor_BD D4

#define R_AHEAD HIGH
#define L_AHEAD LOW

String command;

esp8266WebServer server(80);

const int led = 13;

void carInit(){  
  pinMode(Motor_AE, OUTPUT);
  pinMode(Motor_AD, OUTPUT);
  pinMode(Motor_BE, OUTPUT);
  pinMode(Motor_BD, OUTPUT);

  Serial.begin(115200);
  Serial.println("Car begin");
  }
void goAhead(){
      digitalWrite(Motor_AE, HIGH);
      digitalWrite(Motor_AD, L_AHEAD);
      digitalWrite(Motor_BE, HIGH);
      digitalWrite(Motor_BD, R_AHEAD);
  }

void goBack(){
      digitalWrite(Motor_AE, HIGH);
      digitalWrite(Motor_AD, !L_AHEAD);
      digitalWrite(Motor_BE, HIGH);
      digitalWrite(Motor_BD, !R_AHEAD);
  }

void goRight(){
      digitalWrite(Motor_BE, LOW);
      digitalWrite(Motor_AE, HIGH);
      digitalWrite(Motor_AD, L_AHEAD);
  }

void goLeft(){
      digitalWrite(Motor_BE, HIGH);
      digitalWrite(Motor_AE, LOW);
      digitalWrite(Motor_BD, R_AHEAD);
  }

void stopRobot(){  
      digitalWrite(Motor_AE, LOW);
      digitalWrite(Motor_BE, LOW);
  }

void handleNotFound(){
  digitalWrite(led, 1);
  String message = "File Not Found\n\n";
  message += "URI: ";
  message += server.uri();
  message += "\nMethod: ";
  message += (server.method() == https_GET)?"GET":"POST";
  message += "\nArguments: ";
  message += server.args();
  message += "\n";
  for (uint8_t i=0; i<server.args(); i++){
    message += " " + server.argName(i) + ": " + server.arg(i) + "\n";
  }
  server.send(404, "text/plain", message);
  digitalWrite(led, 0);
}

void setup(void){
  carInit();
  SPIFFS.begin();

  uint8_t mac[WL_MAC_ADDR_LENGTH];
  WiFi.softAPmacAddress(mac);
  String macID = String(mac[WL_MAC_ADDR_LENGTH - 2], HEX) + String(mac[WL_MAC_ADDR_LENGTH - 1], HEX);
  macID.toUpperCase();

  String AP_NameString = "Wifi Car - " + macID;

  char AP_NameChar[AP_NameString.length() + 1];
  memset(AP_NameChar, 0, AP_NameString.length() + 1);

  for (int i = 0; i < AP_NameString.length(); i++)
    AP_NameChar[i] = AP_NameString.charAt(i);

const char* ssid = "AI";
const char* password = "raspberry";
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  Serial.println("");

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.print("Connected to ");
  Serial.println(ssid);
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
  if (MDNS.begin("esp8266")) {
    Serial.println("MDNS responder started");
  }


  //server.on("/", handleRoot);
  server.serveStatic("/", SPIFFS, "/index.html");

  server.on("/get", [](){
    String uri = server.uri();
    Serial.println(uri);
    command = server.arg("command");
    if(command == "forward")
      goAhead();
    else if(command == "backward")
      goBack( );
    else if(command == "left")
      goLeft();
    else if(command == "right")
       goRight();
    else if(command == "stop")
       stopRobot();
    Serial.println(command);
//    setCorlor(red.toInt(),green.toInt(),blue.toInt());
    server.send(200, "text/plain", String("set to ")+command);
  });

  server.onNotFound(handleNotFound);

  server.begin();
  Serial.println("http server started");
}

void loop(void){
  server.handleClient();
}
```

### Part 1.3 使用esp8266通过WiFi控制机械臂舵机

    使用esp8266，通过网页端发送命令，控制多个舵机。

#### **硬件部分**

##### 硬件清单

* esp8266主板
* 舵机
* 杜邦线、数据线
* 机械臂3D打印源文件和零件

##### 硬件连接

<center><img src=https://md.hass.live/Xnip2019-05-05_11-57-01.png?imageView2/0/interlace/1/q/46|imageslim></center>
<center>此处表示舵机连接到了D0口，最多可以连9个舵机（D0-D9）<br>
<font color=orange>黄色</font>-信号D<br>
<font color=red>红色</font>-正极V<br>
<font color=brown>棕色</font>-负极G<br>
</center>

#### **算法及程序**

##### 操作步骤

1. 打开`ai`文件夹，打开路径`chapter1/part1/esp8266_projects/esp8266_servoarm_https`
2. 将esp8266通过数据线连接到电脑
3. 使用Arduino IDE打开文件`esp8266_servoarm_https.ino`
4. 记得把前面的[环境准备](#setup-2)部分再次确认，将环境正确配置，然后点击上传按钮进行上传

<center><img src=https://md.hass.live/Xnip2019-05-05_17-24-20.png></center>

5. 点击`工具`菜单，选择`ESP8266 Sketch Data Upload`,会自动将项目目录下的data文件夹上传到esp8266开发板上。

6. 打开[路由器管理地址](http://192.168.0.1)，esp8266此时应该已经加入到了局域网中，查看esp8266获取到的路由器地址。  

7. 将esp8266与电脑连接断开，连接到移动电源上。

8. 在浏览器中打开esp8266获取到的局域网地址，通过拖动滑块来控制机械臂。

##### 代码详解

* WiFi机械臂程序

```arduino {.line-numbers}
#include <esp8266WiFi.h>
#include <FS.h>
#include <Servo.h>
#include "server.h"

const char* WIFI_SSID = "AI";
const char* WIFI_PASSWORD = "raspberry";

Servo servos[12];
uint8_t servo_pins[12] = {D0,D1,D2,D3,D4,D5,D6,D7,D8,D9,D10,D11};
uint8_t count = 12;
void setAngle(uint8_t di,uint8_t vi){
  if(di< 12 && vi < 180)
    servos[di].write(vi);
}
void attachServos(){
  for (uint8_t i = 0; i < count; ++i){
    servos[i].attach(servo_pins[i]);
  }
}

void detachServos(){
  for (uint8_t i = 0; i < count; ++i){
    servos[i].detach();
  }  
}

void handleNotFound(){
  String message = "File Not Found\n\n";
  message += "URI: ";
  message += server.uri();
  message += "\nMethod: ";
  message += (server.method() == https_GET)?"GET":"POST";
  message += "\nArguments: ";
  message += server.args();
  message += "\n";
  for (uint8_t i=0; i<server.args(); i++){
    message += " " + server.argName(i) + ": " + server.arg(i) + "\n";
  }
  server.send(404, "text/plain", message);
}

void setup() {
  // init the serial
  Serial.begin(115200);
  Serial.println();
  Serial.println("Server initial");
  //init the server
  SPIFFS.begin();
      Serial.println("SPIFFS begin");
  attachServos();
    Serial.println("Servos attached");
  server.serveStatic("/", SPIFFS, "/index.html");
  server.on("/set-servo", [](){
    String uri = server.uri();
    Serial.println(uri);
    String di = server.arg("di");
    String vi = server.arg("vi");
    Serial.println("di="+di+" vi="+vi);
    setAngle(di.toInt(),vi.toInt());
    server.send(200, "text/plain", String("set to ")+"di="+di+" vi="+vi);
  });
  server.onNotFound(handleNotFound);
  server.begin();
  Serial.println("http server started");
  

  // init the WiFi connection
  Serial.println();
  Serial.println();
  Serial.print("INFO: Connecting to ");
  WiFi.mode(WIFI_STA);
  Serial.println(WIFI_SSID);
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("INFO: WiFi connected");
  Serial.print("INFO: IP address: ");
  Serial.println(WiFi.localIP());

}

void loop() {
  server.handleClient();
}
```

### Part 1.4 esp32网络摄像头与人脸识别

    esp32是esp8266的升级版本。拥有更强的处理能力，能够很好的处理实时视频和音频等数据。通过本部分来为小车增加实时视频的功能。  
    也许，你会希望在小车上装一个摄像头，这样就可以身临其境的遥控它了。

#### **硬件部分**

##### 硬件清单

* esp8266主板
* 舵机
* 杜邦线、数据线
* 机械臂3D打印源文件和零件

##### 硬件连接

<center><img src=https://md.hass.live/404.gif></center>

#### **算法及程序**

##### 操作步骤

1. 打开`ai`文件夹，打开路径`chapter1/part1/
2. TBC

##### 代码详解

* 程序

```arduino {.line-numbers}
do something
```

### Part 1.5 综合与进阶

    试着把前面的功能整合到一个小车上，并在一个界面上对它们进行读取和控制。

#### **参考代码**

* [传感器+小车+机械臂+摄像头](下载链接)

#### **抓取大赛**

    每小组为一个队伍，按照规则比赛抓取物品

##### 比赛规则

* sector 1
* sector 2
* sector 3

### 尾声

  通过前面的例子，你已经可以使用无线网络的方式来让esp8266读取传感器数据，控制简单的电机，查看网络摄像头等。其实这些已经是物联网的雏形。  

  在后面的章节里，结合强大的人工智能，你的小车会愈发强大。  
  通过语音技术，让小车听懂你的指令
  通过计算机视觉，让机械臂自动识别和抓取特定物体
  通过深度学习，让小车自动追踪特定物体，以及无人驾驶

---

## **Part 2 物联网开源平台HomeAssistant创意应用**

    Home Assistant是一个开源的物联网平台，兼容各种物联网协议。可以方便的接入和控制各种设备。
    这一部分主要在树莓派（Raspberry Pi）上面进行。
    树莓派是运行Linux操作系统的微型卡片电脑，拥有GPIO端口与其他硬件通信，也具有HDMI，USB端口连接显示设备等。
    树莓派的操作系统在SD卡上，分发给同学的SD卡默认安装了所有的环境和依赖，相关的文档在桌面上。

### Part 2.1 HomeAssistant安装

本课程采用[Docker](https://baike.baidu.com/item/Docker/13344470?fr=aladdin)方式进行安装

#### **硬件部分**


#### **算法及程序**

### Part 2.2 HomeAssistant控制esp8266彩色灯

    简单的项目描述

#### **硬件部分**

#### **算法及程序**

### Part 2.3 HomeAssistant进行人脸识别和语音播报

    简单的项目描述

#### **硬件部分**

#### **算法及程序**

---

## **Part 3 进阶项目-物联网机器人小绿**

    简介

### Part 3.1 组装一个小绿

    简单的项目描述

#### **硬件部分**

#### **算法及程序**

### Part 3.2 让小绿开口说话

    简单的项目描述

#### **硬件部分**

#### **算法及程序**

### Part 3.3 让小绿听你指挥

    简单的项目描述

#### **硬件部分**

#### **算法及程序**

### Part 3.4 使用Google Blockly来控制小绿

    简单的项目描述

#### **硬件部分**

#### **算法及程序**

---

## **Chapter 2 人工智能与机器人**

    这一部分包括……

## **Part 1 人工智能算法相关案例体验**

    介绍

### Part 1.1 Tensorflow训练自定义图片分类器

    简单的项目描述

#### **硬件部分**

#### **算法及程序**

### Part 1.2 使用RNN来生成古诗词

    简单的项目描述

#### **硬件部分**

#### **算法及程序**

### Part 1.3 训练一个简单的游戏AI（Deep Q Network）

    简单的项目描述

#### **硬件部分**

#### **算法及程序**

### Part 1.4 使用进化算法来训练超级马里奥

    简单的项目描述

#### **硬件部分**

#### **算法及程序**

---

## **Part 2 自动追踪小车**

    项目介绍

### Part 2.1 环境准备与硬件搭建

    简单的项目描述

#### **硬件部分**

#### **算法及程序**

### Part 2.2 OpenCV机械臂自动抓取特定形状物体

    使用OpenCV来识别圆形物体，若识别到则发送串口指令给Arduino。Arduino控制机械臂进行抓取。

#### **硬件部分**

#### **算法及程序**

### Part 2.3 OpenCV分类器训练，让小车追踪特定物体

    通过拍照、爬虫等方式获取待训练图片，使用python进行简单的文件处理，用OpenCV训练后，可实现对特定物体的识别和追踪。

#### **硬件部分**

#### **算法及程序**

---

## **Part 3 无人驾驶小车**

    这部分基于树莓派以及一些开源软件构建。
    树莓派从摄像头模块获取输入，然后通过无线方式发送获得的图像数据到电脑，电脑通过之前训练好的神经网络对输入的图像数据预测小车接下来的动作，然后发送这些预测动作的控制指令到树莓派控制小车的程序中。小车根据这些获得的指令实现自动驾驶

### Part 3.1 环境准备与硬件搭建

    需要安装一些Python库并正确连接小车

#### **硬件部分**

##### 硬件清单

* 树莓派
* 树莓派电机扩展板
* 摄像头
* 小车套件

##### 硬件连接

<center><img src=https://md.hass.live/niji/2019-05-07-Xnip2019-05-07_15-41-17.png?imageView2/0/interlace/1/q/46|imageslim></center>

#### **算法及程序**

##### 操作步骤

1. 打开`ai`文件夹，打开路径`chapter2/part3/`
2. 打开终端，执行以下命令

```bash
sudo apt update
sudo apt install
```

### Part 3.2 电机和摄像头驱动测试

    测试软硬件环境的安装是否正确

#### **算法及程序**

##### 操作步骤

1. 打开`ai`文件夹，打开路径`chapter2/part3/`
2. 打开终端，执行以下命令

```bash
sudo apt update
sudo apt install
```

### Part 3.3 无人驾驶数据采集及训练

    搭建起车道，然后运行相应的收集数据的程序，按下笔记本的方向控制小车行驶，每按一次方向键，程序就会记录下一帧相应的图像。让小车平均遍历自动驾驶中可能出现的各种情况，按‘q‘退出数据采集，然后再运行相应的模型训练程序训练自动驾驶神经网络

#### **硬件部分**

##### 硬件清单

* 树莓派
* 树莓派电机扩展板
* 摄像头
* 小车套件

##### 硬件连接

<center><img src=https://md.hass.live/404.gif?imageView2/0/interlace/1/q/46|imageslim></center>

#### **算法及程序**

##### 操作步骤

1. 打开`ai`文件夹，打开路径`chapter2/part3/`
2. 打开终端，执行以下命令

```bash
sudo apt update
sudo apt install
```

### Part 3.4 开始无人驾驶

    根据训练好的神经网络模型，现在我们可以实现自动驾驶了

#### **算法及程序**

##### 操作步骤

1. 打开`ai`文件夹，打开路径`chapter2/part3/`
2. 打开终端，执行以下命令

```bash
sudo apt update
sudo apt install
```