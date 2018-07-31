

class EventModule():

    # Connected memory service is required
    def __init__(self, memoryService):
        events = [
            "FrontTactilTouched",
            "MiddleTactilTouched",
            "RearTactilTouched",
            "AutonomousLife/State",
            "ALTextToSpeech/TextDone",
            # "ALTextToSpeech/TextInterrupted",
            # "ALTextToSpeech/TextStarted",
            "ALTextToSpeech/CurrentSentence",
            # "ALVoiceEmotionAnalysis/EmotionRecognized",
            # "ALBasicAwareness/HumanLost",
            "WordRecognized"
            # "ALBasicAwareness/HumanTracked",
            # "ALBasicAwareness/StimulusDetected"
        ]
        self.listenerIdIncr = 0
        self.eventPool = []
        # subscribers must remain alive
        self.eventSubscribers = []
        # event listeners are often internal, ie listen for text done
        self.listeners = []
        # callbacks of format (key,value)
        # self.callbacks = []
        for eventKey in events:
            self.SubscribeToEvent(eventKey, memoryService)

    # --------------------------------BE VERY CAREFUL WITH BELOW CODE, WE'RE DEFAULTING TO LAST ELEMENT OF ARRAY IN OTHER CASES----------------

    def SubscribeToEvent(self, eventKey, memoryService):
        sub = memoryService.subscriber(eventKey)

        def OnEvent(eventValue):
            print 'event occured..', eventKey, eventValue
            self.eventPool.append({'key': eventKey, 'value': eventValue})
            # for callback in self.callbacks:
            #     callback(eventKey, eventValue)
            thislisteners = filter(lambda l: l['key'] == eventKey, self.listeners)
            for listener in thislisteners:
                listener['callback'](eventValue)

        sub.signal.connect(OnEvent)
        # subscribers must be kept alive
        self.eventSubscribers.append(sub)
        print 'EVENT SUBSCRIBED', eventKey

    def AddListener(self, key, callback):
        listener = {'key': key, 'callback': callback, 'id': self.listenerIdIncr}
        self.listeners.append(listener)
        self.listenerIdIncr += 1
        return listener

    def RemoveListener(self, listener):
        self.listeners.remove(listener)
        # self.listeners = filter(lambda s: s['id'] != id, self.listeners)

    # def AddCallback(self, callback):
    #     self.callbacks.append(callback)

    def HandleRequest(self, params):
        drain = params['drain'] if 'drain' in params else False
        events = self.DrainEvents() if drain == True else self.eventPool
        return {'events': events}

    def DrainEvents(self):
        poolContents = self.eventPool
        self.eventPool = []
        return poolContents
