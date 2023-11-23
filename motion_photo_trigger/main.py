from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import os


hostName = "raspberrypi.local"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        print("generating image")
        os.system("libcamera-still -o ../photo_server/public/smaller.jpg --hflip --vflip")

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
