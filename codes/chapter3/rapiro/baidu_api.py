#!coding:utf-8

from aip import AipSpeech
import yaml
import os
import time

SLUG = 'baidu_yuyin'

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

class Baidu:
	def __init__(self, config):
		APP_ID = config[SLUG]['app_id']
		API_KEY = config[SLUG]['api_key']
		SECRET_KEY = config[SLUG]['secret_key']
		self._client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
	# 读取文件


	# 识别本地文件
	def recognize(self,audio_file = 'record.wav'):
		file = get_file_content(audio_file)
		res = self._client.asr(file, 'wav', 16000, {
	    'dev_pid': 1536,
	})
		return res

	def synthesis(self,text = '你好百度',lang = 'zh',type = 1 , vol = 5):
		result  = self._client.synthesis(text, lang, type, {
	    'vol': vol,
	})
		# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
		if not isinstance(result, dict):
		    with open('auido.mp3', 'wb') as f:
		        f.write(result)
		        return 1
		else:
			print(result)
			return 0
	def say(self,audio_file = 'auido.mp3'):
		os.system('mpg123 ' + audio_file)


if __name__ == '__main__':
    with open("./config.yaml") as f:
        config = yaml.load(f)
        stt = Baidu(config)
        res = stt.recognize()
        if(res['err_no']):
        	print(res)
        else:
   			print(res['result'][0])
        stt.synthesis('hello world')
        stt.say()

