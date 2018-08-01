from pkg.modules.behavior_planner.actions.mind_action import MindAction
from pkg.modules.behavior_planner.mind.mind import Mind


class RoomMind(Mind):
    def __init__(self):
        Mind.__init__(self)
        self.room = None
        self.exitRecursive = ExitRecursiveAction(self)

    def ChangeRooms(self, newRoom):
        if self.room != None:
            self.room.exitAction.Run(self)
        self.room = newRoom
        if self.room != None:
            self.room.enterAction.Run(self)

    def EnterChildRoom(self, childRoom):
        self.room = childRoom
        self.room.enterAction.Run(self)

    def ExitChildRoom(self):
        self.room.exitAction.Run(self)
        self.room = self.room.parentRoom


class ExitRecursiveAction(MindAction):
    def __init__(self, aiMind):
        MindAction.__init__(self, aiMind)
        eventKeys = ["HandLeftBackTouched",
                     "HandLeftLeftTouched",
                     "HandLeftRightTouched",
                     "LeftBumperPressed",
                     "RightBumperPressed"]

        listeners = self.aiMind.nao.events.AddListeners(eventKeys, self.RunIfPredicate)
        self.aiMind.eventListeners.append(listeners)

    def RunIfPredicate(self, value):
        if value == 1:
            self.Run()

    def Run(self):
        MindAction.Run(self)
        while self.aiMind.room != None:
            self.aiMind.ExitChildRoom()
