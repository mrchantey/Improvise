import sys
import server
from dialog import dialog_client
from nao.naoInterface import NaoInterface


def printText(text):
    print text
    return 'text printed\n'+text


def makeDialogRequest(text):
    response = dialog_client.MakeRequest(text)
    nao.methods.DoMethod('Say', [response])
    return response


nao = None

if len(sys.argv) != 1:
    ipAddress = sys.argv[1]
    nao = NaoInterface(ipAddress)
    server.onRequestDialog = makeDialogRequest
    server.onRequestNao = nao.HandleRequest
else:
    server.onRequestDialog = dialog_client.MakeRequest
    print 'NO IP ADDRESS SET, ROBOT NOT CONNECTED..'

server.app.run(debug=True, port=server.PORT)
