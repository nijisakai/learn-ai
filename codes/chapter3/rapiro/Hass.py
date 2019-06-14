# -*- coding:utf-8 -*-
from __future__ import print_function
import requests
import json
import logging

try:
    reload         # Python 2
except NameError:  # Python 3
    from importlib import reload

import sys
reload(sys)
sys.setdefaultencoding('utf8')

SLUG = "homeassistant"

def handle(text,config):
    if isinstance(text, bytes):
        text = text.decode('utf8')
    if u"帮我" in text:
        text = text.replace(u"帮我", "")
    if u"把" in text:
        text = text.replace(u"把", "")
    if u"的" in text:
        text = text.replace(u"的", "")        
    print(text)
    url = config[SLUG]['url']
    port = config[SLUG]['port']
    password = config[SLUG]['password']
    headers = {'x-ha-access': password, 'content-type': 'application/json'}
    p = json.dumps({"text": text})
    r = requests.post(url + ":" + port + "/api/services/conversation/process", headers=headers,data=p)
    print(r.json())
    return text
def isValid(text):
    return any(word in text for word in [u"开启",u"把",u"关闭",
                                         u"打开", u"帮我"])

if __name__ == '__main__':
	text = u"帮我打开卧室的灯"
	# print(u"帮我" in text)
	config = {"homeassistant":{"url":"http://localhost","port":"8123","password":"123789"}}
	handle(text,config)