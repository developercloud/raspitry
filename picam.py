#camera

import time
import picamera

try:
	camera = picamera.PiCamera()
	camera.start_preview()
	camera.iso = 800
        camera.capture("iso800.jpg")
	time.sleep(5)
        
        #print camera.iso
	#camera.capture(time.strftime("%Y-%m-%d %H %M %S")+".jpg")
	#camera.capture("teste.jpg")
	
	camera.iso = 0
        camera.capture("isoZero.jpg")
	time.sleep(5)


except KeyboardInterrupt:
	print "Terminado!"

finally:
	camera.stop_preview()
