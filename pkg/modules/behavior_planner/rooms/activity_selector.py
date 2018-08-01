from pkg.modules.behavior_planner.rooms.room import Room
from pkg.modules.behavior_planner.actions.room_action import EnterAction, ExitAction

from pkg.modules.behavior_planner.rooms.bingo.bingo import Bingo


class ActivitySelector(Room):
    def __init__(self, parentRoom):
        enterAction = ActivitySelectorEnter(self)
        exitAction = ExitAction(self)
        Room.__init__(self, parentRoom, enterAction, exitAction)
        self.bingo = Bingo(parentRoom)


class ActivitySelectorEnter(EnterAction):
    def Run(self, aiMind):
        EnterAction.Run(self, aiMind)
        aiMind.Do('StopAll', {'async': False})
        aiMind.Do('SetLeds', {'name': 'FaceLeds', 'colorName': 'yellow'})
        aiMind.Do('RunBasicAction', {'action': 'stand_up', 'async': False})
        aiMind.Do('RunBasicAction', {'action': 'breathe'})
        # aiMind.Do('RunBasicAction', {'action': 'recognize_speech'})
        aiMind.Do('SetLeds', {'name': 'FaceLeds', 'colorName': 'green'})
        aiMind.Do('Say', {'phrase': 'what would you like to do today?', 'async': False})
        aiMind.ChangeRooms(self.room.bingo)
