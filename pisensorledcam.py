#adaptado de http://blog.emilioeiji.com.br/raspberry-pi-sensor-de-distancia-ultrassonico-hc-sr04/
#HC-SR04
#11
#13

import RPi.GPIO as gpio
import time
import picamera
import os

TRIG = 11 #gpio17
LEDY  = 16 #gpio23
LEDG  = 18 #gpio24
ECHO = 13 #gpio27
IR   = 29 #gpio5
LEDW = 31 #gpio6
PUSH = 40 #gpio21


gpio.setmode(gpio.BOARD)
gpio.setup(TRIG,gpio.OUT)
gpio.setup(ECHO,gpio.IN)
gpio.setup(LEDY,gpio.OUT)
gpio.setup(LEDG,gpio.OUT)
gpio.setup(IR,gpio.OUT)
gpio.setup(LEDW,gpio.OUT)

gpio.output(IR,False)
gpio.output(LEDW,False)
gpio.output(LEDY,False)
gpio.output(LEDG,False)

gpio.setup(PUSH, gpio.IN, pull_up_down=gpio.PUD_UP)

Lmax = 40.0
Lmin = 30.0
Lcenter = 4.0

try:
	camera = picamera.PiCamera()
	camera.start_preview()
	
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

		if (Lmin <= distance <= Lmax):
			gpio.output(LEDY,True)
			input_state = gpio.input(PUSH)
                        c = ((Lmax-Lmin)/2) - (Lcenter/2)
			if (Lmin+c <= distance <= Lmax-c):
				gpio.output(LEDG,True)
				if (input_state == False):
				
					#print "take a photo..."
					print "take a photo..."

				        gpio.output(IR,True)
					time.sleep(0.7)
					camera.capture("testeIR.jpg")
				
				        gpio.output(LEDW,True)
					camera.capture("testeIRW.jpg")

					gpio.output(IR,False)
	
					camera.capture("testeW.jpg")
				        gpio.output(LEDW,False)
  
			else:
				gpio.output(LEDG,False)
		else:
			gpio.output(LEDG,False)
			gpio.output(LEDY,False)

		print "Distancia: ",distance," cm"
	camera.stop_preview()

except KeyboardInterrupt:
	print "Terminado!"


finally:
	gpio.cleanup()
