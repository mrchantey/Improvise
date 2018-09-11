

class SpeechRecognitionModule():
    def __init__(self, serviceModule, visualExpressions=True, audioExpressions=True):
        serviceModule.autonomousMoves.setExpressiveListeningEnabled(False)

        self.speechRecognition = serviceModule.speechRecognition
        self.speechRecognition.setAudioExpression(audioExpressions)
        self.speechRecognition.setVisualExpression(visualExpressions)
        self.vocabulary = []
        self.isRunning = False
        self.StopRecognizing(True)
        # self.UpdateVocabulary()
        # self.StartRecognizing()

    def StartRecognizing(self):
        if not self.isRunning:
            self.isRunning = True
            self.speechRecognition.subscribe("NaoSpeechRecognition")

    def StopRecognizing(self, forceStop=False):
        # if self.isRunning or forceStop == True:
        self.isRunning = False
        try:
            self.speechRecognition.unsubscribe("NaoSpeechRecognition")
        except:
            pass

    def AddWord(self, word, updateVocab=True):
        if not word in self.vocabulary:
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
        if len(self.vocabulary) == 0:
            self.vocabulary.append("supercalafragalisticexpialagotious")
        if self.isRunning:
            self.StopRecognizing()
            self.speechRecognition.setVocabulary(self.vocabulary, False)
            self.StartRecognizing()
        else:
            self.speechRecognition.setVocabulary(self.vocabulary, False)
