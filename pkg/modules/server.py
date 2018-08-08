from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import json
import time
from pkg.utilservices import utility
from threading import Thread

PORT = 5000


class Handler(BaseHTTPRequestHandler):
    # def do_HEAD(self):
    #     self.send_response(200)
    #     self.send_header('Content-Type', 'text/html')
    #     self.end_headers()

    def do_GET(self):

        for pathParam in pathParams:
            print 'path param:', pathParam
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        myObject = {
            "name": "monkey"
        }
        jsonObject = json.dumps(myObject)
        self.wfile.write(jsonObject)

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()

        contentLength = int(self.headers.getheader('content-length', 0))
        body = self.rfile.read(contentLength)
        bodyJson = json.loads(body)
        bodyParsed = utility.parseType(bodyJson)

        pathParams = self.path.split('/')
        if pathParams[1] == 'modules':
            self.OnModuleRequest(pathParams[2], bodyParsed)
        myObject = {
            "name": "monkey"
        }
        jsonObject = json.dumps(myObject)
        self.wfile.write(jsonObject)

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.send_header('Access-Control-Allow-Methods', ['POST', 'GET', 'OPTIONS'])
        self.send_header('Access-Control-Max-Age', 86400)
        BaseHTTPRequestHandler.end_headers(self)


class Server():
    # def __init__(self, port=5000, host='0.0.0.0'):
    def __init__(self, port=5000, host=''):
        self.host = host
        self.port = port

    def Run(self):
        run_thread = Thread(target=self.ServeAsync)
        run_thread.daemon = True
        run_thread.start()

    def ServeAsync(self):
        print time.asctime(), "serving at port", self.port
        handler = Handler
        handler.OnModuleRequest = self.OnModuleRequest
        httpServer = HTTPServer((self.host, self.port), handler)
        while True:
            httpServer.handle_request()

    def Stop(self):
        print time.asctime(), "server closed"

    def OnModuleRequest(self, moduleName, requestBody):
        print 'Module Request callback not set'
        print 'request body:', requestBody
        return {'Module Request callback not set'}


if __name__ == "__main__":
    server = Server()
    server.Run()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        server.Stop()
