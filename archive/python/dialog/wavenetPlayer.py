from pkg.utilities.requestsUtility import PostJson
import base64
import os

# if __name__ == "__main__":
#     DownloadTestFile('pkg/tmp/temp_audio.ogg')

# print res


class WavenetPlayer():
    def __init__(self, services):
        self.audioPlayer = services.audioPlayer

    def PlayWavenetFile(self, params):
        localPath = 'pkg/tmp/temp_audio.wav'
        self.DownloadWavenetFile(params['firebaseStoragePath'], localPath)
        fullPath = os.getcwd() + "/" + localPath
        # fullPath = "/home/nao/improvise/" + tempPath
        print 'playing audio'
        self.audioPlayer.playFile(fullPath)
        print 'audio played'

    def DownloadWavenetFile(self, firebaseStoragePath, localPath):
        body = {
            "sourcePath": firebaseStoragePath
        }
        url = 'http://us-central1-improvise-communicate.cloudfunctions.net/storageGet'
        res64 = PostJson(url, body)
        res = base64.b64decode(res64)
        file = open(localPath, 'wb')
        file.write(res)
        file.close()
