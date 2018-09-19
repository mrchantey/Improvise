

class Action:
    def __init__(self):
        self.subActions = []

    def Run(self):
        for subAction in self.subActions:
            subAction.Run(self)
