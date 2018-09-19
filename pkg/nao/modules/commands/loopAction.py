
# TO BE DEPRECATED


class LoopActionCommand():
    def __init__(self, RunCommandCallback):
        self.RunCommandCallback = RunCommandCallback

    def Run(self, command):
        for startCommand in command['startCommands']:
            self.RunCommandCallback(startCommand)
        for i in range(0, command['loopCount']):
            for loopCommand in command['loopCommands']:
                self.RunCommandCallback(loopCommand)
        for endCommand in command['endCommands']:
            self.RunCommandCallback(endCommand)
