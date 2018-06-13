

class MethodModule():

    def __init__(self, services):
        self.services = services

    def DoMethod(self, methName, params):
        meth = getattr(self, methName)
        meth(params)

    def SetAutoState(self, params):
        self.services.autonomousLife.setState(params[0], _async=True)

    def say(self, params):
        self.Say(params)

    def Say(self, params):
        if len(params) > 1:
            if params[1] == True:
                self.services.animatedSpeech.say(params[0], _async=True)
            else:
                self.services.textToSpeech.say(params[0], _async=True)
        else:
            self.services.textToSpeech.say(params[0], _async=True)

    def RunBehavior(self, params):
        self.services.behaviorManager.runBehavior(params[0], _async=True)

    def PlayAudio(self, params):
        self.services.audioPlayer.playFile(params[0], _async=True)
        # id = self.services.audioPlayer.loadFile(params[0])

    def StopAll(self, params):
        self.services.behaviorManager.stopAllBehaviors(_async=True)
        self.services.textToSpeech.stopAll(_async=True)
        self.services.audioPlayer.stopAll(_async=True)
