from http.server import SimpleHTTPRequestHandler, HTTPServer
import time
import sys
import glob
import os
from request_photo import send_photo_request

path = sys.argv[1]

print("Starting with path: ", path)

hostName = "raspberrypi.local"
serverPort = 8080

class MyServer(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/latest':
            list_of_files = glob.glob(path + '*')
            latest_file = max(list_of_files, key=os.path.getctime)
            self.path = latest_file
        elif not self.path.startswith("/images/"):
            self.path = "/images/"
        return SimpleHTTPRequestHandler.do_GET(self)
    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        message = "Hello, World! Here is a POST response"
        self.wfile.write(bytes(message, "utf8"))
        send_photo_request()
    def end_headers (self):
        self.send_header('Access-Control-Allow-Origin', '*')
        SimpleHTTPRequestHandler.end_headers(self)

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
