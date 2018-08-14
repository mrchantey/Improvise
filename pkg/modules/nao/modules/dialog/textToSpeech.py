

class TextToSpeech():
    def __init__(self, services, events):
        self.services = services
        self.asyncPhraseQueue = []
        events.AddListener("ALTextToSpeech/TextDone", self.TextDoneListener)

    def Say(self, params):
        phrases = self.ParsePhraseParams(params)
        if params['async'] == True:
            isSpeakingAsync = False if len(self.asyncPhraseQueue) == 0 else True
            self.asyncPhraseQueue += phrases
            if not isSpeakingAsync:
                self.SayNextInQueue()
        else:
            for phrase in phrases:
                self.Speak(phrase)

    def ParsePhraseParams(self, params):
        phrase = params['phrase']
        animated = params['animated'] if 'animated' in params else False
        if type(phrase) == list:
            return map(lambda p: {'phrase': p, 'animated': animated, 'async': params['async']}, phrase)
        else:
            return [{'phrase': phrase, 'animated': animated, 'async': params['async']}]

    def SayNextInQueue(self):
        nextPhrase = self.asyncPhraseQueue.pop(0)
        self.Speak(nextPhrase)

    def Speak(self, phraseParams):
        print 'Saying', phraseParams['phrase']
        if phraseParams['animated'] == True:
            self.services.animatedSpeech.say(phraseParams['phrase'], _async=phraseParams['async'])
        else:
            self.services.textToSpeech.say(phraseParams['phrase'], _async=phraseParams['async'])

    def TextDoneListener(self, value):
        if value == 1 and len(self.asyncPhraseQueue) > 0:
            self.SayNextInQueue()
