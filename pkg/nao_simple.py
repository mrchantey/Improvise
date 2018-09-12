import qi
import sys
import time

from pkg.nao.nao import Nao

if __name__ == "__main__":
    nao = None

    def ExitProgram():
        nao.ExitProgram()
    ipAddress = sys.argv[1]
    nao = Nao(ipAddress, ExitProgram, 'stand')

    nao.StartProgram()
    alMotion = nao.serviceModule.services['ALMotion']
    # alMotion.wbEnable(True)

    print 'fall manager enabled:', alMotion.getFallManagerEnabled()
    alMotion.setFallManagerEnabled(False)
    print 'fall manager enabled:', alMotion.getFallManagerEnabled()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        nao.ExitProgram()
        pass

    # nao.commandModule.Run({"commandName": "say", "phrase": "im a cowboy"})
    # nao.commandModule.Run({
    #     "commandName": "naoqi",
    #     "serviceName": "ALTextToSpeech",
    #     "methodName": "say",
    #     "param1": "im going to jump over the moon"
    # })
    # vol = nao.commandModule.Run({
    #     "commandName": "property",
    #     "propertyName": "volume",
    #     "propertyValue": 40
    # })
    # print "volume:", vol
