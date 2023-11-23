import os
from gpiozero import MotionSensor
import time
from datetime import datetime

sensor = MotionSensor(4)

print("IR Sensor Ready.....")

while True:
	print("Waiting for motion")
	sensor.wait_for_motion()
	print("Object Detected")
	sensor.wait_for_no_motion()
	os.system("libcamera-still -o ../photo_server/public/smaller.jpg --hflip --vflip")
	time.sleep(5)
	
		

