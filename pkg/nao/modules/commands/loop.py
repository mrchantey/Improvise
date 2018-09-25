from sequence import CommandSequence


class CommandLoop():
    def __init__(self, RunCommandCallback):
        self.sequence = CommandSequence(RunCommandCallback)
        self.RunCommandCallback = RunCommandCallback

    def Run(self, commandLoop):
        for i in range(0, commandLoop['loopCount']):
            self.sequence.Run(commandLoop)
