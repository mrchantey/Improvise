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
        pathParams = self.GetPathParams()
        if self.path == '/':
            print 'home request'
            self.RespondHome()
        else:
            self.RespondFile(self.path)
        # else:
        #     self.RespondError()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_POST(self):
        reqBody = self.GetRequestBody()
        pathParams = self.GetPathParams()
        if pathParams[1] == 'modules':
            resBody = self.OnRequest(pathParams[2], reqBody)
            self.RespondJson(resBody)
        else:
            self.RespondError()
        # injected method
        # resBody = self.OnRequest(pathParams, reqBody)

    def GetRequestBody(self):
        contentLength = int(self.headers.getheader('content-length', 0))
        bodyStr = self.rfile.read(contentLength)
        bodyObj = json.loads(bodyStr)
        bodyObjClean = utility.parseType(bodyObj)
        return bodyObjClean

    def GetPathParams(self):
        paramsRaw = self.path.split('/')
        params = utility.parseType(paramsRaw)
        return params

    def RespondError(self, statusCode=404):
        self.send_response(statusCode)
        self.end_headers()

    def RespondHome(self):
        self.RespondIPSetter()

    def RespondIPSetter(self):
        file = open('html/ipsetter.html')
        fileTxt = file.read()
        fileTxt = fileTxt.replace('INSERT IP ADDRESS', self.server_address)
        self.RespondString(fileTxt, 'text/html')

    def RespondJson(self, resBody):
        bodyStr = json.dumps(resBody)
        self.RespondString(bodyStr, 'application/json')

    def RespondFile(self, path):
        file = open('html' + path, 'r')
        resBody = file.read()
        mimeType = utility.GetMimeType(path)
        self.RespondString(resBody, mimeType)

    def RespondString(self, resBody, mimeType):
        self.send_response(200)
        self.send_header('Content-Type', mimeType)
        self.end_headers()
        self.wfile.write(resBody)

    # this should be called for preflight responses
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With')
        self.send_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.send_header('Access-Control-Max-Age', 86400)  # 24hr validation of preflight
        BaseHTTPRequestHandler.end_headers(self)


class Server():
    def __init__(self, port, ipAddress, host='0.0.0.0'):
        # def __init__(self, port=5000, host=''):
        self.address = 'http://' + ipAddress + ":" + str(port)
        self.host = host
        self.port = port
        self.RequestCallback = self.EmptyRequestCallback

    def Run(self):
        run_thread = Thread(target=self.ServeAsync)
        run_thread.daemon = True
        run_thread.start()

    def ServeAsync(self):
        print time.asctime(), "serving at port", self.port
        handler = Handler
        handler.OnRequest = self.OnRequest
        handler.server_address = self.address
        httpServer = HTTPServer((self.host, self.port), handler)
        httpServer.serve_forever()
        # while True:
        #     httpServer.handle_request()

    def Stop(self):
        print time.asctime(), "server closed"

    def OnRequest(self, moduleName, body):
        return self.RequestCallback(moduleName, body)

    def EmptyRequestCallback(self, moduleName, body):
        print 'Request callback not set'
        print 'request body:', body
        return {'Request callback not set'}


if __name__ == "__main__":
    server = Server(5000, '127.0.0.1')
    server.Run()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        server.Stop()
