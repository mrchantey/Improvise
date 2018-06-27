import qi
import sys
from modules.services import ServiceModule
from modules.properties import PropertyModule
from modules.methods import MethodModule
from modules.events import EventModule
from modules.actions import ActionModule

# from naoqi import ALBroker


class NaoInterface():

    def __init__(self, ipAddress):
        self.app = qi.Application()
        self.session = qi.Session()
        self.properties = {}
        self.isConnected = False
        try:
            self.session.connect('tcp://'+ipAddress+":9559")
            self.services = ServiceModule(self.session)
            self.events = EventModule(self.services.memory)
            self.properties = PropertyModule(ipAddress, self.services)
            self.methods = MethodModule(self.services, self.events)
            self.actions = ActionModule(self.services, self.properties, self.methods)
            self.isConnected = True

        except RuntimeError:
            print 'Runtime Error, could not connect to robot'

    def OnRequest(self, requestBody):
        attr = getattr(self, requestBody['module'])
        response = attr.HandleRequest(requestBody)
        return response

# @app.route('/nao/<reqType>/<reqName>/<param1>')
# def handleRequestNaoParams(reqType, reqName, param1):
#     return handleRequestNao(reqType, reqName, params=[param1])


# @app.route('/nao/<reqType>/<reqName>', methods=['GET', 'POST', 'OPTIONS'])
# def handleRequestNaoPost(reqType, reqName):
#     if request.method == 'GET':
#         return handleRequestNao(reqType, reqName)
#     elif request.method == 'OPTIONS':
#         return preflightRespond()
#     else:
#         reqBody = utility.parseType(request.json)
#         if 'params' in reqBody:
#             return handleRequestNao(reqType, reqName, params=reqBody['params'])
#         else:
#             return handleRequestNao(reqType, reqName)


# def handleRequestNao(rawReqType, rawReqName, **kwargs):
#     reqType = utility.parseType(rawReqType)
#     reqName = utility.parseType(rawReqName)
#     kwargs = utility.parseType(kwargs)
#     kwargs['reqName'] = reqName
#     responseJson = onRequestNao(reqType, **kwargs)
#     # print 'sending response'
#     # print responseJson
#     return respond(responseJson)


if __name__ == "__main__":
    ipAddress = sys.argv[1]
    naoInterface = NaoInterface(ipAddress)
    naoInterface.methods.Say([["howdie", "lets count to 10", '1', '2', '3', '4'], False])
    naoInterface.methods.Say(["all done", False])
    # naoSession.Connect()
    # naoSession.DoMethod(0, 'setAutoState', 'disabled')
    # naoSession.DoMethod(0, 'setAutoState', 'solitary')
    try:
        while True:
            pass
    except KeyboardInterrupt:
        pass
