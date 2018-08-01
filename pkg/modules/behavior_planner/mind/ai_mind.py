from pkg.modules.behavior_planner.mind.room_mind import RoomMind


class AIMind(RoomMind):
    def __init__(self, nao):
        self.name = "Nao AI Mind"
        self.nao = nao
        RoomMind.__init__(self)

    def Do(self, methodName, params):
        self.nao.methods.DoMethod(methodName, params)

    def __str__(self):
        return self.__class__.__name__
