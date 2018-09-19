

class CommandLoop():
    def __init__(self, RunCommandCallback):
        self.RunCommandCallback = RunCommandCallback

    def Run(self, commandLoop):
        for i in range(0, commandLoop['loopCount']):
            for command in commandLoop['commands']:
                self.RunCommandCallback(command)
