# from __future__ import absolute_import
# sys.path.append("C:/Users/yellowcat/Documents/GitHub/Improvise/back-end")
import sys
import pkg.server as server

from pkg.dialog import dialogInterface
from pkg.nao.naoInterface import NaoInterface


def NaoConverseCallback(text):
    # response = dialog_client.MakeRequest(text)
    response = dialogInterface.Converse(text)
    nao.methods.DoMethod('Say', [response['responseText']])
    return response['responseText']


def ConverseCallback(text):
    response = dialogInterface.Converse(text)
    return response['responseText']


nao = None

if len(sys.argv) != 1:
    ipAddress = sys.argv[1]
    nao = NaoInterface(ipAddress)
    server.onRequestDialog = NaoConverseCallback
    server.onRequestNao = nao.HandleRequest
else:
    print 'NO IP ADDRESS SET, ROBOT NOT CONNECTED..'
    server.onRequestDialog = ConverseCallback

# server.app.run(debug=True, port=server.PORT)
