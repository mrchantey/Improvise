

class AIMind:
    def __init__(self, nao, rootLocation):
        self.name = "Nao AI Mind"
        self.nao = nao
        self.location = rootLocation

    def Do(self, methodName, params):
        self.nao.methods.DoMethod(methodName, params)

    def EnterLocation(self, location):
        self.location = location
        self.location.enterAction.Run(self)

    def Awake(self):
        self.location.enterAction.Run(self)

    def Sleep(self):
        self.location.exitAction.Run(self)

    def __str__(self):
        return self.__class__.__name__
