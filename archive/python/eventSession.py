import qi


class TestClass():

    def __init__(self, ipAddress):
        self.app = qi.Application()
        self.session = qi.Session()
        self.session.connect("tcp://"+ipAddress+":9559")
        self.memory = self.session.service("ALMemory")
        self.tts = self.session.service("ALTextToSpeech")
        self.subscriber = self.memory.subscriber('ALTextToSpeech/CurrentSentence')

        def onEvent(val):
            print "event happened", val
        self.subscriber.signal.connect(onEvent)
        self.tts.say("Hello mr person", _async=True)


if __name__ == "__main__":
    ipAddress = "10.50.16.54"
    testo = TestClass(ipAddress)
    try:
        while True:
            pass
    except KeyboardInterrupt:
        pass
