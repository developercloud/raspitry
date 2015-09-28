#adaptado de http://blog.emilioeiji.com.br/raspberry-pi-sensor-de-distancia-ultrassonico-hc-sr04/
#HC-SR04
#11
#13

import RPi.GPIO as gpio
import time
import picamera


TRIG = 11 #porta11
LED  = 12 #porta12
ECHO = 13 #porta13
IR   = 29 #porta29


gpio.setmode(gpio.BOARD)
gpio.setup(TRIG,gpio.OUT)
gpio.setup(ECHO,gpio.IN)
gpio.setup(LED,gpio.OUT)
gpio.setup(IR,gpio.OUT)

try:
	camera = picamera.PiCamera()
	camera.start_preview()

	while True:
			
		gpio.output(IR,True)
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
		else:
			gpio.output(LED,False)
		print "Distancia: ",distance," cm"

except KeyboardInterrupt:
	print "Terminado!"
	gpio.output(IR,False)
	camera.stop_preview()

finally:
	gpio.cleanup()
