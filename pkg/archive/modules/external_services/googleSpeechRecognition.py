import requests
import base64
import json

APIKEY = open("pkg/keys/improvise-communicate-api-key.txt").read()
GOOGLE_SPEECH_URL = "https://speech.googleapis.com/v1/speech:recognize?key={0}".format(APIKEY)


class GoogleSpeechRecognition():
    def __init__(self):
        pass

    def MakeRequest(self, localPath='last_sentence.wav'):
        audioData = self.GetAudioData(localPath)
        body = self.GetRequestBody(audioData)
        res = requests.post(GOOGLE_SPEECH_URL, body)
        resText = self.GetResponseText(res)
        return resText

    def GetAudioData(self, path):
        file = open(path, 'rb')
        file_content = file.read()
        file.close()
        file_content_64 = base64.b64encode(file_content)
        return file_content_64

    def GetRequestBody(self, audioData):
        body = {
            'config': {
                # 'encoding': 'LINEAR16',
                'sampleRateHertz': '16000',
                'languageCode': 'en-US'
            },
            'audio': {
                'content': audioData
            }
        }
        return json.dumps(body)

    def GetResponseText(self, response):
        if response.status_code == 200:
            data = response.json()
            result = data['results']
            if len(result) > 0:
                if len(result[0]['alternatives']) > 0:
                    text = result[0]['alternatives'][0]['transcript'].encode('utf')
                    return text
        else:
            print response.status_code
            print response.text.encode('utf8')
        return 'there was an error'
