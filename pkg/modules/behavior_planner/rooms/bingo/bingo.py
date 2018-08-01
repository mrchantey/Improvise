from pkg.modules.behavior_planner.rooms.room import Room
from pkg.modules.behavior_planner.actions.room_action import EnterAction
from pkg.modules.behavior_planner.actions.room_action import ExitAction

from pkg.modules.behavior_planner.rooms.bingo.bingo_numbers import BingoNumbers

import time


class Bingo(Room, BingoNumbers):
    def __init__(self, parentRoom):
        enterAction = EnterBingo(self)
        exitAction = ExitBingo(self)
        Room.__init__(self, parentRoom, enterAction, exitAction)
        BingoNumbers.__init__(self, 1, 50)


class EnterBingo(EnterAction):
    def Run(self, aiMind):
        EnterAction.Run(self, aiMind)
        # aiMind.Do('StopAll', {'async': False})
        aiMind.Do('Say', {'phrase': 'lets play bingo!', 'async': False, 'animated': True})
        while self.room == aiMind.room and not BingoNumbers.IsDone(self.room):
            call = BingoNumbers.GetNextBingoCall(self.room)
            aiMind.Do('Say', {'phrase': call, 'async': False, 'animated': True})
            time.sleep(4)
        # if self.room == aiMind.room:
        #     self.room.exitAction.Run(aiMind)


class ExitBingo(ExitAction):
    def Run(self, aiMind):
        ExitAction.Run(self, aiMind)
        aiMind.Do('Say', {'phrase': 'Thanks for playing!', 'async': False, 'animated': True})
        aiMind.Do('RunBasicAction', {'action': 'stand_up', 'async': False})
