#led blinking
#pin6 negativo
#pin12 positivo+1k resistor

import RPi.GPIO as gpio
import time

ledY = 16 #gpio23
ledG = 18 #gpio24

t = .5 #.5 milisegundos

gpio.setmode(gpio.BOARD)
gpio.setup(ledY,gpio.OUT)
gpio.setup(ledG,gpio.OUT)

try:
	while True:
		gpio.output(ledY,1)
		gpio.output(ledG,0)
		time.sleep(t)
		gpio.output(ledY,0)
		gpio.output(ledG,1)
		time.sleep(t)

except KeyboardInterrupt:
	print "Terminado!"

finally:
	gpio.cleanup()
