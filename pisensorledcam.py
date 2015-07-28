#adaptado de http://blog.emilioeiji.com.br/raspberry-pi-sensor-de-distancia-ultrassonico-hc-sr04/
#HC-SR04
#11
#13

import RPi.GPIO as gpio
import time
import picamera
import os

TRIG = 11 #porta11
LED  = 12 #porta12
ECHO = 13 #porta13
IR   = 29 #porta29
LEDW = 31 #porta31
PUSH = 40 #porta40


gpio.setmode(gpio.BOARD)
gpio.setup(TRIG,gpio.OUT)
gpio.setup(ECHO,gpio.IN)
gpio.setup(LED,gpio.OUT)
gpio.setup(IR,gpio.OUT)
gpio.setup(LEDW,gpio.OUT)

gpio.output(IR,False)
gpio.output(LEDW,False)
gpio.output(LED,False)

gpio.setup(PUSH, gpio.IN, pull_up_down=gpio.PUD_UP)

try:
	camera = picamera.PiCamera()
	camera.start_preview()
	gpio.output(IR,True)
	#gpio.output(LEDW,True)

	
	while True:


                print "Medindo..."
		gpio.output(TRIG,False)
		time.sleep(.01)
		gpio.output(TRIG,True)
		time.sleep(0.00001)
		gpio.output(TRIG,False)
		pulse_start = 0
		pulse_end = 0

		while gpio.input(ECHO)==0:
			pulse_start = time.time()
	
		while gpio.input(ECHO)==1:
			pulse_end = time.time()
	
		pulse_duration = pulse_end - pulse_start
		distance = pulse_duration * 17150
		distance = round(distance,2)

		if (30 <= distance <= 40.0):
			gpio.output(LED,True)
			#gpio.output(LEDW,True)
			#gpio.output(IR,True)
			input_state = gpio.input(PUSH)

			if (input_state == False):
				print "take a photo..."
				#camera.start_preview()
				#time.sleep(2)
				camera.capture("teste.jpg")
				#camera.start_preview()
				time.sleep(2)
				
		else:
			gpio.output(LED,False)
			#gpio.output(LEDW,False)
			#gpio.output(IR,False)
		#os.system("clear")
		print "Distancia: ",distance," cm"
	camera.stop_preview()

except KeyboardInterrupt:
	print "Terminado!"


finally:
	gpio.cleanup()
