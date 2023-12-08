import sys, os, time
from gpiozero import MotionSensor

from common import rabbitmq_sender


def notify_movement_detected():
    rabbitmq_sender.send_to_topic(topic="motion_detected", exchange="event", message="motion_detected")


def start_watching():
    print("Starting up")
    sensor = MotionSensor(int(os.environ['MOTION_DETECTOR_CONTROL_PIN']))
    print("IR Sensor Ready.....")
    while True:
        print("Waiting for motion")
        sensor.wait_for_motion()
        notify_movement_detected()
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
