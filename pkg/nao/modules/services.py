

# This could be set up as a dictionary, may be neater and easier to work with

class ServiceModule():

    def __init__(self, session):
        self.session = session
        self.services = {}
        self.audioDevice = self.ConnectService("ALAudioDevice")
        self.audioPlayer = self.ConnectService("ALAudioPlayer")
        self.audioRecorder = self.ConnectService("ALAudioRecorder")
        self.animatedSpeech = self.ConnectService("ALAnimatedSpeech")
        self.autonomousLife = self.ConnectService("ALAutonomousLife")
        self.autonomousMoves = self.ConnectService("ALAutonomousMoves")
        self.behaviorManager = self.ConnectService("ALBehaviorManager")
        self.connectionManager = self.ConnectService("ALConnectionManager")
        self.ConnectService("ALMotion")
        self.memory = self.ConnectService("ALMemory")
        self.leds = self.ConnectService("ALLeds")
        # self.peoplePerception = self.ConnectService("ALPeoplePerception")
        # self.photoCapture = self.ConnectService("ALPhotoCapture")
        self.speechRecognition = self.ConnectService("ALSpeechRecognition")
        self.system = self.ConnectService("ALSystem")
        self.textToSpeech = self.ConnectService("ALTextToSpeech")
        print 'SERVICES CONNECTED'
        # self.videoDevice = self.ConnectService("ALVideoDevice")

    def ConnectService(self, serviceName):
        service = self.session.service(serviceName)
        self.services[serviceName] = service
        # print 'SERVICE CONNECTED', serviceName
        return service

    def Invoke(self, service, methodName):
        service = getattr(self, service)
        method = getattr(service, methodName)
        result = method()
        return result
