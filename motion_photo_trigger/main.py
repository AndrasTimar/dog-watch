from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import os
from threading import Thread


hostName = "raspberrypi.local"
serverPort = 8080

def takePhoto():
    print("Taking photo")
    os.system("libcamera-still -o ./photo_server/public/smaller.jpg --hflip --vflip")


class MyServer(BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        message = "Hello, World! Here is a POST response"
        self.wfile.write(bytes(message, "utf8"))
        Thread(target=takePhoto).start()
    def end_headers (self):
        self.send_header('Access-Control-Allow-Origin', '*')
        BaseHTTPRequestHandler.end_headers(self)

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
