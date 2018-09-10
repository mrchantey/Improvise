

class InternalSpeechCommandListener():
    def __init__(self, eventModule, speechRecognitionModule, RunCommandCallback, speechCommands, alwaysListen=False):
        self.eventModule = eventModule
        self.speechRecognitionModule = speechRecognitionModule
        self.RunCommandCallback = RunCommandCallback
        self.alwaysListen = alwaysListen
        self.wordRecognizedListener = None
        self.headTouchedListeners = self.SubscribeToHeadTouch()
        self.speechCommands = speechCommands
        self.triggerPhrases = map(lambda cmd: cmd['triggerPhrase'], self.speechCommands)

    def SubscribeToHeadTouch(self):
        return self.eventModule.AddListeners(["FrontTactilTouched",
                                              "MiddleTactilTouched",
                                              "RearTactilTouched"],
                                             self.OnHeadTouched)

    def StartListening(self):
        self.speechRecognitionModule.AddWords(self.triggerPhrases)
        self.speechRecognitionModule.StartRecognizing()
        self.wordRecognizedListener = self.eventModule.AddListener("WordRecognized", self.OnWordRecognized)

    def OnWordRecognized(self, word):
        self.StopListening()
        matchingCommand = filter(lambda cmd: cmd['triggerPhrase'] == word[0], self.speechCommands)
        if len(matchingCommand) == 0:
            return
        self.RunCommandCallback(matchingCommand[0])
        if self.alwaysListen:
            self.StartListening()

    def OnHeadTouched(self, val):
        if not val == 1:
            return
        self.StartListening()

    def StopListening(self):
        self.speechRecognitionModule.RemoveWords(self.triggerPhrases)
        self.speechRecognitionModule.StopRecognizing()
        self.eventModule.RemoveListener(self.wordRecognizedListener)
