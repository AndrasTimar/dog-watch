#!/usr/bin/env python
from rabbitmq_listener import listen_blocking
import sys, os
import time

path = sys.argv[1]

def take_photo():
    print("Taking photo")
    os.system("libcamera-still -o "+path+"capture"+ str(time.time())+".jpg --immediate")
    print("Photo taken", flush=True)


def main():
    def callback(ch, method, properties, body):
        take_photo()
    listen_blocking(exchange_name="command", routing_key="take_photo", callback=callback) #TODO maybe move keys to env files


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            print("ERROR IN CAMERA_SERVICE")
            os._exit(0)
