#FROM ubuntu:20.04

FROM balenalib/raspberrypi4-64-debian
# Set in container
ENV TZ=Europe/Budapest

RUN apt-get update && apt-get upgrade
RUN apt-get install -y python3
RUN apt-get install python3-pip

COPY ./dog_detector/requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app
# install the dependencies and packages in the requirements file
RUN pip3 install -r requirements.txt

# copy every content from the local file to the image
COPY ./dog_detector/dog_detector.py /app
COPY ./request_photo.py /app
COPY ./rabbitmq_sender.py /app
# configure the container to run in an executed manner
ENTRYPOINT [ "python3" ]

CMD ["dog_detector.py"]
