#!coding:utf-8
import requests
import json
import yaml
SLUG = 'tuling'
class Tuling:
    def __init__(self,config):
        self.key = config[SLUG]['key']
        self.url = 'http://www.tuling123.com/openapi/api'
    def answer(self,text):
        try:
            req = {'key':self.key,'info':text}
            res = requests.post(url = self.url, data = req)
            print(res.text)
            jd = json.loads(res.text)
            return(jd['text'])
        except:
            return("Error")

if __name__ == '__main__':
    with open("./config.yaml") as f:
        config = yaml.load(f)
    tul = Tuling(config)
    print(tul.answer('找几张图片'))