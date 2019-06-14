#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  	appCam.py
#  	based on tutorial ==> https://blog.miguelgrinberg.com/post/video-streaming-with-flask
# 	PiCam Local Web Server with Flask
# MJRoBot.org 19Jan18
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
from flask import Flask, render_template, Response

# Raspberry Pi camera module (requires picamera package)
from camera_pi import Camera
app = Flask(__name__)
mh= Adafruit_MotorHAT(addr=0x60)

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

    def forward(self, speed=200):
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

    def left(self, speed=100):
        """ pinForward is the forward Pin, so we change its duty
             cycle according to speed. """
        self.left_motor.run(Adafruit_MotorHAT.BACKWARD)
        self.right_motor.run(Adafruit_MotorHAT.FORWARD)
        self.left_motor.setSpeed(speed)
        self.right_motor.setSpeed(speed)

    def right(self, speed=100):
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

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        #frame=cv2.flip(frame,1,det=None)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
motor = Motor()
@app.route('/left_side')
def left_side():
    motor.left()
    return 'true'

@app.route('/right_side')
def right_side():
   motor.right()
   return 'true'

@app.route('/up_side')
def up_side():
   motor.forward()
   return 'true'

@app.route('/down_side')
def down_side():
   motor.backward()
   return 'true'

@app.route('/stop')
def stop():
   motor.stop()
   return  'true'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port =80, debug=True, threaded=True)
