import qi
import sys
import time

# from pkg.modules.nao.modules.speechRecognition import SpeechRecognition
from pkg.modules.nao.modules.services import ServiceModule
from pkg.modules.nao.modules.events import EventModule
from pkg.modules.nao.modules.memory import MemoryModule
from pkg.testWaveNet import DownloadTestFile
from pkg.modules.nao.modules.dialog.dialog import DialogModule


class Nao():

    def __init__(self, ipAddress):
        self.app = qi.Application()
        self.session = qi.Session()
        self.session.connect('tcp://'+ipAddress+":9559")
        self.services = ServiceModule(self.session)
        # self.events = EventModule(self.services.memory)
        self.memory = MemoryModule(self.services.memory)
        # self.dialog = DialogModule(self.services, self.events)
        # self.textToSpeech = self.session.service("ALTextToSpeech")
        # self.audioPlayer = self.session.service("ALAudioPlayer")
        # self.speechRecognition = SpeechRecognition(self.services)


if __name__ == "__main__":
    ipAddress = sys.argv[1]
    nao = Nao(ipAddress)
    # nao.textToSpeech.say("hi there")
    # nao.memory.InsertData("physioDefaultRepetitions",1)
    print nao.memory.GetData("physioDefaultRepetitions")
    # print    nao.services.memory.getData("physioDefaultRepetitions")
    # try:
    #     while True:
    #         pass
    # except KeyboardInterrupt:
    #     pass
