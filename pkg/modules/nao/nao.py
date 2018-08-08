import qi
import sys
from modules.services import ServiceModule
from modules.properties import PropertyModule
from modules.methods import MethodModule
from modules.events import EventModule
from modules.speechRecognition import SpeechRecognition
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
            self.speechRecognition = SpeechRecognition(self.services)
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

    def ExitProgram(self):
        self.speechRecognition.StopRecognizing()


if __name__ == "__main__":
    ipAddress = sys.argv[1]
    nao = Nao(ipAddress)
    nao.services.Invoke("system", "shutdown")
    # nao.speechRecognition.AddWords(["yes", "no", "freeze all motor functions"])
    # nao.speechRecognition.StartRecognizing()
    try:
        while True:
            pass
    except KeyboardInterrupt:
        nao.ExitProgram()
        pass
