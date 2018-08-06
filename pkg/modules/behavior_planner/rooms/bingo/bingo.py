from pkg.modules.behavior_planner.rooms.room import Room
from pkg.modules.behavior_planner.actions.room_action import EnterAction
from pkg.modules.behavior_planner.actions.room_action import RoomAction
from pkg.modules.behavior_planner.actions.room_action import ExitAction

from pkg.modules.behavior_planner.rooms.bingo.bingo_numbers import BingoNumbers

import time


class Bingo(Room, BingoNumbers):
    def __init__(self, parentRoom):
        playBingoAction = PlayBingo(self)
        enterAction = EnterBingo(self, playBingoAction)
        exitAction = ExitBingo(self, playBingoAction)
        Room.__init__(self, parentRoom, enterAction, exitAction)
        BingoNumbers.__init__(self, 1, 50)


class EnterBingo(EnterAction):
    def __init__(self, room, playBingoAction):
        EnterAction.__init__(self, room)
        self.playBingoAction = playBingoAction

    def Run(self, rootMind):
        EnterAction.Run(self, rootMind)
        # rootMind.Do('StopAll', {'async': False})
        rootMind.Do('Say', {'phrase': 'lets play bingo!', 'async': False, 'animated': True})
        self.playBingoAction.Run(rootMind)


class PlayBingo(RoomAction):
    def __init__(self, room):
        RoomAction.__init__(self, room)
        self.loop = True

    def Run(self, rootMind):
        RoomAction.Run(self, rootMind)
        while self.loop and not BingoNumbers.IsDone(self.room):
            call = BingoNumbers.GetNextBingoCall(self.room)
            rootMind.Do('Say', {'phrase': call, 'async': False, 'animated': True})
            # time.sleep(4)


class ExitBingo(ExitAction):
    def __init__(self, room, playBingoAction):
        ExitAction.__init__(self, room)
        self.playBingoAction = playBingoAction

    def Run(self, rootMind):
        self.playBingoAction.loop = False
        ExitAction.Run(self, rootMind)
        # print 'EXITING BINGO'
        rootMind.Do('Say', {'phrase': 'Thanks for playing!', 'async': False, 'animated': True})
        # rootMind.Do('RunBasicAction', {'action': 'stand_up', 'async': False})
