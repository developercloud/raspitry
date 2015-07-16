#led blinking
import RPi.GPIO as gpio
import time

p = 12 #porta 18
t = .5 #.5 milisegundos

gpio.setmode(gpio.BOARD)
gpio.setup(p,gpio.OUT)

try:
	while True:
		gpio.output(p,0)
		time.sleep(t)
		gpio.output(p,1)
		time.sleep(t)

except KeyboardInterrupt:
	print "Terminado!"

finally:
	gpio.cleanup()
