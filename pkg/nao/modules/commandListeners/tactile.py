

class TactileCommandListener():
    def __init__(self, eventModule, RunCommandCallback):
        self.eventModule = eventModule
        self.RunCommandCallback = RunCommandCallback
        self.headTouchedListeners = []
        self.leftHandTouchedListeners = []

    def StartListening(self):
        self.headTouchedListeners = (
            self.eventModule.AddListeners([
                "FrontTactilTouched",
                "MiddleTactilTouched",
                "RearTactilTouched"],
                self.OnHeadTouched))
        self.leftHandTouchedListeners = (
            self.eventModule.AddListeners([
                "HandLeftBackTouched",
                "HandLeftLeftTouched",
                "HandLeftRightTouched"],
                self.OnLeftHandTouched
            ))

    def StopListening(self):
        self.eventModule.RemoveListeners(self.headTouchedListeners)
        self.eventModule.RemoveListeners(self.leftHandTouchedListeners)

    def SubscribeToHeadTouch(self):
        return

    def OnHeadTouched(self, val):
        if not val == 1:
            return
        self.RunCommandCallback({
            'commandName': 'internal',
            'instruction': 'internalSpeechStartListening'
        })

    def OnLeftHandTouched(self, val):
        if not val == 1:
            return
        self.RunCommandCallback({
            'commandName': 'internal',
            'instruction': 'exitProgram'
        })
