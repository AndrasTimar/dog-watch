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
    list_of_files=glob.glob(path + '/*')
    filesDict = {'images': ['image1.jpg', 'image2.jpg']}
    return jsonify(list_of_files)
@app.route('/request_photo', methods=['POST'])
def request_photo():
    send_photo_request()
    return "OK"
# main driver function
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

#hostName = "0.0.0.0"
#serverPort = 8080

#class MyServer(SimpleHTTPRequestHandler):
#    def do_GET(self):
#        if self.path == '/latest':
#            list_of_files = glob.glob(path + '*')
#            latest_file = max(list_of_files, key=os.path.getctime)
#            self.path = latest_file
#        elif not self.path.startswith("/images/"):
#            self.path = "/images/"
#        self.send_response(200)
#        self.send_header('Content-type', 'text/html')
#        self.end_headers()
#        message = "This is the return message"
#        self.wfile.write(bytes(message, "utf8"))
#        return SimpleHTTPRequestHandler.do_GET(self)
#    def do_POST(self):
#        self.send_response(200)
#        self.send_header('Content-type','text/html')
#        self.end_headers()
#        message = "Hello, World! Here is a POST response"
#        self.wfile.write(bytes(message, "utf8"))
#        send_photo_request()
#    def end_headers (self):
#        self.send_header('Access-Control-Allow-Origin', '*')
#        SimpleHTTPRequestHandler.end_headers(self)

#if __name__ == "__main__":        
#    webServer = HTTPServer((hostName, serverPort), MyServer)
#    print("Server started http://%s:%s" % (hostName, serverPort))

#    try:
#        webServer.serve_forever()
#    except KeyboardInterrupt:
#        pass

#    webServer.server_close()
#    print("Server stopped.")
