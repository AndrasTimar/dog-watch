FROM ubuntu:20.04

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get --no-install-recommends install -y python3-pip git
RUN apt-get install -y cmake libgnutls28-dev openssl libboost-dev
RUN pip3 install pyyaml ninja meson jinja2 ply
RUN apt-get install -y libgstreamer1.0-0 libgstreamer1.0-dev gstreamer1.0-dev gstreamer1.0-libav gstreamer1.0-tools gstreamer1.0-x gstreamer1.0-plugins-base-apps libgstreamer-plugins-base1.0-dev

RUN apt-get install -y libgnutls28-dev openssl libudev-dev libboost-dev qtbase5-dev libqt5core5a libqt5gui5 libqt5widgets5 && pip3 install pyyaml ply jinja2
RUN git clone https://git.libcamera.org/libcamera/libcamera.git
WORKDIR /libcamera
RUN meson setup build
RUN ninja -C build install
RUN cp /usr/local/lib/aarch64-linux-gnu/gstreamer-1.0/* /usr/lib/aarch64-linux-gnu/gstreamer-1.0/
WORKDIR /
CMD [ "gst-device-monitor-1.0", "Video"]
# copy the requirements file into the image
COPY ./camera_service/requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app
# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

RUN ls -l

# copy every content from the local file to the image
COPY ./camera_service/camera_service.py /app
# configure the container to run in an executed manner
ENTRYPOINT [ "python3" ]

CMD ["camera_service.py", "/images/"]
