#-*-coding:utf-8 -*-
from pyfirmata import Arduino, util
import time
import cv2
import  numpy as np
import serial
ser = serial.Serial()
ser.baudrate = 9600  # 设置波特率
#ser.port = 'COM4'  # for Windows 端口是COM4  查看端口方法 在资源管理器中查看 win+x，输入M，回车。
ser.port = '/dev/ttyUSB0' # for Linux 查看端口方法 ls /dev/ttyUSB*
print(ser)
ser.open()  # 打开串口
print(ser.is_open)  # 检验串口是否打开
# board = Arduino('COM3')

def duoji ():
    board.servo_config(13, 0, 255, 20)
    print("ceshi")
    time.sleep(0.2)
    board.servo_config(13, 0, 255, 255)
    time.sleep(0.2)
def arduino ():
    board.digital[13].write(0)  # 向io口13写入0
    time.sleep(0.1)
    board.digital[13].write(1)  # 向io口13写入1
    time.sleep(0.1)
    board.analog [13].write(100)

def detect_circle_demo ():
    video_capture = cv2.VideoCapture(0)
    while True:
        if not video_capture.isOpened():
            print('Unable to load camera.')
            break
        ret, img = video_capture.read()
        #img = cv2.pyrMeanShiftFiltering(img, 10, 25)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 灰度图像
        circles1 = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT , 1, 100, param1=100, param2=100, minRadius=50,maxRadius=200)
       # cv.HoughCircles(cimage, cv.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)
        try:  # 如果上一步没有检测到。执行try内容，就会报错。可以修改尝试看下。
            circles = circles1[0, :, :]  # 提取为二维
        except TypeError:
            print(u'未发现圆形物体！！')
        else:
            circles = np.uint16(np.around(circles))  # 四舍五入
            for i in circles[:]:
                cv2.circle(img, (i[0], i[1]), i[2], color=[0, 0, 0], thickness=2)  # 画圆
                cv2.circle(img, (i[0], i[1]), 2, color=[0, 255, 0], thickness=2)  # 画圆心
                cv2.putText(img, "center", (i[0] - 20, i[1] - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
                print(i[0],i[1])
                print(u"检测到圆形物体，开始分离！")
                
                ser.write(b"a")
                #print(ser.read(1))
                # 输出坐标
        # 显示视频
        cv2.imshow('Video', img)
        cv2.waitKey(10)
detect_circle_demo()