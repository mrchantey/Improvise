import sys
from pkg.modules.nao.nao import Nao
from pkg.modules.behavior_planner.behavior_planner import BehaviorPlanner
import time


class AutoImprovise():
    def __init__(self, ipAddress):
        self.nao = Nao(ipAddress)
        self.behaviorPlanner = BehaviorPlanner(self.nao)

# NAOIP = "10.50.16.53"
# NAOIP = "NA01.local"


if __name__ == "__main__":
    NAOIP = sys.argv[1]
    autoImprovise = AutoImprovise(NAOIP)
    autoImprovise.behaviorPlanner.Begin()
    try:
        while autoImprovise.behaviorPlanner.aiMind.room != None:
            time.sleep(0.1)
    except KeyboardInterrupt:
        print 'exiting..'
    autoImprovise.behaviorPlanner.End()
    print 'program terminated'
