import urllib.request as request
import time
otto_url = "http://192.168.0.157"

def setServo(pin,value):
	url = otto_url + '/set-servo?di=%d&vi=%d' % (pin,value)
	try:
		res = request.urlopen(url).read()
	except:
		print('error occured')
	if(res):
		print(url,res)

def attachServos():
	url = otto_url + '/attach-servos'
	res = request.urlopen(url).read()
	print(url,res)

if __name__ == '__main__':
	setServo(7,45)
	# attachServos()
	time.sleep(2)

	setServo(7,135)
	# attachServos()
	time.sleep(2)

