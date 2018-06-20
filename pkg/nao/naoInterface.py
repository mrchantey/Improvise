import qi
import sys
from serviceModule import ServiceModule
from propertyModule import PropertyModule
from methodModule import MethodModule
from eventModule import EventModule
from actionModule import ActionModule

# from naoqi import ALBroker


class NaoInterface():

    def __init__(self, ipAddress):
        self.app = qi.Application()
        self.session = qi.Session()
        self.properties = {}
        try:
            self.session.connect('tcp://'+ipAddress+":9559")
            self.services = ServiceModule(self.session)
            self.properties = PropertyModule(ipAddress, self.services)
            self.methods = MethodModule(self.services)
            self.events = EventModule(self.services.memory)
            self.actions = ActionModule(self.services, self.properties, self.methods)

        except RuntimeError:
            print 'Runtime Error, could not connect to robot'

    def HandleRequest(self, reqType, **kwargs):
        attr = getattr(self, reqType)
        response = attr.HandleRequest(kwargs)
        return response

        # BELOW FOR TESTING ONLY
if __name__ == "__main__":
    ipAddress = sys.argv[1]
    naoInterface = NaoInterface(ipAddress)
    naoInterface.methods.Say(["howdie", False])
    # naoSession.Connect()
    # naoSession.DoMethod(0, 'setAutoState', 'disabled')
    # naoSession.DoMethod(0, 'setAutoState', 'solitary')
    try:
        while True:
            pass
    except KeyboardInterrupt:
        pass
