from pkg.modules.behavior_planner.events.event import Event


class RoomEvent(Event):
    # rootmind can deliver nao event module
    def __init__(self, rootMind, action, predicate, keys, oneShot):
        Event.__init__(self, action, predicate, keys, rootMind.nao.events, oneShot)
        self.rootMind = rootMind

    def OnTrigger(self, val):
        print 'trigger bang'
        if self.predicate(val):
            if self.oneShot:
                self.StopListening()
            self.action.Run(self.rootMind)
