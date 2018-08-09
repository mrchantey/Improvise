import sys
from pkg.modules.nao.nao import Nao
# from pkg.modules.message_client.client import MessageClient
from pkg.modules.behavior_planner.behavior_planner import BehaviorPlanner
from pkg.modules.server import Server
import time


class AutoImprovise():
    def __init__(self, ipAddress, deployed):
        self.nao = Nao(ipAddress)
        serverIP = '127.0.0.1' if not deployed else self.nao.properties.properties['ipAddress']['get']()
        print 'spinning up server with ip address', serverIP
        self.server = Server(5000, serverIP)
        self.server.RequestCallback = self.OnModuleRequest
        self.behaviorPlanner = BehaviorPlanner(self.nao)

    def OnModuleRequest(self, moduleName, reqBody):
        attr = getattr(self, moduleName)
        resBody = attr.OnRequest(reqBody)
        return resBody

# NAOIP = "10.50.16.53"
# NAOIP = "NA01.local"


if __name__ == "__main__":
    NAOIP = sys.argv[1]
    deployed = True if '-d' in sys.argv else False
    print 'starting up...'
    print 'deployed:', deployed
    autoImprovise = AutoImprovise(NAOIP, deployed)
    autoImprovise.server.Run()
    autoImprovise.behaviorPlanner.Begin()
    try:
        while autoImprovise.behaviorPlanner.rootMind.travelMind.room != None:
            time.sleep(0.01)
    except KeyboardInterrupt:
        print 'exiting..'
    autoImprovise.behaviorPlanner.End()
    autoImprovise.nao.ExitProgram()
    autoImprovise.server.Stop()
    print 'program terminated'
