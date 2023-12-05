#FROM ubuntu:20.04

FROM balenalib/raspberrypi4-64-debian
# Set in container
ENV TZ=Europe/Budapest

# See https://github.com/waveform80/picamera/issues/578
ENV READTHEDOCS=True
ENV LD_LIBRARY_PATH=/opt/vc/li

RUN apt-get update && apt-get upgrade
RUN apt-get install -y python3
RUN apt-get install python3-pip
RUN apt-get install libcamera-apps-lite

COPY ./camera_service/requirements.txt /app/requirements.txt

#RUN groupadd -r -g 888 app && \
#    useradd -r -u 888 -g app -d /app app && \
#    chown -R app:app /app && \
#    usermod -a -G video app
#USER app

# switch working directory
WORKDIR /app
# install the dependencies and packages in the requirements file
RUN pip3 install -r requirements.txt

# copy every content from the local file to the image
COPY ./camera_service/camera_service.py /app
# configure the container to run in an executed manner
ENTRYPOINT [ "python3" ]

CMD ["camera_service.py", "/images/"]
