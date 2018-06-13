

class EventModule():

    # Connected memory service is required
    def __init__(self, memoryService):
        events = [
            "AutonomousLife/State",
            # "ALTextToSpeech/TextDone",
            # "ALTextToSpeech/TextInterrupted",
            # "ALTextToSpeech/TextStarted",
            "ALTextToSpeech/CurrentSentence"
            # "ALVoiceEmotionAnalysis/EmotionRecognized",
            # "ALBasicAwareness/HumanLost",
            # "ALBasicAwareness/HumanTracked",
            # "ALBasicAwareness/StimulusDetected"
        ]
        self.eventPool = []
        self.eventSubscribers = []
        for eventKey in events:
            self.SubscribeToEvent(eventKey, memoryService)

    # --------------------------------BE VERY CAREFUL WITH BELOW CODE, WE'RE DEFAULTING TO LAST ELEMENT OF ARRAY IN OTHER CASES----------------

    def SubscribeToEvent(self, eventKey, memoryService):
        sub = memoryService.subscriber(eventKey)

        def OnEvent(eventValue):
            print 'event occured..', eventKey, eventValue
            self.eventPool.append({'key': eventKey, 'value': eventValue})
        sub.signal.connect(OnEvent)
        # subscribers must be kept alive
        self.eventSubscribers.append(sub)
        print 'EVENT SUBSCRIBED', eventKey

    def DrainEvents(self):
        poolContents = self.eventPool
        self.eventPool = []
        return poolContents
