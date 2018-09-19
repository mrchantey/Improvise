from pkg.modules.behavior_planner.actions.action import Action
from pkg.modules.behavior_planner.mind.mind import Mind
from pkg.modules.behavior_planner.events.event import Event


class TravelMind(Mind):
    def __init__(self, rootMind):
        Mind.__init__(self, rootMind)
        self.room = None
        self.exitRecursiveAction = ExitRecursiveAction(self)
        self.exitRecursiveEvent = ExitRecursiveEvent(self.exitRecursiveAction, nao.events)

    def WakeUp(self):
        Mind.WakeUp(self)
        self.exitRecursiveEvent.StartListening()

    def Sleep(self):
        Mind.Sleep(self)
        self.exitRecursiveEvent.StopListening()

    def ChangeRooms(self, newRoom):
        if self.room != None:
            self.room.exitAction.Run(self.rootMind)
        self.room = newRoom
        if self.room != None:
            self.room.enterAction.Run(self.rootMind)

    def EnterChildRoom(self, childRoom):
        self.room = childRoom
        self.room.enterAction.Run(self.rootMind)

    def ExitChildRoom(self):
        self.room.exitAction.Run(self.rootMind)
        self.room = self.room.parentRoom


class ExitRecursiveEvent(Event):
    def __init__(self, action, naoEventModule):

        eventKeys = ["HandLeftBackTouched",
                     "HandLeftLeftTouched",
                     "HandLeftRightTouched",
                     "LeftBumperPressed",
                     "RightBumperPressed"]

        def predicate(val): return True if val == 1 else False

        Event.__init__(self, action, predicate, eventKeys, naoEventModule, True)


class ExitRecursiveAction(Action):
    def __init__(self, travelMind):
        Action.__init__(self)
        self.travelMind = travelMind

    def Run(self):
        Action.Run(self)
        while self.travelMind.room != None:
            self.travelMind.ExitChildRoom()
