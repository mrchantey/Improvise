from pkg.modules.behavior_planner.locations.location import Location
from pkg.modules.behavior_planner.actions.location_action import EnterAction
from pkg.modules.behavior_planner.actions.location_action import ExitAction

from pkg.modules.behavior_planner.locations.bingo import Bingo


class ActivitySelector(Location):
    def __init__(self):
        enterAction = ActivitySelectorEnter(self)
        exitAction = ExitAction(self)
        Location.__init__(self, enterAction, exitAction)
        self.bingo = Bingo()


class ActivitySelectorEnter(EnterAction):
    def Run(self, aiMind):
        EnterAction.Run(self, aiMind)
        aiMind.Do('StopAll', {'async': False})
        aiMind.Do('SetLeds', {'name': 'FaceLeds', 'colorName': 'yellow'})
        aiMind.Do('RunBasicAction', {'action': 'stand_up', 'async': False})
        aiMind.Do('SetLeds', {'name': 'FaceLeds', 'colorName': 'green'})
        aiMind.Do('Say', {'phrase': 'what would you like to do today?', 'async': False})
        aiMind.EnterLocation(self.location.bingo)
