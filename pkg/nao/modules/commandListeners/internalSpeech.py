

class InternalSpeechCommandListener():
    def __init__(self, eventModule, speechRecognitionModule, RunCommandCallback, presetCommands, alwaysListen=False):
        self.speechRecognitionModule = speechRecognitionModule
        self.RunCommandCallback = RunCommandCallback
        self.alwaysListen = alwaysListen
        self.presetCommands = presetCommands
        self.triggerPhrases = map(lambda cmd: cmd['name'], self.presetCommands)
        eventModule.AddListener("WordRecognized", self.OnWordRecognized)

    def StartListening(self):
        self.speechRecognitionModule.AddWords(self.triggerPhrases)
        self.speechRecognitionModule.StartRecognizing()

    def OnWordRecognized(self, word):
        self.StopListening()
        matchingCommand = filter(lambda cmd: cmd['name'] == word[0], self.presetCommands)
        if len(matchingCommand) > 0:
            # print 'WORD RECOGNIZED MATCH:', word
            # print matchingCommand[0]
            self.RunCommandCallback(matchingCommand[0])
        # if self.alwaysListen:
        #     self.StartListening()

    def StopListening(self):
        # print 'stopping listening'
        self.speechRecognitionModule.StopRecognizing()
        self.speechRecognitionModule.RemoveWords(self.triggerPhrases)
