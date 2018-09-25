

class EventCommand():
    def __init__(self, eventModule):
        self.eventModule = eventModule

    def Run(self, command):
        if 'drain' in command:
            if command['drain'] == True:
                return self.eventModule.DrainEvents()
            else:
                return self.eventModule.eventPool
        else:
            return self.eventModule.DrainEvents()
