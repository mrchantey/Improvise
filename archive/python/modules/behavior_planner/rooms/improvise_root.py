from pkg.modules.behavior_planner.rooms.room import Room
from pkg.modules.behavior_planner.rooms.activity_selector import ActivitySelector
from pkg.modules.behavior_planner.actions.room_action import ExitAction, EnterAction, RoomAction
from pkg.modules.behavior_planner.events.room_event import RoomEvent


class ImproviseRoot(Room):
    def __init__(self, nao):
        goToActivitySelectorAction = GoToActivitySelectorAction(self)
        enterAction = EnterImprovise(self, goToActivitySelectorAction)
        exitAction = ExitImprovise(self, goToActivitySelectorAction)
        Room.__init__(self, None, enterAction, exitAction)
        self.activitySelector = ActivitySelector(self)


class GoToActivitySelectorEvent(RoomEvent):
    def __init__(self, rootMind, action):

        def predicate(val): return True if val == 1 else False
        keys = [
            "FrontTactilTouched",
            "MiddleTactilTouched",
            "RearTactilTouched"]

        RoomEvent.__init__(self, rootMind, action, predicate, keys, True)


class GoToActivitySelectorAction(RoomAction):

    def Run(self, rootMind):
        print 'going to activity selector'
        rootMind.Do('SetLeds', {"name": "BrainLeds", "colorName": "blue"})
        rootMind.travelMind.EnterChildRoom(self.room.activitySelector)


class EnterImprovise(EnterAction):
    def __init__(self, room, goToActivitySelectorAction):
        EnterAction.__init__(self, room)
        self.goToActivitySelectorAction = goToActivitySelectorAction

    def Run(self, rootMind):
        EnterAction.Run(self, rootMind)
        rootMind.Do('SetLeds', {"name": "FaceLeds", "colorName": "yellow", "duration": 0.1, 'async': False})
        rootMind.Do('StopAll', {'async': False})
        rootMind.Do('SetLeds', {"name": "FaceLeds", "colorName": "green"})
        rootMind.Do('SetLeds', {"name": "FeetLeds", "colorName": "green"})
        rootMind.Do('RunBasicAction', {"action": "twinkle_brain"})
        goToActivitySelectorAction = GoToActivitySelectorAction(self.room)
        goToActivitySelectorEvent = GoToActivitySelectorEvent(rootMind, goToActivitySelectorAction)
        self.room.events.append(goToActivitySelectorEvent)
        goToActivitySelectorEvent.StartListening()
        # rootMind.eventMind.CreateRoomEvent()
        rootMind.Do('RunBasicAction', {"action": "rest", "async": False})


class ExitImprovise(ExitAction):
    def __init__(self, room, goToActivitySelectorAction):
        ExitAction.__init__(self, room)
        self.goToActivitySelectorAction = goToActivitySelectorAction

    def Run(self, rootMind):
        rootMindRoomEvents = filter(lambda e: e.rootMind == rootMind, self.room.events)
        # print len(rootMindRoomEvents), 'removed'
        for e in rootMindRoomEvents:
            e.StopListening()
        self.room.events = filter(lambda e: e.rootMind != rootMind, self.room.events)

        ExitAction.Run(self, rootMind)
        rootMind.Do('SetLeds', {"name": "FaceLeds", "colorName": "white"})
        rootMind.Do('SetLeds', {"name": "BrainLeds", "colorName": "blue"})
        rootMind.Do('SetLeds', {"name": "FeetLeds", "colorName": "white"})
        rootMind.Do('RunBasicAction', {"action": "rest", "async": False})
        rootMind.Do('StopAll', {"async": False})
