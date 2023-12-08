import pika
import os


def send_to_topic(topic, exchange, message):
    connection = pika.BlockingConnection(pika.ConnectionParameters(os.environ["RABBIT_MQ_HOST"]))
    channel = connection.channel()
    channel.exchange_declare(exchange=exchange, exchange_type='topic')
    channel.basic_publish(exchange=exchange, routing_key=topic, body=message)
    print(" [x] Sent: " + str(message) + " to topic: " + topic + ", exchange: " + exchange, flush=True)
    connection.close()
