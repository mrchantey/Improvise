from flask import Flask, request, render_template, make_response
from pkg.utilservices import utility
import json

PORT = 5000
app = Flask(__name__)


def respond(body, status=200, contentType="application/json"):
    if contentType == 'application/json':
        body = json.dumps(body)
    response = make_response(body, status)
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = contentType
    # response.headers.update(headers)
    return response


def preflightRespond():
    response = make_response('', 200)
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = ['POST', 'GET', 'OPTIONS']
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Max-Age'] = 86400
    return response


@app.route('/')
def handleIndex():
    return respond(render_template('index.html'), 200, 'text/html')


# @app.route('/modules/<moduleName>', methods=["GET"])
# @app.route('/modules/<moduleName>/<key1>/<val1>')
# @app.route('/modules/<moduleName>/<key1>/<val1>/<key2>/<val2>')
# @app.route('/modules/<moduleName>/<key1>/<val1>/<key2>/<val2>/<key3>/<val3>')
# def handleModuleGetRequest(moduleName, key1='key1', val1=None, key2='key2', val2=None, key3='key3', val3=None):
#     moduleName = utility.parseType(moduleName)
#     key1 = utility.parseType(key1)
#     val1 = utility.parseType(val1)
#     key2 = utility.parseType(key2)
#     val2 = utility.parseType(val2)
#     key3 = utility.parseType(key3)
#     val3 = utility.parseType(val3)
#     requestBody = {}
#     requestBody[key1] = val1
#     requestBody[key2] = val2
#     requestBody[key3] = val3
#     response = OnModuleRequest(moduleName, requestBody)
#     return respond(response)


@app.route('/modules/<moduleName>', methods=['OPTIONS', 'POST'])
def handleModulePostRequest(moduleName):
    if request.method == 'OPTIONS':
        return preflightRespond()
    else:
        moduleName = utility.parseType(moduleName)
        requestBody = utility.parseType(request.json)
        response = OnModuleRequest(moduleName, requestBody)
        return respond(response)


def OnModuleRequest(moduleName, requestBody):
    print "UNFULFILLED REQUEST DEPENDENCY"
    return {"unfulfilled request": "you sent " + moduleName + "\n" + requestBody}


if __name__ == "__main__":
    app.run(port=PORT, host="0.0.0.0")
