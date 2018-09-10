import qi
import sys
import time

# from pkg.nao.modules.speechRecognition import SpeechRecognition
from pkg.nao.modules.services import ServiceModule
from pkg.nao.modules.events import EventModule
from pkg.nao.modules.speechRecognition import SpeechRecognitionModule
# from pkg.nao.modules.textToSpeech import TextToSpeechModule
# from pkg.nao.modules.memory import MemoryModule
from pkg.nao.nao import Nao
# from pkg.testWaveNet import DownloadTestFile
# from pkg.nao.modules.dialog.dialog import DialogModule

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

    # nao.commandModule.Run({"commandName": "say", "phrase": "im a cowboy"})
    # nao.commandModule.Run({
    #     "commandName": "naoqi",
    #     "serviceName": "ALTextToSpeech",
    #     "methodName": "say",
    #     "param1": "im going to jump over the moon"
    # })
    # vol = nao.commandModule.Run({
    #     "commandName": "property",
    #     "propertyName": "volume",
    #     "propertyValue": 40
    # })
    # print "volume:", vol
