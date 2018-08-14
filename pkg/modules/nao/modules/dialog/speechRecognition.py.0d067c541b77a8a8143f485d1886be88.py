
class SpeechDetection():
    def __init__(self, services, events, speechToText, speechCompletedCallback):
        self.speechCompletedCallback = speechCompletedCallback
        self.speechToText = speechToText
        # self.googleSpeechRecognition = GoogleSpeechRecognition()
        self.audioRecorder = services.audioRecorder
        events.AddListener("SpeechDetected", self.OnNativeSpeechDetected)
        self.speechToText.AddWords(["fdsjkfds"])
        self.StopRecording()

    def StartDetecting(self):
        self.speechToText.StartRecognizing()
        self.StartRecording()

    def StartRecording(self):
        # path = '/home/nao/recordings/last_sentence.wav'
        path = '/home/nao/custom/improvise/last_sentence.wav'
        channels = (0, 0, 1, 0)
        self.audioRecorder.startMicrophonesRecording(path, "wav", 16000, channels)

    def StopRecording(self):
        self.audioRecorder.stopMicrophonesRecording()

    def StopDetecting(self):
        self.speechToText.StopRecognizing()
        self.StopRecording()

    # will be a dummy placeholder word
    def OnNativeSpeechDetected(self, value):
        # if value == 1:
        #     print 'SPEECH ON'
        #     self.StartRecording()
        if value == 0:
            print 'SPEECH OFF'
            self.StopRecording()
            self.speechCompletedCallback()
            # responseText = self.googleSpeechRecognition.MakeRequest()
            # print "Response", responseText
