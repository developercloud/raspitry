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
	        gpio.output(IR,True)

	gpio.output(IR,False)
	camera.stop_preview()

except KeyboardInterrupt:
	print "Terminado!"


finally:
	gpio.cleanup()
