

class Mind:
    def __init__(self, rootMind):
        self.rootMind = rootMind

    def WakeUp(self):
        print self, 'has awoken'

    def Sleep(self):
        print self, 'has gone to sleep'

    def __str__(self):
        return self.__class__.__name__
