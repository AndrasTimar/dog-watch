#!/usr/bin/env python
import pika
#movement.started
#movement
#any message
def send_to_topic(topic, exchange, message):
	connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
	channel = connection.channel()
	channel.exchange_declare(exchange=exchange, exchange_type='topic')
	channel.basic_publish(exchange=exchange, routing_key=topic, body=message)
	print(" [x] Sent: " + str(message))
	connection.close()
if __name__ == '__main__':
	try:
		send("A MESSAGE")
	except KeyboardInterrupt:
		print('Interrupted')
		try:
			sys.exit(0)
		except SystemExit:
			os._exit(0)
