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


@app.route('/nao/<attrType>')
@app.route('/nao/<attrType>/<attrName>', methods=['GET', 'POST', 'OPTIONS'])
@app.route('/nao/<attrType>/<attrName>/<param1>')
@app.route('/nao/<attrType>/<attrName>/<param1>/<param2>')
def handleNaoRequest(attrType, attrName=None, param1=None, param2=None):
        # parsing may not be nessecary for get requests
    if request.method == 'OPTIONS':
        return preflightRespond()
    attrType = utility.parseUnicode(attrType)
    attrName = utility.parseUnicode(attrName)
    param1 = utility.parseUnicode(param1)
    param2 = utility.parseUnicode(param2)
    if attrType == 'method':
        params = request.json['params'] if request.method == 'POST' else [param1, param2]
        return handleMethodDo(attrName, params)
    elif attrType == 'property':
        if attrName == None:
            return respond(nao.propertyMod.GetBakedProperties())
        elif request.method == 'POST':
            value = utility.parseUnicode(request.json['value'])
            return handlePropertySet(attrName, value)
        elif param1 != None:
            return handlePropertySet(attrName, param1)
        else:
            return handlePropertyGet(attrName)
    elif attrType == 'action':
        if attrName == None:
            return respond(nao.actionMod.GetBakedActions())
        else:
            return handleActionRun(attrName)
    elif attrType == 'events':
        if request.method == 'POST':
            return handleEventsGet(utility.parseUnicode(request.json))
        else:
            return handleEventsGet(param1)


# ----------------GETTING THERE------------------

def handlePropertyRequest():
    pass


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


def handleEventsGet(drainEvents=None):
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
