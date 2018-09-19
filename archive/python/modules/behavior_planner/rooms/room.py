
class Room:
    def __init__(self, parentRoom, enterAction, exitAction):
        self.parentRoom = parentRoom
        self.actions = []
        self.events = []
        self.enterAction = enterAction
        self.exitAction = exitAction

    def __str__(self):
        return self.__class__.__name__
