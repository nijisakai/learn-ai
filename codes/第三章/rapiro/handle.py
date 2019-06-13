#!coding:utf-8
from rapiro import *
rap = rapiro()
def handle(str):
    cmds = ["前进","后退","左转","右转","停止"]
    for cmd in cmds:
        if(cmd in str):
            rap.do(cmd)
            break
