# 第2节 Python计算机视觉编程

计算机视觉，英文 Computer Vision，简称 CV。计算机视觉是一门研究如何使机器 “看” 的科学，更进一步的说，就是指用摄影机和电脑代替人眼对目标进行识别、跟踪和测量等。

---

## 2.1 基于OpenCV的人脸识别操作

在树莓派上利用OpenCV进行相关操作，实现对给定图片中相关人脸的识别功能

### 硬件准备

- 树莓派、电源连接线
- 鼠标、键盘
- 显示屏

### 环境准备

1.首先我们需要安装Python3
打开[Pythong官方网站](https://www.python.org/downloads/source/)，并下载合适的Python版本

2.将树莓派开机并在命令行中安装OpenCV

```bash
sudo apt-get install libcv-dev
sudo apt-get install python-opencv
```

3.接着我们需要安装`numpy`库和`matlitlib`库，一个用于计算一个用于图像绘制

```bash
pip install numpy
sudo apt-get install python3-matplotlib
```

这样我们就完成了实验所需所有的环境配置

### 程序及操作

1.首先点击[这里](https://raw.githubusercontent.com/shantnu/Webcam-Face-Detect/master/haarcascade_frontalface_default.xml)下载一个 cascade file，并将其另存为*_haarcascade_frontalface_default.xml_*

2.创建一个后缀名为`*.py`的python文件 ( 可用我们之前安装的 Python3 打开 ) 并在文件中输入以下代码

```python
# Import OpenCV library
import cv2

# Load a cascade file for detecting faces
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml");

# Load image
# 需要更改 picture.jpeg 为自己图片的名称
image = cv2.imread('picture.jpeg')

# Convert into grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Look for faces in the image using the loaded cascade file
faces = faceCascade.detectMultiScale(gray, 1.2, 5)
for (x,y,w,h) in faces:
	# Create rectangle around faces
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,0),2)

# Create the resizeable window
# 需要更改 picture.jpeg 为自己图片的名称
cv2.namedWindow('picturex', cv2.WINDOW_NORMAL)

# Display the image
# 需要更改 picture.jpeg 为自己图片的名称
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

3.将 `cascade file`、`*.py`文件、以及我们所需要识别的图片发在同一路径下就像下图一样 ( 这保证了我们一会程序运行的确定性 )

![文件结构图](http://pic-learn-ai.oss-cn-beijing.aliyuncs.com/4.png)

4.运行程序
需要我们在该目录下打开命令行（可使用快捷键鼠标点击路径按F4实现）输入

```python
#filename.py是你保存的代码文件的名称
python3 filename.py
```

之后我们就可以看到我们所选择的的图片加载出来，并且其中的人物的脸部会用方框圈起来
