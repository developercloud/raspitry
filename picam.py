#camera

import time
import picamera

try:
	camera = picamera.PiCamera()

	camera.start_preview()

	#camera.capture(time.strftime("%Y-%m-%d %H %M %S")+".jpg")
	camera.capture("teste.jpg")
	
	time.sleep(5)


except KeyboardInterrupt:
	print "Terminado!"

finally:
	camera.stop_preview()
