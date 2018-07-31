import sys
import threading
from pkg.modules.nao.nao import Nao
from pkg.modules.behavior_planner.behavior_planner import BehaviorPlanner


class AutoImprovise():
    def __init__(self, ipAddress):
        self.nao = Nao(ipAddress)
        self.behaviorPlanner = BehaviorPlanner(self.nao)

# NAOIP = "10.50.16.53"
# NAOIP = "NA01.local"


if __name__ == "__main__":
    NAOIP = sys.argv[1]
    autoImprovise = AutoImprovise(NAOIP)
    xyz = raw_input("waiting for enter key press")
    print 'exiting..'
