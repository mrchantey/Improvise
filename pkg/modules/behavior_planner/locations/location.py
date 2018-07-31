
class Location:
    def __init__(self, enterAction, exitAction):
        self.actions = []
        self.eventListeners = []
        self.enterAction = enterAction
        self.exitAction = exitAction

    def __str__(self):
        return self.__class__.__name__
