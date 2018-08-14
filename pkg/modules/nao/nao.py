import qi
import sys
from modules.services import ServiceModule
from modules.properties import PropertyModule
from modules.methods import MethodModule
from modules.events import EventModule
from modules.dialog.dialog import DialogModule
from modules.actions.actions import ActionModule
from modules.ftp import FTPModule

# FOR TESTING
from pkg.backEndClient import BackEndClient
import time


class Nao():

    def __init__(self, ipAddress, backEndClient):
        self.app = qi.Application()
        self.session = qi.Session()
        self.properties = {}
        # self.isConnected = False
        self.ftpClient = FTPModule(ipAddress)
        # self.ftpClient.Login()
        # try:
        self.session.connect('tcp://'+ipAddress+":9559")
        self.services = ServiceModule(self.session)
        self.events = EventModule(self.services.memory)
        self.dialog = DialogModule(self.ftpClient, backEndClient, self.services, self.events)
        self.properties = PropertyModule(ipAddress, self.services)
        self.methods = MethodModule(self.services, self.events, self.dialog.textToSpeech)
        self.actions = ActionModule(self.properties, self.methods)
        self.isConnected = True

        # except RuntimeError:
        # print 'Runtime Error, could not connect to robot'

    def OnRequest(self, requestBody):
        attr = getattr(self, requestBody['module'])
        response = attr.HandleRequest(requestBody)
        return response

    def ExitProgram(self):
        self.dialog.End()
        self.ftpClient.Logout()


if __name__ == "__main__":
    ipAddress = sys.argv[1]
    backEndClient = BackEndClient("127.0.0.1:3000")
    nao = Nao(ipAddress, backEndClient)
    nao.dialog.Begin()
    # # nao.services.Invoke("system", "shutdown")
    # # nao.speechRecognition.AddWords(["yes", "no", "freeze all motor functions"])
    # nao.speechRecognition.StartRecognizing()
    # lastSentence = nao.ftpClient.GetLastSentence()
    # print lastSentence
    try:
        while True:
            pass
    except KeyboardInterrupt:
        nao.ExitProgram()
        pass
