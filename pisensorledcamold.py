#adaptado de http://blog.emilioeiji.com.br/raspberry-pi-sensor-de-distancia-ultrassonico-hc-sr04/
#HC-SR04
#11
#13

import RPi.GPIO as gpio
import time
import picamera


TRIG = 11 #gpio17
LED  = 16 #gpio23
IR   = 29 #gpio5
ECHO = 13 #gpio27
PUSH = 40 #gpio21

gpio.setmode(gpio.BOARD)
gpio.setup(TRIG,gpio.OUT)
gpio.setup(ECHO,gpio.IN)
gpio.setup(IR,gpio.OUT)
gpio.setup(LED,gpio.OUT)
gpio.output(LED,False)
gpio.output(IR,False)

gpio.setup(PUSH, gpio.IN,pull_up_down=gpio.PUD_UP)

try:
        camera = picamera.PiCamera()
	
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

		if (30.0 <= distance <= 40.0):
			gpio.output(LED,True)
			gpio.output(IR,True)
			input_state = gpio.input(PUSH)
			if (input_state == False):
				print "take a photo..."
				time.sleep(5)
				camera.capture("teste.jpg")
				camera.stop_preview()
				
		else:
			gpio.output(LED,False)
			gpio.output(IR,False)

		print "Distancia: ",distance," cm"

except KeyboardInterrupt:
	print "Terminado!"

finally:
	gpio.cleanup()
