from pkg.modules.behavior_planner.rooms.room import Room
from pkg.modules.behavior_planner.actions.room_action import RoomAction
from pkg.modules.behavior_planner.actions.room_action import EnterAction
from pkg.modules.behavior_planner.actions.room_action import ExitAction
from pkg.modules.behavior_planner.rooms.activity_selector import ActivitySelector


class ImproviseRoot(Room):
    def __init__(self):
        enterAction = ImproviseRootEnterAction(self)
        exitAction = ImproviseRootExitAction(self)
        Room.__init__(self, None, enterAction, exitAction)
        self.activitySelector = ActivitySelector(self)
        self.goToActivitySelector = GoToActivitySelector(self)


class GoToActivitySelector(RoomAction):
    def RunIfPredicate(self, aiMind, tactileValue):
        if tactileValue == 1:
            self.Run(aiMind)

    def Run(self, aiMind):
        print 'going to activity selector'
        aiMind.Do('SetLeds', {"name": "BrainLeds", "colorName": "blue"})
        for el in self.room.eventListeners:
            aiMind.nao.events.RemoveListener(el)
        self.room.eventListeners = []
        aiMind.EnterChildRoom(self.room.activitySelector)


class ImproviseRootEnterAction(EnterAction):
    def Run(self, aiMind):
        # self.room.goToActivitySelector.RunIfPredicate(aiMind, 1)
        # Skip for testing
        EnterAction.Run(self, aiMind)
        aiMind.Do('SetLeds', {"name": "FaceLeds", "colorName": "yellow", "duration": 0.1, 'async': False})
        aiMind.Do('StopAll', {'async': False})
        aiMind.Do('SetLeds', {"name": "FaceLeds", "colorName": "green"})
        aiMind.Do('SetLeds', {"name": "FeetLeds", "colorName": "green"})
        aiMind.Do('RunBasicAction', {"action": "twinkle_brain"})

        def GoToActivitySelectorWrapper(tactileVal):
            self.room.goToActivitySelector.RunIfPredicate(aiMind, tactileVal)

        eventKeys = [
            "FrontTactilTouched",
            "MiddleTactilTouched",
            "RearTactilTouched"]

        listeners = aiMind.nao.events.AddListeners(eventKeys, GoToActivitySelectorWrapper)
        self.room.eventListeners += listeners

        aiMind.Do('RunBasicAction', {"action": "rest", "async": False})


class ImproviseRootExitAction(ExitAction):
    def Run(self, aiMind):
        ExitAction.Run(self, aiMind)
        aiMind.Do('SetLeds', {"name": "FaceLeds", "colorName": "white"})
        aiMind.Do('SetLeds', {"name": "BrainLeds", "colorName": "blue"})
        aiMind.Do('SetLeds', {"name": "FeetLeds", "colorName": "white"})
        aiMind.Do('RunBasicAction', {"action": "rest", "async": False})
        aiMind.Do('StopAll', {"async": False})
