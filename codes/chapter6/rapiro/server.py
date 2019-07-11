#!coding:utf-8
import snowboydecoder
import sys
import signal
import os
import yaml

from record import Mic
from baidu_api import Baidu
import Hass
from Tuling import Tuling
from opiro import rapiro

interrupted = False
stt = None
tuling = None
rap = None
mic = Mic()
mic.fetchThreshold()
detector = None
config = None

def detected_callback():
    global detector
    global mic
    global config
    global stt
    global tuling
    global rap
    detector.terminate()
    print "hotword detected"
    os.system("aplay resources/ding.wav")
    # os.system("arecord -d 4 -r 16000 -c 1 -t wav -f S16_LE record.wav")
    mic.activeListenToAllOptions()
    res = stt.recognize()
    if(res['err_no']):
      print(res)
    else:
      text = res['result'][0]
      print(text)
      action = rap.isValid(text)
      if(action):
          print('handled by rapiro')
          rap.do(action)
      elif(Hass.isValid(text)):
        print('handled by hass')
        res = Hass.handle(text,config)
        stt.synthesis('已执行'+res)
        stt.say()
      else:
        print('no handler matched , use default tuling')
        res = tuling.answer(text)
        stt.synthesis(res)
        stt.say()

    detector.start(detected_callback=detected_callback,
           interrupt_check=interrupt_callback,
           sleep_time=0.03)

def signal_handler(signal, frame):
    global interrupted
    interrupted = True

def interrupt_callback():
    global interrupted
    return interrupted

def main():
  global detector
  global stt
  global config
  global tuling
  global rap
  if len(sys.argv) == 1:
      print("Error: need to specify model name")
      print("Usage: python demo.py your.model")
      sys.exit(-1)

  with open("./config.yaml") as f:
      config = yaml.load(f)
  
  stt = Baidu(config)
  tuling = Tuling(config)
  rap = rapiro('http://192.168.0.143')
  print(len(sys.argv))
  model = sys.argv[1]

  # capture SIGINT signal, e.g., Ctrl+C
  signal.signal(signal.SIGINT, signal_handler)

  detector = snowboydecoder.HotwordDetector(model, sensitivity=0.5)
  print('Listening... Press Ctrl+C to exit')

  # main loop
  detector.start(detected_callback=detected_callback,
                 interrupt_check=interrupt_callback,
                 sleep_time=0.03)

  detector.terminate()


if __name__ == '__main__':
  main()
