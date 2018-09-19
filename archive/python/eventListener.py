from naoqi import *
import sys


def CreateEventListener(eventCallback):

    eventListener = EventListenerModule("eventListener")
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
    eventListener.ListenForEvents(events, eventCallback)
    return eventListener


class EventListenerModule(ALModule):

    def ListenForEvents(self, events, eventCallback):
        self.memory = ALProxy("ALMemory")
        self.eventCallback = eventCallback
        for event in events:
            self.memory.subscribeToEvent(event, "eventListener", "onMemoryEvent")

    def onMemoryEvent(self, propName, propValue):
        # print "\n", "Property", propName, "was changed to", propValue
        self.eventCallback(propName, propValue)


if __name__ == "__main__":
    ipAddress = sys.argv[1]
    broker = ALBroker("myBroker", '0.0.0.0', 0, ipAddress, 9559)
    # tts = ALProxy("ALTextToSpeech")

    def printEvent(eventName, eventValue):
        print "EVENT", eventName, eventValue
    eventListener = CreateEventListener(printEvent)
    try:
        while True:
            pass
    except KeyboardInterrupt:
        pass
