import sys
from pkg.modules.nao.nao import Nao
from pkg.modules.message_client.client import MessageClient
from pkg.modules.behavior_planner.behavior_planner import BehaviorPlanner
import time


class AutoImprovise():
    def __init__(self, ipAddress):
        self.messageClient = MessageClient("10.50.16.50:3000")
        self.nao = Nao(ipAddress)
        self.behaviorPlanner = BehaviorPlanner(self.nao)

# NAOIP = "10.50.16.53"
# NAOIP = "NA01.local"


if __name__ == "__main__":
    NAOIP = sys.argv[1]
    autoImprovise = AutoImprovise(NAOIP)
    autoImprovise.behaviorPlanner.Begin()
    try:
        while autoImprovise.behaviorPlanner.rootMind.travelMind.room != None:
            time.sleep(0.01)
    except KeyboardInterrupt:
        print 'exiting..'
    autoImprovise.behaviorPlanner.End()
    autoImprovise.nao.ExitProgram()
    print 'program terminated'
