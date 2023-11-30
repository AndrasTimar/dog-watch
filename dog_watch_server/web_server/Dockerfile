# start by pulling the python image
FROM python:3.12.0-alpine

# copy the requirements file into the image
COPY ./web_server/requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app
# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

RUN ls -l

# copy every content from the local file to the image
COPY ./web_server/server.py /app
COPY ./request_photo.py /app
COPY ./rabbitmq_sender.py /app
# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["server.py", "./static/images/" ]
