

# This could be set up as a dictionary, may be neater and easier to work with

class ServiceModule():

    def __init__(self, session):
        self.session = session
        self.audioDevice = self.ConnectService("ALAudioDevice")
        self.audioPlayer = self.ConnectService("ALAudioPlayer")
        self.animatedSpeech = self.ConnectService("ALAnimatedSpeech")
        self.autonomousLife = self.ConnectService("ALAutonomousLife")
        self.behaviorManager = self.ConnectService("ALBehaviorManager")
        self.memory = self.ConnectService("ALMemory")
        self.leds = self.ConnectService("ALLeds")
        # self.peoplePerception = self.ConnectService("ALPeoplePerception")
        # self.photoCapture = self.ConnectService("ALPhotoCapture")
        # self.speechRecognition = self.ConnectService("ALSpeechRecognition")
        self.system = self.ConnectService("ALSystem")
        self.textToSpeech = self.ConnectService("ALTextToSpeech")
        # self.videoDevice = self.ConnectService("ALVideoDevice")

    def ConnectService(self, serviceName):
        service = self.session.service(serviceName)
        print 'SERVICE CONNECTED', serviceName
        return service
