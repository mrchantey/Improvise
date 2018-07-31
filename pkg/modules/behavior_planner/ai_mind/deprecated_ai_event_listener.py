

# class AIEventListener:
#     def __init__(self, naoEvents):
#         self.subcriptionIdIncrementer = 0
#         naoEvents.AddCallback(self.OnNaoEvent)
#         self.subscriptions = []
#         pass

#     def SubscribeToEvent(self, key, callback):
#         subscription = {'key': key, 'callback': callback, 'id': self.subcriptionIdIncrementer}
#         self.subscriptions.append(subscription)
#         self.subcriptionIdIncrementer += 1
#         return subscription[id]

#     def UnsubscribeFromEvent(self, id):
#         self.subscriptions = filter(lambda s: s['id'] != id, self.subscriptions)

#     # def OnNaoEvent(self, key, value):
#     #     print "ai mind heard event", key, value
#     #     self.theseSubscriptions =
