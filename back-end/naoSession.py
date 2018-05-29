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
            # print 'session connected at', ipAddress
#                        self.TextToSpeech = ALProxy("ALTextToSpeech", ipAddress, 9559)

            # self.AudioDevice = self.ConnectService("ALAudioDevice")
            # self.AnimatedSpeech = self.ConnectService("ALAnimatedSpeech")
            # self.AutonomousLife = self.ConnectService("ALAutonomousLife")
            self.BehaviorManager = self.ConnectService("ALBehaviorManager")
            self.System = self.ConnectService("ALSystem")
            # self.Memory = self.ConnectService("ALMemory")
            # self.PeoplePerception = self.ConnectService("ALPeoplePerception")
            # self.PhotoCapture = self.ConnectService("ALPhotoCapture")
            # self.SpeechRecognition = self.ConnectService("ALSpeechRecognition")
            # self.TextToSpeech = self.ConnectService("ALTextToSpeech")
            # self.VideoDevice = self.ConnectService("ALVideoDevice")
            # self.TextToSpeech = self.session.service("ALTextToSpeech")

            return True
        except RuntimeError:
            return False

    # def Say(self, phrase):
    #     self.TextToSpeech.say(phrase, _async=True)

    def ConnectService(self, serviceName):
        service = self.session.service(serviceName)
        print '\n', serviceName, 'connected!'
        return service
