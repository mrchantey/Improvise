

class CommandSequence():
    def __init__(self, RunCommandCallback):
        self.RunCommandCallback = RunCommandCallback

    def Run(self, commandSequence):
        for command in commandSequence['commands']:
            self.RunCommandCallback(command)
