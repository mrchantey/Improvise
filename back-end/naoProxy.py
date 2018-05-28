from naoqi import ALProxy


class NaoProxy():
    def __init__(self):
        pass

    def Connect(self, ipAddress):
        print 'connecting to robot at', ipAddress, '...'
        try:
            self.TextToSpeech = ALProxy("ALTextToSpeech", ipAddress, 9559)
            print 'connected to robot at', ipAddress
            return True
        except RuntimeError:
            print 'could not connect to robot at', ipAddress
            return False
