from pkg.modules.behavior_planner.minds.travel_mind import TravelMind
from pkg.modules.behavior_planner.minds.mind import Mind
# from pkg.modules.behavior_planner.mind.event_mind import EventMind


class RootMind(Mind):
    def __init__(self, nao):
        self.name = "Nao AI Mind"
        self.nao = nao
        self.travelMind = TravelMind(self)
        # self.eventMind = EventMind(self)

    def WakeUp(self):
        Mind.WakeUp(self)
        self.travelMind.WakeUp()

    def Sleep(self):
        Mind.Sleep(self)
        self.travelMind.Sleep()

    # just a shortcut
    def Do(self, methodName, params):
        params['methodName'] = methodName
        self.nao.methods.DoMethod(params)

    def __str__(self):
        return self.__class__.__name__
