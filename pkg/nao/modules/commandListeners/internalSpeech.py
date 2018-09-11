

class InternalSpeechCommandListener():
    def __init__(self, eventModule, speechRecognitionModule, RunCommandCallback, speechCommands, alwaysListen=False):
        self.speechRecognitionModule = speechRecognitionModule
        self.RunCommandCallback = RunCommandCallback
        self.alwaysListen = alwaysListen
        self.speechCommands = speechCommands
        self.triggerPhrases = map(lambda cmd: cmd['triggerPhrase'], self.speechCommands)
        eventModule.AddListener("WordRecognized", self.OnWordRecognized)

    def StartListening(self):
        self.speechRecognitionModule.AddWords(self.triggerPhrases)
        self.speechRecognitionModule.StartRecognizing()

    def OnWordRecognized(self, word):
        self.StopListening()
        matchingCommand = filter(lambda cmd: cmd['triggerPhrase'] == word[0], self.speechCommands)
        if len(matchingCommand) > 0:
            print 'WORD RECOGNIZED MATCH:', word
            self.RunCommandCallback(matchingCommand[0])
        # if self.alwaysListen:
        #     self.StartListening()

    def StopListening(self):
        # print 'stopping listening'
        self.speechRecognitionModule.StopRecognizing()
        self.speechRecognitionModule.RemoveWords(self.triggerPhrases)
