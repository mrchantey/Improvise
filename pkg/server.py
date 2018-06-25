# from __future__ import absolute_import
from flask import Flask, request, render_template, make_response
import sys
from utilservices import utility
import signal
import json
# from nao import naoInterface
# from tests import naoTest

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


def onRequestDialog(text):  # Dependency injected to this method
    return "dialog request not set\n" + text


@app.route('/dialog', methods=['GET', 'POST', 'OPTIONS'])  # Perhaps temporary
def handleRequestDialog():
    if request.method == 'GET':
        return respond(render_template('dialogIndex.html'), 200, 'text/html')
    elif request.method == 'OPTIONS':
        return preflightRespond()
    else:
        reqBody = utility.parseType(request.json)
        # print 'TODO HANDLE DIALOG POST REQUEST', reqBody
        if 'params' in reqBody:
            responseText = onRequestDialog('params'['text'])
            return respond({'responseText': responseText})


@app.route('/dialog/<text>')
def handleRequestDialogURL(text):
    whiteSpaceText = text.replace("_", " ")
    responseText = onRequestDialog(whiteSpaceText)
    return respond({'responseText': responseText})


def onRequestNao(reqType, **kwargs):  # Dependency injected to this method
    return "nao request not set"


@app.route('/nao/<reqType>/<reqName>/<param1>')
def handleRequestNaoParams(reqType, reqName, param1):
    return handleRequestNao(reqType, reqName, params=[param1])


@app.route('/nao/<reqType>/<reqName>', methods=['GET', 'POST', 'OPTIONS'])
def handleRequestNaoPost(reqType, reqName):
    if request.method == 'GET':
        return handleRequestNao(reqType, reqName)
    elif request.method == 'OPTIONS':
        return preflightRespond()
    else:
        reqBody = utility.parseType(request.json)
        if 'params' in reqBody:
            return handleRequestNao(reqType, reqName, params=reqBody['params'])
        else:
            return handleRequestNao(reqType, reqName)


def handleRequestNao(rawReqType, rawReqName, **kwargs):
    reqType = utility.parseType(rawReqType)
    reqName = utility.parseType(rawReqName)
    kwargs = utility.parseType(kwargs)
    kwargs['reqName'] = reqName
    responseJson = onRequestNao(reqType, **kwargs)
    # print 'sending response'
    # print responseJson
    return respond(responseJson)
