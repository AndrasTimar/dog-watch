from rabbitmq_sender import send_to_topic
def send_photo_request():
	send_to_topic("movement.photo_requested", "movement", "movement_detected")
