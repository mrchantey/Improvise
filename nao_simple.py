import qi
import sys
import time
# import os
# from pkg.modules.nao.modules.speechRecognition import SpeechRecognition
# from pkg.modules.nao.modules.services import ServiceModule
from pkg.modules.nao.modules.events import EventModule


class Nao():

    def __init__(self, ipAddress):
        self.app = qi.Application()
        self.session = qi.Session()
        self.session.connect('tcp://'+ipAddress+":9559")
        self.textToSpeech = self.session.service("ALTextToSpeech")
        # self.services = ServiceModule(self.session)
        # self.speechRecognition = SpeechRecognition(self.services)


if __name__ == "__main__":
    ipAddress = sys.argv[1]
    nao = Nao(ipAddress)
