#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  	appCam.py
#  	based on tutorial ==> https://blog.miguelgrinberg.com/post/video-streaming-with-flask
# 	PiCam Local Web Server with Flask
# MJRoBot.org 19Jan18
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
from Adafruit_MotorHAT.Adafruit_PWM_Servo_Driver import PWM
from flask import Flask, render_template, Response
import time
# Raspberry Pi camera module (requires picamera package)
from camera_pi import Camera

import RPi.GPIO as GPIO
GPIO.setwarnings(False)

# create a socket and bind socket to the host
#client_socket = socket(AF_INET, SOCK_STREAM)
#client_socket.connect(('localhost', 8002))

def measure():
    """
    measure distance
    """
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    start = time.time()

    while GPIO.input(GPIO_ECHO)==0:
        start = time.time()

    while GPIO.input(GPIO_ECHO)==1:
        stop = time.time()

    elapsed = stop-start
    distance = (elapsed * 34300)/2

    return distance

def measure1():
    """
    measure distance
    """
    GPIO.output(GPIO_TRIGGER1, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER1, False)
    start = time.time()

    while GPIO.input(GPIO_ECHO1)==0:
        start = time.time()

    while GPIO.input(GPIO_ECHO1)==1:
        stop = time.time()

    elapsed = stop-start
    distance1 = (elapsed * 34300)/2

    return distance1

# referring to the pins by GPIO numbers
GPIO.setmode(GPIO.BCM)

# define pi GPIO
GPIO_TRIGGER = 23
GPIO_ECHO    = 24
GPIO_TRIGGER1= 27
GPIO_ECHO1    = 22
bee =26
# output pin: Trigger
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)
GPIO.setup(GPIO_TRIGGER1,GPIO.OUT)
# input pin: Echo
GPIO.setup(GPIO_ECHO,GPIO.IN)
GPIO.setup(GPIO_ECHO1,GPIO.IN)
# output pin :bee
GPIO.setup(bee,GPIO.OUT)
# initialize trigger pin to low
GPIO.output(GPIO_TRIGGER, False)
GPIO.output(GPIO_TRIGGER1, False)
#import cv2
app = Flask(__name__)
mh= Adafruit_MotorHAT(addr=0x60)
pwm = PWM(0x60,debug = False)
# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

#atexit.register(turnOffMotors)

class Motor:

    def __init__(self):
        """ Initialize the motor with its control pins and start pulse-width
             modulation """
        self.left_motor = mh.getMotor(1)
        self.right_motor = mh.getMotor(2)
        self.flag=0

    def forward(self, speed=300):
        """ pinForward is the forward Pin, so we change its duty
             cycle according to speed. """
        self.left_motor.run(Adafruit_MotorHAT.FORWARD)
        self.right_motor.run(Adafruit_MotorHAT.FORWARD)
        self.left_motor.setSpeed(speed)
        self.right_motor.setSpeed(speed)

    def backward(self, speed=300):
        """ pinBackward is the forward Pin, so we change its duty
             cycle according to speed. """
        self.left_motor.run(Adafruit_MotorHAT.BACKWARD)
        self.right_motor.run(Adafruit_MotorHAT.BACKWARD)
        self.left_motor.setSpeed(speed)
        self.right_motor.setSpeed(speed)

    def left(self, speed=150):
        """ pinForward is the forward Pin, so we change its duty
             cycle according to speed. """
        self.left_motor.run(Adafruit_MotorHAT.BACKWARD)
        self.right_motor.run(Adafruit_MotorHAT.FORWARD)
        self.left_motor.setSpeed(speed)
        self.right_motor.setSpeed(speed)

    def right(self, speed=150):
        """ pinForward is the forward Pin, so we change its duty
             cycle according to speed. """
        self.left_motor.run(Adafruit_MotorHAT.FORWARD)
        self.right_motor.run(Adafruit_MotorHAT.BACKWARD)
        self.left_motor.setSpeed(speed)
        self.right_motor.setSpeed(speed)

    def stop(self):
        """ Set the duty cycle of both control pins to zero to stop the motor. """
        mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
        mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
        mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
        mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

class Servo:
    #pwm = PWM(0x60,debug = False)
    angle=90
    servo=-1
    flag=0
    def __init__(self,servo,angle=90):
        #self.pwm = PWM(0x60,debug = False)
        self.servo=servo
        self.angle=angle
        pwm.setPWMFreq(50)  
    def setServoPulse(self,channel, pulse):
        pulseLength = 1000000.0                   # 1,000,000 us per second
        pulseLength /= 50.0                       # 50 Hz
        #print ("%d us per period" % pulseLength)
        pulseLength /= 4096.0                     # 12 bits of resolution
        #print ("%d us per bit" % pulseLength)
        pulse *= 1000.0
        pulse /= (pulseLength*1.0)
        # pwmV=int(pluse)
        #print("pluse: %f  " % (pulse))
        pwm.setPWM(channel, 0, int(pulse))
    def setangle(self,x):
        y=x/90.0+0.5
        y=max(y,0.5)
        y=min(y,2.5)
        self.angle=x
        self.setServoPulse(self.servo,y)
    def up(self):
        if self.angle<=178:
            self.angle+=2
            self.setangle(self.angle)
    def down(self):
        if self.angle>=2:
            self.angle-=2
            self.setangle(self.angle)
@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        #frame=cv2.flip(frame,1,dst=None)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


motor = Motor()
myservo1=Servo(0)
myservo2=Servo(14)   
@app.route('/left_side')
def left_side():
    motor.flag=0
    motor.left()
    return 'true'

@app.route('/right_side')
def right_side():
   motor.flag=0
   motor.right()
   return 'true'

@app.route('/up_side')
def up_side():
   motor.flag=0
   motor.forward()
   return 'true'

@app.route('/down_side')
def down_side():
   motor.flag=0
   motor.backward()
   return 'true'

@app.route('/stop')
def stop():
   motor.flag=0
   motor.stop()
   return  'true'

@app.route('/sup')
def sup():
   myservo1.flag=1
   while(myservo1.flag):
       myservo1.up()
       time.sleep(0.2)
   return  'true'
@app.route('/sdown')
def sdown():
   myservo1.flag=1
   while(myservo1.flag):
       myservo1.down()
       time.sleep(0.2)
   return  'true'
@app.route('/sleft')
def sleft():
   myservo2.flag=1 
   while(myservo2.flag):
       myservo2.up()
       time.sleep(0.2)
   return  'true'
@app.route('/sright')
def sright():
   myservo2.flag=1
   while(myservo2.flag):
       myservo2.down()
       time.sleep(0.2)
   return  'true'
@app.route('/sstop1')
def sstop1():
   myservo1.flag=0;
   return  'true'
@app.route('/sstop2')
def sstop2():
   myservo2.flag=0
   return  'true'
@app.route('/comeback')
def comeback():
   myservo1.flag=0
   myservo2.flag=0
   myservo1.setangle(90)
   myservo2.setangle(90)
   return  'true'
@app.route("/self_drive")
def self_drive():
    motor.flag=1
    try:
        while(motor.flag):
            distance=measure()
            distance1=measure1()
            if(distance<10 or distance1<10):
                motor.stop()
                for i in range(500):
                    GPIO.output(bee,True)
                    time.sleep(0.003)
                    GPIO.output(bee,False)
                #myservo2.setangle(0)
                for i in range(45):
                    myservo2.up()
                d_left=measure()
                time.sleep(1)
                #myservo2.setangle(180)
                for i in  range(90):
                    myservo2.down()
                d_right=measure()
                time.sleep(1)
                for i in range(45):
                    myservo2.up()
                #myservo2.setangle(90)
                if(d_right>20):
                    motor.right()
                    time.sleep(1.5)
                elif(d_left>20):
                    motor.left()
                    time.sleep(1.5)
                else:
                    motor.left()
                    time.sleep(3)
            else:
                motor.forward()
                for i in range(100):
                    GPIO.output(bee,True)
                    time.sleep(0.001)
                    GPIO.output(bee,False)

        GPIO.cleanup()
        return 'true'
    finally:
        motor.stop()
        return 'true'

if __name__ == '__main__':
    #self_drive()
    comeback()
    app.run(host='0.0.0.0', port =80, debug=True, threaded=True)
    comeback()
