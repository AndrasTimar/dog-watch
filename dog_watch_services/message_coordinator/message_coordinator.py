import sys

sys.path.append("..")
 
from common import send_to_topic
from common import listen_blocking

def handle_motion_detection(body):
    send_to_topic(exchange="command", topic="take_photo", message="take_photo")

def handle_photo_requested(body):
    send_to_topic(exchange="command", topic="take_photo", message="take_photo")

def handle_event(ch, method, properties, body):
    print("Received event: " + str(body), flush = True)
    routing_key = method.routing_key
    match routing_key:
        case "motion_detected": 
            handle_motion_detection(body)
        case "photo_requested": 
            handle_photo_requested(body)
        case _: raise ValueError(f"Unknown event {routing_key}")

def start():
    def callback(ch, method, properties, body):
        handle_event(ch, method, properties, body)
    print("Message coordinator listening...", flush = True)
    listen_blocking(exchange_name="event", routing_key="*", callback=callback) #TODO maybe move keys to env files


if __name__ == '__main__':
    try:
        start()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)		

