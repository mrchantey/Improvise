

class Event():
    def __init__(self, action, predicate, keys, naoEventModule, oneShot=False):
        self.action = action
        self.predicate = predicate
        self.keys = keys
        self.naoEventModule = naoEventModule
        self.listeners = []
        self.oneShot = oneShot

    def OnTrigger(self, val):
        if self.predicate(val):
            if self.oneShot:
                self.StopListening()
            self.action.Run()

    def StartListening(self):
        self.listeners = self.naoEventModule.AddListeners(self.keys, self.OnTrigger)

    def StopListening(self):
        self.naoEventModule.RemoveListeners(self.listeners)
        self.listeners = []
