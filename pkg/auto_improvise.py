import sys
from pkg.nao.nao import Nao
# from pkg.modules.message_client.client import MessageClient
# from pkg.modules.behavior_planner.behavior_planner import BehaviorPlanner
from pkg.server import Server
import time
# pow


class AutoImprovise():
    def __init__(self, ipAddress, port, deployed):
        self.nao = Nao(ipAddress)
        serverIP = self.GetServerIPAddress(deployed)
        self.server = Server(port, serverIP, self.nao.commandModule.Run)
        # self.behaviorPlanner = BehaviorPlanner(self.nao)

    def GetServerIPAddress(self, deployed):
        if deployed:
            response = self.nao.commandModule.Run({
                "commandName": "property",
                "propertyName": "ipAddress"
            })
            return response['propertyValue']
        else:
            return '127.0.0.1'


if __name__ == "__main__":
    NAOIP = sys.argv[1]
    PORT = 5000
    deployed = True if '-d' in sys.argv else False
    print 'starting up...'
    print 'deployed:', deployed
    autoImprovise = AutoImprovise(NAOIP, PORT, deployed)
    # autoImprovise.behaviorPlanner.Begin()
    autoImprovise.server.Run()
    try:
        while True:
            pass
        # while autoImprovise.behaviorPlanner.rootMind.travelMind.room != None:
            # time.sleep(0.01)
    except KeyboardInterrupt:
        print 'exiting..'
    # autoImprovise.behaviorPlanner.End()
    autoImprovise.nao.ExitProgram()
    autoImprovise.server.Stop()
    print 'program terminated'
