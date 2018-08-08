import qi
import sys
import requests


class Nao():

    def __init__(self, ipAddress):
        self.app = qi.Application()
        self.session = qi.Session()
        self.session.connect('tcp://'+ipAddress+":9559")
        self.textToSpeech = self.session.service("ALTextToSpeech")
        self.system = self.session.service("ALSystem")
        # self.connectionManager = self.session.service("ALConnectionManager")


if __name__ == "__main__":
    ipAddress = sys.argv[1]
    nao = Nao(ipAddress)
    # for attr in nao.connectionManager.services()[0]:
    #     print attr
    nao.system.shutdown()
    # nao.system.reboot()
    res = requests.get("http://10.50.16.50:3000")
    print 'status', res.status_code
    print 'text', res.text
    resJson = res.json()
    print 'json', resJson

    # nao.textToSpeech.say(resJson['message'])
    # try:
    #     while True:
    #         pass
    # except KeyboardInterrupt:
    #     pass
