#!coding:utf-8
import os
import time
import requests
class rapiro:
    def __init__(self,ip):
        self.ip = ip
        self.actions = {
            "停止":'/otto-home',
            "前进":'/otto-walk',
            "后退":'/otto-walk-back',
            "挥手":'/wave-hands',
            "左转":'/otto-turn',
            "右转":'/otto-turn-right'
            }
    def get(self,url):
        r = requests.get(self.ip+url)
        print(r.text)
    def do(self,action):
        method = self.actions.get(action,None)
        if(method):
            self.get(method)
            print("rapiro " + action)
    def isValid(self,text):
        for key in self.actions.keys():
            if(key in text):
                return key
        return None

if __name__ == '__main__':
    rap = rapiro('http://192.168.0.143')
    action = rap.isValid('前进123')
    print(action)
    if action:
        rap.do(action)
    '''rap.do("前进")'''
    time.sleep(4)
    rap.do("挥手")
    time.sleep(4)
    rap.do("停止")
