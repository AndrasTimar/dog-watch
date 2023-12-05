sudo docker image build -t camera_service:latest -f ./Dockerfile_camera_service .
sudo docker image build -t server:latest -f ./Dockerfile_web_server .
sudo docker image build -t dog_detector:latest -f ./Dockerfile_dog_detector .
sudo docker image build -t message_coordinator:latest -f ./Dockerfile_message_coordinator .