from pkg.modules.behavior_planner.locations.location import Location
from pkg.modules.behavior_planner.actions.location_action import EnterAction
from pkg.modules.behavior_planner.actions.location_action import ExitAction


class Bingo(Location):
    def __init__(self):
        enterAction = EnterBingo(self)
        exitAction = ExitAction(self)
        Location.__init__(self, enterAction, exitAction)


class EnterBingo(EnterAction):
    def Run(self, aiMind):
        EnterAction.Run(self, aiMind)
        aiMind.Do('StopAll', {'async': False})
        aiMind.Do('Say', {'phrase': 'lets play bingo!'})
