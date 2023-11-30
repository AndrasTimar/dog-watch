sudo docker image build -t camera_service:latest -f ./camera_service/Dockerfile .
sudo docker image build -t server:latest -f ./web_server/Dockerfile .
sudo docker image build -t dog_detector:latest -f ./dog_detector/Dockerfile .
