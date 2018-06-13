from flask import Flask, request, render_template, make_response
import sys
from utilservices import utility
import signal
import json
from nao import naoInterface
from tests import naoTest

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
    return respond(nao.propertyMod.GetBakedProperties())


@app.route('/action')
def handleAllActionRequest():
    return respond(nao.actionMod.GetBakedActions())


@app.route('/nao/<attrType>/<attrName>', methods=['GET', 'POST', 'OPTIONS'])
@app.route('/nao/<attrType>/<attrName>/<param1>/<param2>')
def handleNaoRequest(attrType, attrName=None, param1=None, param2=None)
    if request.method == 'OPTIONS':
        return preflightRespond()
    # parsing may not be nessecary for get requests
    attrType = utility.parseUnicode(attrType)
    if attrType == 'method':
        params = [param1, param2]
        handleMethodDo(attrName, params)
    elif attrType == 'property':
        if attrName == None:
            return respond(nao.propertyMod.GetBakedProperties())
        else:
            return handleProperty


@app.route('/property/<propName>', methods=['GET', 'POST', 'OPTIONS'])
def handlePropertyRequest(propName):
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
    methName = utility.parseUnicode(methName)
    params = utility.parseUnicode(request.json['params'])
    return handleMethodDo(methName, params)


@app.route('/action/<actionId>')
def handleActionRunRequest(actionId):
    actionId = utility.parseUnicode(actionId)
    return handleActionRun(actionId)


@app.route('/events/<drain>')
def handleEventsRequest(drain):
    bDrain = True if drain == 'true' else False
    return handleEventsGet(bDrain)


@app.route('/events', methods=['GET', 'POST', 'OPTIONS'])
def handleDefaultEventsRequest():
    if request.method == 'OPTIONS':
        return preflightRespond()
    elif request.method == 'POST':
        return handleEventsGet(request.json['drain'])
    else:
        return handleEventsGet(False)

# Really for testing and quick commands only--------------------------------------------------------------------------------


@app.route('/property/<propName>/<propValue>')
def handlePropertyGETSetRequest(propName, propValue):
    propName = utility.parseUnicode(propName)
    propValue = utility.parseUnicode(propValue)
    return handlePropertySet(propName, propValue)


@app.route('/method/<methName>/<param1>')
def handleMethodGETDoRequest(methName, param1):
    methName = utility.parseUnicode(methName)
    param1 = utility.parseUnicode(param1)
    return handleMethodDo(methName, [param1])
# -------------------------------------------------------------------------------------------------------


def handlePropertyGet(propName):
    print 'property get request..', propName
    propValue = nao.propertyMod.GetProperty(propName)
    return respond({'value': propValue})


def handlePropertySet(propName, propValue):
    # print 'property set request..', propName, type(propValue), propValue
    confirmedValue = nao.propertyMod.SetProperty(propName, propValue)
    return respond({'value': confirmedValue})


def handleMethodDo(methName, params):
    # print 'do method request..', methName
    nao.methodMod.DoMethod(methName, params)
    return respond({'methName': methName, 'methParams': params})


def handleActionRun(actionId):
    nao.actionMod.RunAction(actionId)
    return respond({'actionId': actionId})


def handleEventsGet(drainEvents):
    print 'get events request..'
    events = None
    if drainEvents == True:
        events = nao.eventMod.DrainEvents()
    else:
        events = nao.eventMod.eventPool
    for event in events:
        print event
    return respond(events)

# --------------------------------------------------------------------------------------------------------


if __name__ == '__main__':
    global nao
    if len(sys.argv) == 1:
        print 'no ip address entered..'
    else:
        ipAddress = utility.parseUnicode(sys.argv[1])
        print 'Robot connect attempt at', ipAddress, '..'
        nao = naoInterface.NaoInterface(ipAddress)
        if len(sys.argv) > 2:
            PORT = sys.argv[2]
        app.run(debug=True)
        try:
            while True:
                pass
        except KeyboardInterrupt:
            pass
