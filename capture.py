import RPi.GPIO as gpio
import time
import picamera
import os
import sys

IR1  = 29 #gpio5
IR2  = 31 #gpio6
PUSH = 40 #gpio21

gpio.setmode(gpio.BOARD)
gpio.setup(IR1,gpio.OUT)
gpio.setup(IR2,gpio.OUT)
gpio.setup(PUSH, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.output(IR1,False)
gpio.output(IR2,False)

def getName():
	name = "captures "+time.strftime("%y-%m-%d %H %M %S")
	return name;

try:
	camera = picamera.PiCamera()
	camera.start_preview()
	gpio.output(IR1,True)
	while True:
		input_state = gpio.input(PUSH)
		if (input_state == False):
			print ("take a photo...")
			gpio.output(IR1,True)
			gpio.output(IR2,True)
			filename = getName()
			camera.capture("/home/pi/raspitry/"+filename+" IR.jpg")
			gpio.output(IR1,False)
			gpio.output(IR2,False)	
			sys.exit(os.EX_OK)

except KeyboardInterrupt:
	print ("Terminado!")

finally:
	gpio.cleanup()
