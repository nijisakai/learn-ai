# 第3节 Python计算机视觉编程

## 3.1 基于opencv的人脸识别操作

    在树莓派上利用opencv进行相关操作，实现对给定图片中相关人脸的识别功能

### 硬件准备

- 树莓派、电源连接线、鼠标、键盘、以及显示屏

### 环境准备

1.首先我们需要安装python3
在这一步里我们需要登陆python官网

> <https://www.python.org/downloads/source/>

并下载合适的python版本
2.将树莓派开机并在命令行中输入如下操作

>sudo apt-get install libcv-dev
sudo apt-get install python-opencv

这一步我们是完成opencv在树莓派上的安装，在安装后我们可以通过以下操作来导入opencv
>1、打开命令行并输入

     python3  
![12](图片/1.png)

>2、接着输入

```bash
import cv2
```

![12](图片/2.png)
>3、之后我们可以通过以下代码来检测我们所使用的opencv版本
![12](图片/3.png)

3.接着我们需要安装两个库 (numpy 和 matlitlib) 一个用于计算一个用于图像绘制
使用以下代码在命令行中进行安装

```bash
pip install numpy
sudo apt-get install python3-matplotlib
```

这样我们就完成了实验所需所有的环境配置

### 程序及操作

1.首先需要在下面的网址里下载一个 cascade file
<https://raw.githubusercontent.com/shantnu/Webcam-Face-Detect/master/haarcascade_frontalface_default.xml>

并将其另存为

*_haarcascade_frontalface_default.xml_*

2.创建一个 .py 的文件 ( 可用我们之前安装的 Python3 打开 ) 并在文件中输入以下代码

```python
# Import OpenCV library
import cv2

# Load a cascade file for detecting faces
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml");

# Load image
image = cv2.imread('picturex.jpeg')

# Convert into grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Look for faces in the image using the loaded cascade file
faces = faceCascade.detectMultiScale(gray, 1.2, 5)
for (x,y,w,h) in faces:
	# Create rectangle around faces
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,0),2)

# Create the resizeable window
cv2.namedWindow('picturex', cv2.WINDOW_NORMAL)

# Display the image
cv2.imshow('picturex', image)

# Wait until we get a key
k=cv2.waitKey(0)

# If pressed key is 's'
if k == ord('s'):
    # Save the image
    cv2.imwrite('convertedimage.jpg', image)
    # Destroy all windows
    cv2.destroyAllWindows()
# If pressed key is ESC
elif k == 27:
    # Destroy all windows
cv2.destroyAllWindows()
```

**_第8/15/23行的picturex是我们需要更改的图片名字_**

3.将 cascade file、.py文件、以及我们所需要识别的图片发在同一路径下就像下图一样 ( 这保证了我们一会程序运行的确定性 )
<center>

![12](图片/4.png)
</center>

4.运行程序
需要我们在该目录下打开命令行（可使用快捷键鼠标点击路径按F4实现）
在命令行中输入

```python
#filename.py是你保存的代码文件的名称
python3 filename.py
```

之后我们就可以看到我们所选择的的图片加载出来，并且其中的人物的脸部会用方框圈起来