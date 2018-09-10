import qi
import sys
from modules.services import ServiceModule
from modules.events import EventModule
from modules.command import CommandModule
from modules.speechRecognition import SpeechRecognitionModule

import time


class Nao():

    def __init__(self, ipAddress):
        self.app = qi.Application()
        self.session = qi.Session()
        self.properties = {}
        # self.isConnected = False
        # self.ftpClient.Login()
        try:
            self.session.connect('tcp://'+ipAddress+":9559")
            self.serviceModule = ServiceModule(self.session)
            self.eventModule = EventModule(self.serviceModule.memory)
            self.speechRecognitionModule = SpeechRecognitionModule(self.serviceModule, True, False)
            self.commandModule = CommandModule(self.serviceModule, self.eventModule, self.speechRecognitionModule)
            self.isConnected = True
        except RuntimeError:
            print 'Runtime Error, could not connect to robot'

    def OnRequest(self, requestBody):
        attr = getattr(self, requestBody['module'])
        response = attr.HandleRequest(requestBody)
        return response

    def ExitProgram(self):
        self.commandModule.StopAllListeners()
        self.commandModule.Run({
            "commandName": "naoqi",
            "serviceName": "ALAutonomousLife",
            "methodName": "setState",
            "param1": "disabled"
        })
        # self.dialog.End()
        # self.ftpClient.Logout()


if __name__ == "__main__":
    ipAddress = sys.argv[1]
    nao = Nao(ipAddress)
    nao.commandModule.StartAllListeners()
    try:
        while True:
            pass
    except KeyboardInterrupt:
        nao.ExitProgram()
        pass
