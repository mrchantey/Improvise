

class SpeechRecognition():
    def __init__(self, services, expressions=True):
        services.autonomousMoves.setExpressiveListeningEnabled(False)

        self.speechRecognition = services.speechRecognition
        self.speechRecognition.setAudioExpression(expressions)
        self.speechRecognition.setVisualExpression(expressions)
        self.vocabulary = []
        self.ForceStop()
        self.isRunning = False
        # self.StartRecognizing()

    def StartRecognizing(self):
        if not self.isRunning:
            self.speechRecognition.subscribe("NaoSpeechRecognition")
            self.isRunning = True

    def ForceStop(self):
        try:
            self.speechRecognition.unsubscribe("NaoSpeechRecognition")
        except:
            pass

    def StopRecognizing(self):
        if self.isRunning:
            self.speechRecognition.unsubscribe("NaoSpeechRecognition")
            self.isRunning = False

    def AddWord(self, word, updateVocab=True):
        self.vocabulary.append(word)
        if updateVocab:
            self.UpdateVocabulary()

    def AddWords(self, words):
        for word in words:
            self.AddWord(word, False)
        self.UpdateVocabulary()

    def RemoveWord(self, word, updateVocab=True):
        while word in self.vocabulary:
            self.vocabulary.remove(word)
        if updateVocab:
            self.UpdateVocabulary()

    def RemoveWords(self, words):
        for word in words:
            self.RemoveWord(word, False)
        self.UpdateVocabulary()

    def UpdateVocabulary(self):
        if self.isRunning:
            self.StopRecognizing()
            self.speechRecognition.setVocabulary(self.vocabulary, False)
            self.StartRecognizing()
        else:
            self.speechRecognition.setVocabulary(self.vocabulary, False)
