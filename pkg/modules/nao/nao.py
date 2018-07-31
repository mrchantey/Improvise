import qi
import sys
from modules.services import ServiceModule
from modules.properties import PropertyModule
from modules.methods import MethodModule
from modules.events import EventModule
from modules.actions.actions import ActionModule


class Nao():

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
            self.actions = ActionModule(self.properties, self.methods)
            self.isConnected = True

        except RuntimeError:
            print 'Runtime Error, could not connect to robot'

    def OnRequest(self, requestBody):
        attr = getattr(self, requestBody['module'])
        response = attr.HandleRequest(requestBody)
        return response


if __name__ == "__main__":
    ipAddress = sys.argv[1]
    nao = Nao(ipAddress)
    # nao.services.leds.fadeRGB("FaceLeds", 1, 0, 1, 4)
    # nao.services.leds.fadeRGB("FaceLeds", "green", 4)
    nao.methods.SetLeds({"name": "FaceLeds", "colorName": "green", "duration": 3})
    # nao.methods.Say({"phrase": "hello"})
    # for action in nao.actions.actions:
    #     print action
    # try:
    #     while True:
    #         pass
    # except KeyboardInterrupt:
    #     pass
