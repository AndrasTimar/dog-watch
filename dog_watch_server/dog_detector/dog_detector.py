import sys,os
from gpiozero import MotionSensor
import time
from request_photo import send_photo_request

def start_watching():
	print("Starting up")
	sensor = MotionSensor(int(os.environ['MOTION_DETECTOR_CONTROL_PIN']))
	print("IR Sensor Ready.....")
	while True:
		print("Waiting for motion")
		sensor.wait_for_motion()
		send_photo_request()
		sensor.wait_for_no_motion()
		time.sleep(5)

if __name__ == '__main__':
    try:
        start_watching()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)		

