import RPi.GPIO as gpio
import time

ledW = 31 #gpio6


t = .5 #.5 milisegundos

gpio.setmode(gpio.BOARD)
gpio.setup(ledW,gpio.OUT)

try:
	while True:
		gpio.output(ledW,1)
		time.sleep(t)
		gpio.output(ledW,0)
		time.sleep(t)

except KeyboardInterrupt:
	print "Terminado!"

finally:
	gpio.cleanup()
