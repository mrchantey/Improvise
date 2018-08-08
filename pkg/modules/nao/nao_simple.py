import qi
import sys


class Nao():

    def __init__(self, ipAddress):
        self.app = qi.Application()
        self.session = qi.Session()
        self.session.connect('tcp://'+ipAddress+":9559")
        self.textToSpeech = self.session.service("ALTextToSpeech")
        self.system = self.session.service("ALSystem")


if __name__ == "__main__":
    ipAddress = sys.argv[1]
    nao = Nao(ipAddress)
