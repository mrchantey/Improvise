# from pkg.modules.behavior_planner.mind.mind import Mind
# from pkg.modules.behavior_planner.events.event import Event


# class EventMind(Mind):
#     def __init__(self, rootMind):
#         Mind.__init__(self, rootMind)
#         self.events = []

#     def WakeUp(self):
#         Mind.WakeUp(self)

#     def Sleep(self):
#         Mind.Sleep(self)

#     def CreateRoomEvent(self, roomAction, predicate, keys, oneShot=True):
#         def actionWrapper(val):
#             roomAction.Run(self.rootMind)
#         event = Event(actionWrapper, predicate, keys, self.rootMind.nao.events, oneShot)
#         self.events.append(event)
#         return event
