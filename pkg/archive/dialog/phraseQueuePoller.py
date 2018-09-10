
from threading import Thread
from pkg.utilities.requestsUtility import PostJson
import time
phraseQueueKey = "robot/phraseQueue"


class PhraseQueuePoller():
    def __init__(self, sayTextPhraseCallback, playWavenetCallback):
        self.delay = 3
        self.clear = True
        self.sayTextPhraseCallback = sayTextPhraseCallback
        self.playWavenetCallback = playWavenetCallback
        pollThread = Thread(name="phraseQueuePoller", target=self.PollPhraseQueue)
        pollThread.setDaemon(True)
        pollThread.start()

    def PollPhraseQueue(self):
        while True:
            print 'getting phrase queue...'
            phrases = self.GetPhraseQueue()
            textPhrases = filter(lambda p: p['type'] == 'text', phrases)
            for textPhrase in textPhrases:
                self.sayTextPhraseCallback(textPhrase)
            audioPhrases = filter(lambda p: p['type'] == 'audio', phrases)
            for audioPhrase in audioPhrases:
                self.playWavenetCallback(audioPhrase)
            time.sleep(self.delay)

    def GetPhraseQueue(self):
        body = {
            "key": phraseQueueKey
        }
        url = 'http://us-central1-improvise-communicate.cloudfunctions.net/databaseget'
        phrases = PostJson(url, body)
        if self.clear:
            self.ClearPhraseQueue()
        return phrases

    def ClearPhraseQueue(self):
        body = {
            "key": phraseQueueKey,
            "value": []
        }
        url = 'http://us-central1-improvise-communicate.cloudfunctions.net/databaseset'
        return PostJson(url, body)


if __name__ == '__main__':
    def PrintPhrase(phrase):
        print phrase
    phraseQueuePoller = PhraseQueuePoller(PrintPhrase, PrintPhrase)
    try:
        while True:
            time.sleep(0.1)
            print 'main thread running...'
    except KeyboardInterrupt:
        pass
