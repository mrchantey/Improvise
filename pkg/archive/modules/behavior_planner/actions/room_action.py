from pkg.modules.behavior_planner.actions.action import Action


class RoomAction(Action):
    def __init__(self, room):
        Action.__init__(self)
        self.room = room

    def Run(self, rootMind):
        Action.Run(self)


class EnterAction(RoomAction):
    def Run(self, aiMind):
        RoomAction.Run(self, aiMind)
        print aiMind, "has entered", self.room


class ExitAction(RoomAction):
    def Run(self, aiMind):
        RoomAction.Run(self, aiMind)
        print aiMind, "has exited", self.room
