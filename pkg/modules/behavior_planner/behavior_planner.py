from pkg.modules.behavior_planner.mind.ai_mind import AIMind
from pkg.modules.behavior_planner.rooms.improvise_root import ImproviseRoot
from pkg.modules.behavior_planner.rooms.bingo.bingo import Bingo


class BehaviorPlanner:
    def __init__(self, nao=None):
        self.rootRoom = Bingo(None)
        # self.rootRoom = ImproviseRoot()
        self.aiMind = AIMind(nao)

    def Begin(self):
        self.aiMind.ChangeRooms(self.rootRoom)

    def End(self):
        self.aiMind.exitRecursive.Run()


if __name__ == "__main__":
    behaviorPlanner = BehaviorPlanner()
