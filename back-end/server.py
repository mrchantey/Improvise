from flask import Flask, request, render_template, make_response
import sys
import utility
import signal
import json
from naoInterface import NaoInterface
from naoTest import NaoTest
from eventListener import CreateEventListener

PORT = 5000
# nao = None
eventListener = None
app = Flask(__name__)
eventStack = []


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


# @app.route('/cors', methods=['POST', 'GET', 'OPTIONS'])
# def handleAllow():
#     if request.method == 'OPTIONS':
#         return preflightRespond()
#     return respond({'name': 'peter', 'age': 21})

@app.route('/property')
def handleAllPropertyRequest():
    if nao == None:
        return respond('', 204)
    return respond(nao.properties)


@app.route('/property/<propName>', methods=['GET', 'POST', 'OPTIONS'])
def handlePropertyRequest(propName):
    if request.method == 'OPTIONS':
        return preflightRespond()
    if nao == None:
        return respond('', 204)
    propName = utility.parseUnicode(propName)
    if request.method == 'GET':
        return handlePropertyGet(propName)
    elif request.method == 'POST':
        propValue = utility.parseUnicode(request.json['value'])
        return handlePropertySet(propName, propValue)


@app.route('/method/<methName>', methods=['POST', 'OPTIONS'])
def handleMethodRequest(methName):
    if request.method == 'OPTIONS':
        return preflightRespond()
    if nao == None:
        return respond('', 204)
    methName = utility.parseUnicode(methName)
    param1 = utility.parseUnicode(request.json['param1'])
    return handleMethodDo(methName, param1)

# Really for testing and quick commands only--------------------------------------------------------------------------------


@app.route('/property/<propName>/<propValue>')
def handlePropertyGETSetRequest(propName, propValue):
    if nao == None:
        return respond('', 204)
    propName = utility.parseUnicode(propName)
    propValue = utility.parseUnicode(propValue)
    return handlePropertySet(propName, propValue)


@app.route('/method/<methName>/<param1>')
def handleMethodGETDoRequest(methName, param1):
    if nao == None:
        return respond('', 204)
    methName = utility.parseUnicode(methName)
    param1 = utility.parseUnicode(param1)
    return handleMethodDo(methName, param1)
# -------------------------------------------------------------------------------------------------------


def handlePropertyGet(propName):
    print 'property get request..', propName
    propValue = nao.GetProperty(propName)
    return respond({'value': propValue})


def handlePropertySet(propName, propValue):
    # print 'property set request..', propName, type(propValue), propValue
    nao.SetProperty(propName, propValue)
    propValue = nao.GetProperty(propName)
    return respond({'value': propValue})


def handleMethodDo(methName, param1):
    print 'do method request..', methName, type(param1), param1
    nao.DoMethod(methName, param1)
    return respond({'methName': methName, 'methParam1': param1})


def storeEvent(eventName, eventValue):
    global eventStack
    eventStack.append({'name': eventName, 'value': eventValue})


@app.route('/event')
def giveEvents():
    global eventStack
    events = eventStack
    eventStack = []
    print 'giving events', events
    return respond(json.dumps(events))
    # socketio.emit("RobotEventTrigger", data)

# --------------------------------------------------------------------------------------------------------


def ConnectRobot(ipAddress):
    ipAddress = utility.parseUnicode(ipAddress)
    print 'Robot connect attempt at', ipAddress, '..'
    global nao
    if nao != None:
        if nao.properties['isConnected'] == True:
            nao.CloseSession()
    nao = NaoInterface(ipAddress)

    if nao.properties['isConnected'] == True:
        print 'nao connection succeeded..'
        global eventListener
        # try:
        # eventListener = CreateEventListener(storeEvent)
        # except:
        # print 'event listener already registered', eventListener
    else:
        print 'nao connection failed..'


if __name__ == '__main__':
    if len(sys.argv) > 1:
        ConnectRobot(sys.argv[1])
    else:
        global nao
        nao = NaoTest()
    if len(sys.argv) > 2:
        PORT = sys.argv[2]
    app.run(debug=True)
    try:
        while True:
            pass
    except KeyboardInterrupt:
        pass
