#adaptado de http://blog.emilioeiji.com.br/raspberry-pi-sensor-de-distancia-ultrassonico-hc-sr04/
#HC-SR04
#11
#13

import RPi.GPIO as gpio
import time


TRIG = 11 #porta11
ECHO = 13 #porta13

gpio.setmode(gpio.BOARD)
gpio.setup(TRIG,gpio.OUT)
gpio.setup(ECHO,gpio.IN)

s =100
inic = 1
L = list()
avg = 0

try:
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
		print "Distancia: ",distance," cm ---> ",inic
		L.append(distance)
		if (inic < s):
			inic = inic +1
		if (inic == s):
			avg = float(sum(L))/s
			L.pop(0)
			
		print("AVG: %.2f" %avg)

except KeyboardInterrupt:
	print "Terminado!"

finally:
	gpio.cleanup()
