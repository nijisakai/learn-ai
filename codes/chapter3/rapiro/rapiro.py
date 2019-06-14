#!coding:utf-8
import os
import time
class rapiro:
    def forward(self):
        os.system('"C:/Users/hyinn/AppData/Local/Google/Chrome/Application/chrome.exe" http://192.168.0.157/otto-walk')
    def backward(self):
        os.system('echo "#M1" | minicom -b 57600 -D /dev/ttyUSB0')
    def turn_left(self):
        os.system('echo "#M4" | minicom -b 57600 -D /dev/ttyUSB0')
    def turn_right(self):
        os.system('echo "#M3" | minicom -b 57600 -D /dev/ttyUSB0')
    def wave_hands(self):
        os.system('echo "#M5" | minicom -b 57600 -D /dev/ttyUSB0')
    def wave_right(self):
        os.system('echo "#M6" | minicom -b 57600 -D /dev/ttyUSB0')
    def grip_hands(self):
        os.system('echo "#M7" | minicom -b 57600 -D /dev/ttyUSB0')
    def wave_left(self):
        os.system('echo "#M8" | minicom -b 57600 -D /dev/ttyUSB0')
    def stretch_right(self):
        os.system('echo "#M9" | minicom -b 57600 -D /dev/ttyUSB0')
    def stop(self):
        os.system('echo "#M0" | minicom -b 57600 -D /dev/ttyUSB0')
    def other(self):
        print("未定义的指令")
    def do(self,action):
        actions = {
            "停止":self.stop,
            "前进":self.forward,
            "后退":self.backward,
            "挥手":self.wave_hands,
            "左转":self.turn_left,
            "右转":self.turn_right
            }
        method = actions.get(action,self.other)
        if(method):
            method()
            print("rapiro " + action)

if __name__ == '__main__':
    rap = rapiro()
    rap.do("前进")
    time.sleep(4)
    rap.do("挥手")
    time.sleep(4)
    rap.do("停止")
