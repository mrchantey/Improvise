import sys
from pkg.nao.nao import Nao
# from pkg.modules.message_client.client import MessageClient
# from pkg.modules.behavior_planner.behavior_planner import BehaviorPlanner
from pkg.server import Server
import time
# pow


class AutoImprovise():
    def __init__(self, ipAddress, port, deployed, defaultPose):
        self.nao = Nao(ipAddress, self.ExitProgram, defaultPose)
        serverIP = self.GetServerIPAddress(deployed)
        self.server = Server(port, serverIP, self.nao.commandModule.Run)
        self.server.Run()
        self.exitFlag = False
        # self.behaviorPlanner = BehaviorPlanner(self.nao)

    def GetServerIPAddress(self, deployed):
        if deployed:
            returnData = self.nao.commandModule.Run({
                "commandName": "property",
                "propertyName": "ipAddress",
                "sayValue": False
            })
            return returnData['response']['propertyValue']
        else:
            return '127.0.0.1'

    def StartProgram(self):
        self.nao.StartProgram()

    def ExitProgram(self):
        print 'exiting..'
        self.nao.ExitProgram()
        self.server.Stop()
        self.exitFlag = True


if __name__ == "__main__":
    NAOIP = sys.argv[1]
    PORT = 5000
    deployed = True if '-d' in sys.argv else False
    defaultPose = 'rest' if '-rest' in sys.argv else 'stand'
    print 'starting up...'

    autoImprovise = AutoImprovise(NAOIP, PORT, deployed, defaultPose)
    autoImprovise.StartProgram()

    try:
        while autoImprovise.exitFlag == False:
            pass
    except KeyboardInterrupt:
        autoImprovise.ExitProgram()
    print 'program terminated'
    sys.exit()
