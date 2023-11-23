from http.server import SimpleHTTPRequestHandler, HTTPServer
import time
import os
from threading import Thread
from dog_detector import startWatching, takePhoto
import sys
import glob
import os

path = sys.argv[1]

print("Starting with path: ", path)

hostName = "raspberrypi.local"
serverPort = 8080

Thread(target=startWatching,args=(path,)).start()

class MyServer(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/latest':
            list_of_files = glob.glob(path + '*')
            latest_file = max(list_of_files, key=os.path.getctime)
            self.path = latest_file
        return SimpleHTTPRequestHandler.do_GET(self)
    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        message = "Hello, World! Here is a POST response"
        self.wfile.write(bytes(message, "utf8"))
        Thread(target=takePhoto, args=(path,)).start()
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
