#!/usr/bin/env python
import pika

def send_to_topic(topic, exchange, message):
	connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
	channel = connection.channel()
	channel.exchange_declare(exchange=exchange, exchange_type='topic')
	channel.basic_publish(exchange=exchange, routing_key=topic, body=message)
	print(" [x] Sent: " + str(message))
	connection.close()
