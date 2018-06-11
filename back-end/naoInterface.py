import qi
import sys
from naoqi import ALBroker


class NaoInterface():

    def __init__(self, ipAddress):
        self.session = qi.Session()
        self.properties = {}

        self.properties['isConnected'] = self.TryConnect(ipAddress)

        if self.properties['isConnected'] == False:
            return

    def GetProperty(self, propName):
        print 'property requested..', propName
        if propName == 'volume':
            return self.audioDevice.getOutputVolume()

    def SetProperty(self, propName, value):
        if propName == 'volume':
            self.audioDevice.setOutputVolume(value)

    def DoMethod(self, methName, param1):
        print 'doing method', methName, 'with parameter', param1, '..'
        if methName == 'SetAutoState':
            self.autonomousLife.setState(param1, _async=True)
        elif methName == 'SayPhrase':
            self.textToSpeech.say(param1, _async=True)

    def CloseSession(self):
        self.broker.shutdown()

    def TryConnect(self, ipAddress):
        try:
            self.broker = ALBroker("myBroker", '0.0.0.0', 0, ipAddress, 9559)

            self.session.connect('tcp://'+ipAddress)
            # print 'session connected at', ipAddress
#                        self.TextToSpeech = ALProxy("ALTextToSpeech", ipAddress, 9559)
#                        self.TextToSpeech = ALProxy("ALTextToSpeech")
            self.audioDevice = self.ConnectService("ALAudioDevice")
            # self.animatedSpeech = self.ConnectService("ALAnimatedSpeech")
            self.autonomousLife = self.ConnectService("ALAutonomousLife")
            self.behaviorManager = self.ConnectService("ALBehaviorManager")
            # self.memory = self.ConnectService("ALMemory")
            # self.peoplePerception = self.ConnectService("ALPeoplePerception")
            # self.photoCapture = self.ConnectService("ALPhotoCapture")
            # self.speechRecognition = self.ConnectService("ALSpeechRecognition")
            self.system = self.ConnectService("ALSystem")
            self.textToSpeech = self.ConnectService("ALTextToSpeech")
            # self.videoDevice = self.ConnectService("ALVideoDevice")

            self.properties['ipAddress'] = ipAddress
            self.properties['name'] = self.system.robotName()
            self.properties['volume'] = self.audioDevice.getOutputVolume()
            self.properties['behaviors'] = self.behaviorManager.getInstalledBehaviors(
            )
            self.properties['autoState'] = self.autonomousLife.getState()

            return True
        except RuntimeError:
            return False

    def ConnectService(self, serviceName):
        service = self.session.service(serviceName)
        print serviceName, 'connected!'
        return service


# BELOW FOR TESTING ONLY
if __name__ == "__main__":
    def printEvent(name, value):
        print name, value
    ipAddress = sys.argv[1]
    naoInterface = NaoInterface(ipAddress, printEvent)
    # naoSession.Connect()
    # naoSession.DoMethod(0, 'setAutoState', 'disabled')
    # naoSession.DoMethod(0, 'setAutoState', 'solitary')
    try:
        while True:
            pass
    except KeyboardInterrupt:
        pass
