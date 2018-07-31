

class LocationAction:
    def __init__(self, location):
        self.location = location
        self.subActions = []

    def Run(self, aiMind):
        for subAction in self.subActions:
            subAction.Run(self, aiMind)


class EnterAction(LocationAction):
    def Run(self, aiMind):
        LocationAction.Run(self, aiMind)
        print aiMind, "has entered", self.location


class ExitAction(LocationAction):
    def Run(self, aiMind):
        LocationAction.Run(self, aiMind)
        print aiMind, "has exited", self.location
