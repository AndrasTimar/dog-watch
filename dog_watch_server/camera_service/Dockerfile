# start by pulling the python image
FROM python:3.12.0-alpine

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
ENTRYPOINT [ "python" ]

CMD ["camera_service.py", "/images/"]

