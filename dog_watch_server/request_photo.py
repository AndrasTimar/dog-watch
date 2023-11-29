from rabbitmq_sender import sendToTopic
def send_photo_request():
	sendToTopic("movement.photo_requested", "movement", "movement_detected")
