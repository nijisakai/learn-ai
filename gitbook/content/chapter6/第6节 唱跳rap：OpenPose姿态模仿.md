# 第6节 唱跳rap：OpenPose姿态模仿

---

>卡内基梅隆大学（Carnegie Mellon University）的研究人员开发了一个身体跟踪系统，并命名为 OpenPose。该系统能实时跟踪人的肢体运动，包括手和脸部。它使用计算机视觉和机器学习技术来处理视频帧，甚至可以同时跟踪多个人的运动。

### 姿态检测的应用

对标准化体育动作进行建模，通过视频方式对运动员实时动作进行比对分析，可实现动作规范指标化。同时，还可以对运动员运动量进行统计分析，科学指导体育训练教学。

![dd](http://10391610.s21i.faiusr.com/2/ABUIABACGAAg0uz23QUokOKNpAEwywM4xgI.jpg)

![ddd](https://md.hass.live/niji/2019-06-09-13714448-f0f92028e2d41d01.gif)

![dddd](https://md.hass.live/niji/2019-06-09-Xnip2019-06-09_16-20-49.png)

### 小绿通过OpenPose模仿人类动作

#### 原理图

```sequence
摄像头-->PC/树莓派: WiFi/USB
PC/树莓派-->小绿: WiFi
Note right of PC/树莓派: OpenPose处理帧画面，计算姿态角度
PC/树莓派-->小绿: 发送处理结果
Note right of 小绿: 动作执行
```

#### 活动1：模仿视频文件中的人物动作

1.将小绿通电

2.在电脑上打开Anaconda Prompet，

```bash
conda activate learn-ai
cd C:\learn-ai\codes\chapter6\OpenPose
python OpenPoseVideo.py
```

**OpenPoseVideo.py部分代码：**

```python
……
//这部分指定输入源为文件夹下的`sample_video.mp4`
input_source = "sample_video.mp4"
cap = cv2.VideoCapture(input_source)
#cap = cv2.VideoCapture(0)
hasFrame, frame = cap.read()
……
//这部分将各个关节的姿态通过反三角函数转化为角度数据发送给舵机
POSE_PAIRS2 = [ { "servo":2,"pair":[2,3] ,"trim":0 ,"factor":-1 , 'angle':-1,'rangle':-1 } ,{ "servo":3,"pair": [5,6] , "trim": 180 ,"factor":-1 , 'angle':-1,'rangle':-1} ]
    POSE_PAIRS2.extend( [ { "servo":4,"pair":[3,4] ,"trim":0 ,"factor":-1 , 'angle':-1,'rangle':-1} ,{ "servo":5,"pair": [6,7] , "trim": 180 ,"factor":-1 , 'angle':-1,'rangle':-1} ])
    for idx,item in enumerate(POSE_PAIRS2):
        partA = item['pair'][0]
        partB = item['pair'][1]
        # print(points[partB])
        if points[partA] and points[partB]:
            angle = int(atan2( points[partB][0]-points[partA][0] , points[partB][1]-points[partA][1])/pi*180)
            print((item['servo'],angle))
            # angle = limitTo(angle,10,170)
            print((item['servo'],angle))
            item['rangle'] = angle
            if(item['servo'] %2 == 0 and angle > 90):
                angle = angle - 360 
            elif(item['servo'] %2 != 0 and angle < -90):
                angle = angle + 360
            angle = limitTo(angle,item['trim']-170,item['trim']-10)
            item['angle'] = (angle*item['factor'] + item['trim'])
```

3.运行代码后将会在电脑窗口中看到实时的姿态，同时小绿也会跟随视频中的人物姿态运动。

![微信截图_20190826202230](https://md.hass.live/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20190826202230.png)

#### 活动2：模仿实时姿态

1.将小绿通电

2.在电脑上打开Anaconda Prompet，

```bash
conda activate learn-ai
cd C:\learn-ai\codes\chapter6\OpenPose
python OpenPoseRealtimeVideo.py
```

3.运行代码后将会在电脑窗口中看到连接电脑的USB摄像头的实时画面。画面中的人物姿态将会实时的传递给小绿。试试挥挥手，看看小绿模仿的怎么样
