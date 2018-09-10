from pkg.modules.behavior_planner.rooms.room import Room
from pkg.modules.behavior_planner.actions.room_action import EnterAction, ExitAction, RoomAction
from pkg.modules.behavior_planner.events.room_event import RoomEvent
from pkg.modules.behavior_planner.rooms.bingo.bingo import Bingo


class ActivitySelector(Room):
    def __init__(self, parentRoom):
        enterAction = ActivitySelectorEnter(self)
        exitAction = ExitAction(self)
        Room.__init__(self, parentRoom, enterAction, exitAction)
        self.bingo = Bingo(parentRoom)


class SelectActivityEvent(RoomEvent):
    def __init__(self, rootMind, action, activityName):
        keys = ["WordRecognized"]

        def predicate(val): return True if val[0] == activityName else False
        RoomEvent.__init__(self, rootMind, action, predicate, keys, True)


class SelectActivityAction(RoomAction):
    def __init__(self, room, activityRoom):
        RoomAction.__init__(self, room)
        self.activityRoom = activityRoom

    def Run(self, rootMind):
        print "Bingo Selected"
        RoomAction.Run(self, rootMind)
        rootMind.travelMind.ChangeRooms(self.activityRoom)


class ActivitySelectorEnter(EnterAction):
    def Run(self, rootMind):
        EnterAction.Run(self, rootMind)
        rootMind.Do('StopAll', {'async': False})
        rootMind.Do('SetLeds', {'name': 'FaceLeds', 'colorName': 'yellow'})
        rootMind.Do('RunBasicAction', {'action': 'stand_up', 'async': False})
        rootMind.Do('RunBasicAction', {'action': 'breathe'})
        # rootMind.Do('RunBasicAction', {'action': 'recognize_speech'})
        rootMind.Do('SetLeds', {'name': 'FaceLeds', 'colorName': 'green'})
        rootMind.Do('Say', {'phrase': 'what would you like to do today?', 'async': False})
        #
        rootMind.nao.speechRecognition.AddWords(["bingo", "Party", "Go Scuba Diving"])
        rootMind.nao.speechRecognition.StartRecognizing()
        bingoAction = SelectActivityAction(self.room, self.room.bingo)
        bingoEvent = SelectActivityEvent(rootMind, bingoAction, "bingo")
        self.room.events.append(bingoEvent)
        bingoEvent.StartListening()
