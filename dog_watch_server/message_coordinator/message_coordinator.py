from rabbitmq_sender import send_to_topic
from rabbitmq_listener import listen_blocking

def handle_event(event):
    #TODO handle differently per event
    print("Received event: " + str(event), flush = True)
    send_to_topic(exchange="command", topic="take_photo", message="take_photo")

def start():
    def callback(ch, method, properties, body):
        handle_event(body)
    print("Message coordinator listening...", flush = True)
    listen_blocking(exchange_name="dog_watch", routing_key="*", callback=callback) #TODO maybe move keys to env files


if __name__ == '__main__':
    try:
        start()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)		

