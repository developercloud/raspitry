import RPi.GPIO as gpio
import picamera

IR   = 29 #gpio5

gpio.setmode(gpio.BOARD)
gpio.setup(IR,gpio.OUT)

gpio.output(IR,False)

try:
	camera = picamera.PiCamera()
	#camera.preview_fullscreen = False
	#camera.preview_window = (0,0,800,600)
	camera.start_preview()
	
	while True:
	        gpio.output(IR,True)

	gpio.output(IR,False)
	camera.stop_preview()

except KeyboardInterrupt:
	print "Terminado!"

finally:
	gpio.cleanup()
