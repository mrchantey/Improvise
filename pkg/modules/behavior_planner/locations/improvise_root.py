from pkg.modules.behavior_planner.locations.location import Location
from pkg.modules.behavior_planner.actions.location_action import LocationAction
from pkg.modules.behavior_planner.actions.location_action import EnterAction
from pkg.modules.behavior_planner.actions.location_action import ExitAction
from pkg.modules.behavior_planner.locations.activity_selector import ActivitySelector


class ImproviseRoot(Location):
    def __init__(self):
        enterAction = ImproviseRootEnterAction(self)
        exitAction = ImproviseRootExitAction(self)
        Location.__init__(self, enterAction, exitAction)
        self.activitySelector = ActivitySelector()
        self.goToActivitySelector = GoToActivitySelector(self)


class GoToActivitySelector(LocationAction):
    def RunIfPredicate(self, aiMind, tactileValue):
        if tactileValue == 1:
            self.Run(aiMind)

    def Run(self, aiMind):
        print 'going to activity selector'
        for el in self.location.eventListeners:
            aiMind.nao.events.RemoveListener(el)
        self.location.eventListeners = []
        aiMind.EnterLocation(self.location.activitySelector)


class ImproviseRootEnterAction(EnterAction):
    def Run(self, aiMind):
        EnterAction.Run(self, aiMind)
        aiMind.Do('SetLeds', {"name": "FaceLeds", "colorName": "yellow", "duration": 0.1})
        aiMind.Do('StopAll', {'async': False})
        aiMind.Do('SetLeds', {"name": "FaceLeds", "colorName": "green"})
        aiMind.Do('RunBasicAction', {"action": "twinkle_brain"})

        def GoToActivitySelectorWrapper(tactileVal):
            self.location.goToActivitySelector.RunIfPredicate(aiMind, tactileVal)

        listenerA = aiMind.nao.events.AddListener("FrontTactilTouched", GoToActivitySelectorWrapper)
        listenerB = aiMind.nao.events.AddListener("MiddleTactilTouched", GoToActivitySelectorWrapper)
        listenerC = aiMind.nao.events.AddListener("RearTactilTouched", GoToActivitySelectorWrapper)
        self.location.eventListeners.append(listenerA)
        self.location.eventListeners.append(listenerB)
        self.location.eventListeners.append(listenerC)
        aiMind.Do('RunBasicAction', {"action": "rest", "async": False})


class ImproviseRootExitAction(ExitAction):
    def Run(self, aiMind):
        ExitAction.Run(self, aiMind)
        aiMind.Do('SetLeds', {"name": "FaceLeds", "colorName": "white"})
        aiMind.Do('RunBasicAction', {"action": "rest", "async": False})
