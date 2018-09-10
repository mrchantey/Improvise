# from speechToText import SpeechToText
from textToSpeech import TextToSpeech
from wavenetPlayer import WavenetPlayer
from phraseQueuePoller import PhraseQueuePoller
from speechDetection import SpeechDetection
import base64


class DialogModule():
    def __init__(self, services, events):
        # self.speechToText = SpeechToText(services, True, False)
        # self.speechDetection = SpeechDetection(services, events, self.speechToText, self.OnSpeechCompleted)
        self.textToSpeech = TextToSpeech(services, events)
        self.wavenetPlayer = WavenetPlayer(services)
        self.phraseQueuePoller = PhraseQueuePoller(self.textToSpeech.Say,self.wavenetPlayer.PlayWavenetFile)

    # def Begin(self):
    #     # self.textToSpeech.Say({'phrase': 'hi there', 'async': False})
    #     self.speechDetection.StartDetecting()

    # def End(self):
    #     # self.textToSpeech.Say({'phrase': 'goodbye', 'async': False})
    #     self.speechDetection.StopDetecting()

    # def OnSpeechCompleted(self):
    #     # # THIS WILL BE DIFFERENT IN DEPLOYMENT MODE
    #     # audio_bits = self.ftpClient.GetLastSentence()
    #     # print 'audio retrieved, size:', len(audio_bits), 'bits'
    #     # audio_bytes = base64.b64encode(audio_bits)
    #     # requestBody = {
    #     #     'audioBytes': audio_bytes
    #     # }
    #     # # response = self.backEndClient.MakeRequest(requestBody)
    #     # print 'RESPONSE RECEIVED:'
    #     # # print response

    #     # # if type(response) == dict and 'text' in response:
    #     #     # responseText = response['text']
    #     #     # print responseText
    #     #     # self.textToSpeech.Say({'phrase': responseText, 'async': False})
        # self.Begin()
