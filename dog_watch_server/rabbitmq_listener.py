import pika, sys, os
import time
from time import sleep

#routing_key is the topic to listen to
def listen_blocking(exchange_name, routing_key, callback, retry_timeout_seconds = 3, max_retry_count = 10): 
    connection = None
    connected = False
    retry_count = 0
    while(not connected):
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters(host=os.environ["RABBIT_MQ_HOST"], heartbeat=36000))
            channel = connection.channel()
            channel.exchange_declare(exchange=exchange_name, exchange_type='topic')
            result = channel.queue_declare(queue='', exclusive=True)
            queue_name= result.method.queue
            channel.queue_bind(exchange=exchange_name,queue=queue_name, routing_key=routing_key)

            channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

            print(' [*] Waiting for messages. To exit press CTRL+C', flush=True)
            connection = True
            channel.start_consuming()
        except Exception as e:
            print(str(e), flush=True)
            if retry_count >= max_retry_count:
                raise
            print(f"Could not connect to message queue. Retrying in {retry_timeout_seconds} seconds")
            sleep(retry_timeout_seconds)
            continue