import sys
import glob
import os
from flask import jsonify
from flask import Flask
from common import rabbitmq_sender
from datetime import datetime


def send_photo_request():
    rabbitmq_sender.send_to_topic(topic="photo_requested", exchange="event", message="photo_requested")


app = Flask(__name__)

path = sys.argv[1]

print("Starting with path: ", path)


@app.route('/', methods=['GET'])
def hello_world():
    list_of_files = sorted(glob.glob(path + "*"), key=os.path.getctime, reverse=True)
    result = []
    for file in list_of_files:
        only_filename = file.split("/")[-1]
        file_stats = os.stat(file)
        ct_date_time = datetime.fromtimestamp(file_stats.st_ctime).strftime('%Y-%m-%d %H:%M:%S')
        result.append({"name": only_filename, "ctime": ct_date_time, "size": file_stats.st_size})
    return jsonify(result)


@app.route('/request_photo', methods=['POST'])
def request_photo():
    send_photo_request()
    return "OK"


# main driver function
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
