from http.server import SimpleHTTPRequestHandler, HTTPServer
import time
import sys
import glob
import os
from request_photo import send_photo_request
from flask import jsonify
from flask import Flask
 
app = Flask(__name__)

path = sys.argv[1]

print("Starting with path: ", path)
 
@app.route('/', methods=['GET'])
def hello_world():
    list_of_files=sorted(glob.glob(path+"*"), key=os.path.getmtime)
    filesDict = {'images': ['image1.jpg', 'image2.jpg']}
    return jsonify(list_of_files)
@app.route('/request_photo', methods=['POST'])
def request_photo():
    send_photo_request()
    return "OK"
# main driver function
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
