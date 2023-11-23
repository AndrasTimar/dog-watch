import os
from gpiozero import MotionSensor
import time

def takePhoto(path):
    print("Taking photo")
    os.system("libcamera-still -o "+path+"capture"+ str(time.time())+".jpg --hflip --vflip")

def startWatching(path):
	print("Starting up")
	sensor = MotionSensor(4)
	print("IR Sensor Ready.....")
	while True:
		print("Waiting for motion")
		sensor.wait_for_motion()
		print("Object Detected")
		sensor.wait_for_no_motion()
		takePhoto(path)
		time.sleep(5)
		

