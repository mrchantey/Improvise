import time


class InternalCommand():
    def __init__(self, ExitProgramCallback, internalSpeechCommandListener):
        self.exitProgramCallback = ExitProgramCallback
        self.internalSpeechCommandListener = internalSpeechCommandListener

    def Run(self, command):
        if command['instruction'] == 'exitProgram':
            self.exitProgramCallback()
        elif command['instruction'] == 'internalSpeechStartListening':
            self.internalSpeechCommandListener.StartListening()
        elif command['instruction'] == 'pause':
            time.sleep(command['duration'])
