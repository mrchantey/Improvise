

class MethodModule():

    def __init__(self, services, events):
        self.services = services
        self.events = events
        self.phraseQueue = []
        events.AddListener("ALTextToSpeech/TextDone", self.TextDoneListener)

    def HandleRequest(self, kwargs):
        meth = getattr(self, kwargs['reqName'])
        if 'params' in kwargs:
            meth(kwargs['params'])
        else:
            meth()
        return {'status': 'all good'}

    def DoMethod(self, methName, params):
        meth = getattr(self, methName)
        meth(params)

    def SetAutoState(self, params):
        self.services.autonomousLife.setState(params[0], _async=True)

    def Say(self, params):
        isSpeaking = True if len(self.phraseQueue) > 0 else False
        animated = params[1] if len(params) > 1 else False
        if type(params[0]) == list:
            for i in range(0, len(params[0])):
                self.phraseQueue.append({'phrase': params[0][i], 'animated': animated})
        else:
            self.phraseQueue.append({'phrase': params[0], 'animated': animated})
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
        self.services.behaviorManager.runBehavior(params[0], _async=True)

    def PlayAudio(self, params):
        self.services.audioPlayer.playFile(params[0], _async=True)
        # id = self.services.audioPlayer.loadFile(params[0])

    def StopAll(self):
        self.phraseQueue = []
        self.services.behaviorManager.stopAllBehaviors(_async=True)
        self.services.textToSpeech.stopAll(_async=True)
        self.services.audioPlayer.stopAll(_async=True)
