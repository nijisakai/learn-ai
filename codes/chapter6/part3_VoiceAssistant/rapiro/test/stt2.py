#!coding:utf-8
 
import wave
import urllib, pycurl
import base64
import json
import yaml
from handle import *
## get access token by api key & secret key
## 获得token，需要填写你的apikey以及secretkey
def get_token():
    with open("./config.yaml") as f:
        config = yaml.load(f)
        apiKey = config["baidu_yuyin"]["api_key"]
        secretKey = config["baidu_yuyin"]["secret_key"]
    auth_url = "https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=" + apiKey + "&client_secret=" + secretKey
 
    print(auth_url)
    res = urllib.urlopen(auth_url)
    json_data = res.read().decode("utf-8")
    return json.loads(json_data)['access_token']
 
def dump_res(buf):
    if json.loads(buf.decode("utf-8"))['err_msg']=='success.':
        res = json.loads(buf.decode("utf-8"))['result'][0]
        print("ok:" + res)
        print(type(res))
        handle(res.encode("utf-8"))
 
## post audio to server
def use_cloud(token):
    fp = wave.open('record.wav', 'rb')#录音文件名
    ##已经录好音的语音片段
    nf = fp.getnframes()
    f_len = nf * 2
    audio_data = fp.readframes(nf)
 
    cuid = "8133661" #你的产品id
    base = 'http://vop.baidu.com/server_api'
    srv_url = base + '?cuid=' + cuid + '&token=' + token
    http_header = [
        'Content-Type: audio/pcm; rate=16000',
        'Content-Length: %d' % f_len
    ]
 
    c = pycurl.Curl()
    c.setopt(pycurl.URL, str(srv_url)) #curl doesn't support unicode
    #c.setopt(c.RETURNTRANSFER, 1)
    c.setopt(c.HTTPHEADER, http_header)   #must be list, not dict
    c.setopt(c.POST, 1)
    c.setopt(c.CONNECTTIMEOUT, 30)
    c.setopt(c.TIMEOUT, 30)
    c.setopt(c.WRITEFUNCTION, dump_res)
    c.setopt(c.POSTFIELDS, audio_data)
    c.setopt(c.POSTFIELDSIZE, f_len)
    c.perform() #pycurl.perform() has no return val
 
if __name__ == "__main__":
    token = get_token()
    #获得token
    #进行处理然后
    use_cloud(token)
