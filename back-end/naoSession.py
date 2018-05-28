import qi
import threading
import time


def runAsync(callback):
    thread = threading.Thread(target=callback)
    thread.daemon = True
    thread.start()


class NaoSession():
    def __init__(self):
        self.session = qi.Session()

    def Connect(self, ipAddress):
        try:
            self.session.connect('tcp://'+ipAddress)
            print 'session connected at', ipAddress
            self.TextToSpeech = self.session.service("ALTextToSpeech")
            return True
        except RuntimeError:
            return False

    def Say(self, phrase):
        self.TextToSpeech.say(phrase, _async=True)
