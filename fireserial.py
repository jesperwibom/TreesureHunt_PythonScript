#!/usr/local/bin/python
import serial
from time import sleep
import requests

### Our firebase
#firebase_url = "https://blinding-torch-9917.firebaseio.com/"

### My firebase
firebase_url = "https://boiling-heat-8172.firebaseio.com/"

### Arduino adress on raspberry pi
#arduino = '/dev/tty.usbmodem1421'

### Arduino adress on mac
arduino = '/dev/tty.usbmodem1421'

### Set this to your Arduino adress
#ser = serial.Serial(arduino, 9600)

while 1:

	### While the script runs it will search the LightCue key on firebase
	r = requests.get(firebase_url+'LightCue.json')
	result = r.json()

	### If a result that is not 0 is found it sends that result through serial and sets LightCue to 0
	if result == 1:
		#ser.write('1')
		requests.put(firebase_url+'LightCue.json',data='0')
		print ("1")
	elif result == 2:
		#ser.write('2')
		requests.put(firebase_url+'LightCue.json',data='0')
		print ("2")
	elif result == 3:
		#ser.write('3')
		requests.put(firebase_url+'LightCue.json',data='0')
		print ("3")
	sleep(0.1)


