import sys
from pkg.modules.nao.nao import Nao
# from pkg.modules.message_client.client import MessageClient
from pkg.modules.behavior_planner.behavior_planner import BehaviorPlanner
from pkg.modules.server import Server
from pkg.backEndClient import BackEndClient
import time
# pow


class AutoImprovise():
    def __init__(self, ipAddress, deployed):
        self.backEndClient = BackEndClient("localhost:3000")
        self.nao = Nao(ipAddress, self.backEndClient)
        serverIP = '127.0.0.1' if not deployed else self.nao.properties.properties['ipAddress']['get']()
        self.server = Server(5000, serverIP)
        self.server.RequestCallback = self.OnModuleRequest
        self.behaviorPlanner = BehaviorPlanner(self.nao)

    def OnModuleRequest(self, moduleName, reqBody):
        attr = getattr(self, moduleName)
        resBody = attr.OnRequest(reqBody)
        return resBody


if __name__ == "__main__":
    NAOIP = sys.argv[1]
    deployed = True if '-d' in sys.argv else False
    print 'starting up...'
    print 'deployed:', deployed
    autoImprovise = AutoImprovise(NAOIP, deployed)
    autoImprovise.behaviorPlanner.Begin()
    autoImprovise.server.Run()
    try:
        while autoImprovise.behaviorPlanner.rootMind.travelMind.room != None:
            time.sleep(0.01)
    except KeyboardInterrupt:
        print 'exiting..'
    autoImprovise.behaviorPlanner.End()
    autoImprovise.nao.ExitProgram()
    autoImprovise.server.Stop()
    print 'program terminated'
