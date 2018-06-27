

class MethodModule():

    def __init__(self, services, events):
        self.services = services
        self.events = events
        self.phraseQueue = []
        events.AddListener("ALTextToSpeech/TextDone", self.TextDoneListener)

    def HandleRequest(self, params):
        meth = getattr(self, params['methodName'])
        meth(params)
        return {'status': 'all good'}

    def DoMethod(self, methName, params):
        meth = getattr(self, methName)
        meth(params)

    def SetAutoState(self, requestBody):
        self.services.autonomousLife.setState(requestBody['state'], _async=True)

    def Say(self, params):
        isSpeaking = True if len(self.phraseQueue) > 0 else False
        phrase = params['phrase']
        animated = params['animated'] if 'animated' in params else False
        if type(phrase) == list:
            for i in range(0, len(phrase)):
                self.phraseQueue.append({'phrase': phrase[i], 'animated': animated})
        else:
            self.phraseQueue.append({'phrase': phrase, 'animated': animated})
        if isSpeaking == False:
            nextPhrase = self.phraseQueue.pop(0)
            self.BeginSpeaking(nextPhrase['phrase'], nextPhrase['animated'])

    def BeginSpeaking(self, phrase, animated):
        if animated == True:
            self.services.animatedSpeech.say(phrase, _async=True)
        else:
            self.services.textToSpeech.say(phrase, _async=True)

    def TextDoneListener(self, value):
        if value == 1 and len(self.phraseQueue) > 0:
            nextPhrase = self.phraseQueue.pop(0)
            self.BeginSpeaking(nextPhrase['phrase'], nextPhrase['animated'])

    def RunBehavior(self, params):
        self.services.behaviorManager.runBehavior(params['path'], _async=True)

    def PlayAudio(self, params):
        self.services.audioPlayer.playFile(params['path'], _async=True)
        # id = self.services.audioPlayer.loadFile(params[0])

    def StopAll(self, params=None):
        self.phraseQueue = []
        self.services.behaviorManager.stopAllBehaviors(_async=True)
        self.services.textToSpeech.stopAll(_async=True)
        self.services.audioPlayer.stopAll(_async=True)
