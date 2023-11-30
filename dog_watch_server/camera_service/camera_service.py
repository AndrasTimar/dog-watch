#!/usr/bin/env python
import pika, sys, os
import time

path = sys.argv[1]

def take_photo():
    print("Taking photo")
    os.system("libcamera-still -o "+path+"capture"+ str(time.time())+".jpg --immediate")


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq',heartbeat=36000)) #TODO env var
    channel = connection.channel()
    channel.exchange_declare(exchange='movement',exchange_type='topic')

    result = channel.queue_declare(queue='', exclusive=True)
    queue_name= result.method.queue
    channel.queue_bind(exchange='movement',queue=queue_name, routing_key="movement.photo_requested")

    def callback(ch, method, properties, body):
        take_photo()
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C', flush=True)
    channel.start_consuming()

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
