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
            self.serviceMod = ServiceModule(self.session)
            self.propertyMod = PropertyModule(ipAddress, self.serviceMod)
            self.methodMod = MethodModule(self.serviceMod)
            self.eventMod = EventModule(self.serviceMod.memory)
            self.actionMod = ActionModule(self.serviceMod, self.propertyMod, self.methodMod)

        except RuntimeError:
            print 'Runtime Error, could not connect to robot'


# BELOW FOR TESTING ONLY
if __name__ == "__main__":
    ipAddress = sys.argv[1]
    naoInterface = NaoInterface(ipAddress)
    naoInterface.methodMod.Say(["howdie", False])
    # naoSession.Connect()
    # naoSession.DoMethod(0, 'setAutoState', 'disabled')
    # naoSession.DoMethod(0, 'setAutoState', 'solitary')
    try:
        while True:
            pass
    except KeyboardInterrupt:
        pass
