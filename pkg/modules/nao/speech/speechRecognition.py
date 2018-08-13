

from nativeSpeechRecognition import NativeSpeechRecognition
from pkg.modules.external_services.googleSpeechRecognition import GoogleSpeechRecognition


class SpeechRecognition():
    def __init__(self, services, events):
        self.nativeSpeechRecognition = NativeSpeechRecognition(services, True, False)
        self.googleSpeechRecognition = GoogleSpeechRecognition()
        self.audioRecorder = services.audioRecorder
        events.AddListener("SpeechDetected", self.OnNativeSpeechDetected)
        self.nativeSpeechRecognition.AddWords(["fdsjkfds"])
        self.StopRecording()

    def StartRecognizing(self):
        self.nativeSpeechRecognition.StartRecognizing()
        self.StartRecording()

    def StartRecording(self):
        # path = '/home/nao/recordings/last_sentence.wav'
        path = '/home/nao/custom/improvise/last_sentence.wav'
        channels = (0, 0, 1, 0)
        self.audioRecorder.startMicrophonesRecording(path, "wav", 16000, channels)

    def StopRecording(self):
        self.audioRecorder.stopMicrophonesRecording()

    def StopRecognizing(self):
        self.nativeSpeechRecognition.StopRecognizing()
        self.StopRecording()

    # will be a dummy placeholder word
    def OnNativeSpeechDetected(self, value):
        # if value == 1:
        #     print 'SPEECH ON'
        #     self.StartRecording()
        if value == 0:
            print 'SPEECH OFF'
            self.StopRecording()
            responseText = self.googleSpeechRecognition.MakeRequest()
            print "Response", responseText
