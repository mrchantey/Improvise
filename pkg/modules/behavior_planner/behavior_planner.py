from pkg.modules.behavior_planner.ai_mind.ai_mind import AIMind
from pkg.modules.behavior_planner.locations.improvise_root import ImproviseRoot


class BehaviorPlanner:
    def __init__(self, nao=None):
        self.rootLocation = ImproviseRoot()
        self.aiMind = AIMind(nao, self.rootLocation)
        self.aiMind.Awake()
        # self.aiMind.Sleep()


if __name__ == "__main__":
    behaviorPlanner = BehaviorPlanner()
