from pkg.modules.behavior_planner.minds.root_mind import RootMind
from pkg.modules.behavior_planner.rooms.improvise_root import ImproviseRoot
from pkg.modules.behavior_planner.rooms.bingo.bingo import Bingo


class BehaviorPlanner:
    def __init__(self, nao):
        # self.rootRoom = Bingo(None)
        self.rootRoom = ImproviseRoot(nao)
        self.rootMind = RootMind(nao)
        self.rootMind.WakeUp()

    def Begin(self):
        self.rootMind.travelMind.ChangeRooms(self.rootRoom)

    def End(self):
        self.rootMind.travelMind.exitRecursiveAction.Run()
