#!coding:utf-8
"""
@author: wanqingfeng
"""
import cv2
import time

cam = cv2.VideoCapture(0)
i = 0
while True:
    (isCaptured,frame) = cam.read() #采集摄像头
    if(isCaptured):
        cv2.imshow("one",frame)

    # time.sleep(1)#每隔一秒采一帧
    if cv2.waitKey(1) & 0xFF == ord("s"): #按‘s’采集
        cv2.imwrite("calib/frame%d.jpg"%i,frame)
        i = i + 1
    elif cv2.waitKey(1) & 0xFF == ord("q"): #按‘q’结束采集
        break
cam.release()
cv2.destroyAllWindows()