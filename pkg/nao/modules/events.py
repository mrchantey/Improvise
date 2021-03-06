

class EventModule():

    # Connected memory service is required
    def __init__(self, memoryService):
        events = [
            "FrontTactilTouched",
            "MiddleTactilTouched",
            "RearTactilTouched",
            "HandLeftBackTouched",
            "HandLeftLeftTouched",
            "HandLeftRightTouched",
            "LeftBumperPressed",
            "RightBumperPressed",
            "AutonomousLife/State",
            "ALTextToSpeech/TextDone",
            # "ALTextToSpeech/TextInterrupted",
            # "ALTextToSpeech/TextStarted",
            "ALTextToSpeech/CurrentSentence",
            "SpeechDetected",
            "WordRecognized",
            # "ALSpeechRecognition/Status"
            # "NAOqiReady"
            # "ALVoiceEmotionAnalysis/EmotionRecognized",
            # "ALBasicAwareness/HumanLost",
            # "ALBasicAwareness/HumanTracked",
            # "ALBasicAwareness/StimulusDetected"
        ]
        self.eventPool = []
        # subscribers must remain alive
        self.eventSubscribers = []
        # event listeners are often internal, ie listen for text done
        self.listeners = []
        # callbacks of format (key,value)
        # self.callbacks = []
        for eventKey in events:
            self.SubscribeToEvent(eventKey, memoryService)

        print 'EVENTS SUBSCRIBED'

    # --------------------------------BE VERY CAREFUL WITH BELOW CODE, WE'RE DEFAULTING TO LAST ELEMENT OF ARRAY IN OTHER CASES----------------

    def SubscribeToEvent(self, eventKey, memoryService):
        sub = memoryService.subscriber(eventKey)

        def OnEvent(eventValue):
            print 'event occured..', eventKey, eventValue
            self.eventPool.append({'key': eventKey, 'value': eventValue})
            eventListeners = filter(lambda l: l['key'] == eventKey, self.listeners)
            # for listener in eventListeners:
            #     print 'LISTENER CALLBACK:', listener['callback']
            for listener in eventListeners:
                listener['callback'](eventValue)

        sub.signal.connect(OnEvent)
        # subscribers must be kept alive
        self.eventSubscribers.append(sub)
        # print 'EVENT SUBSCRIBED', eventKey

    def AddListener(self, key, callback):
        matchingListeners = filter(lambda l: l['key'] == key and l['callback'] == callback, self.listeners)
        if len(matchingListeners) > 0:
            return matchingListeners[0]
        else:
            listener = {'key': key, 'callback': callback}
            self.listeners.append(listener)
            return listener

    def RemoveListener(self, listener):
        if listener in self.listeners:
            self.listeners.remove(listener)

    def AddListeners(self, keys, callback):
        listeners = []
        for key in keys:
            listener = self.AddListener(key, callback)
            listeners.append(listener)
        return listeners

    def RemoveListeners(self, listeners):
        for listener in listeners:
            self.RemoveListener(listener)

    def HandleRequest(self, params):
        drain = params['drain'] if 'drain' in params else False
        events = self.DrainEvents() if drain == True else self.eventPool
        return {'events': events}

    def DrainEvents(self):
        poolContents = self.eventPool
        self.eventPool = []
        return poolContents
