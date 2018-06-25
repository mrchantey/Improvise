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
        try:
            self.session.connect('tcp://'+ipAddress+":9559")
            self.services = ServiceModule(self.session)
            self.events = EventModule(self.services.memory)
            self.properties = PropertyModule(ipAddress, self.services)
            self.methods = MethodModule(self.services, self.events)
            self.actions = ActionModule(self.services, self.properties, self.methods)

        except RuntimeError:
            print 'Runtime Error, could not connect to robot'

    def HandleRequest(self, reqType, **kwargs):
        attr = getattr(self, reqType)
        response = attr.HandleRequest(kwargs)
        return response


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
