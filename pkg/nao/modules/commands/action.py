
from pkg.utilities.utility import OpenJson


class ActionCommand():
    def __init__(self, RunCommandCallback):
        self.RunCommandCallback = RunCommandCallback
        basicActions = OpenJson('pkg/data/actions/basic.json')
        physioActions = OpenJson('pkg/data/actions/physio.json')
        self.actions = basicActions + physioActions

    def Run(self, command):
        for subCommand in command['subCommands']:
            self.RunCommandCallback(subCommand)
        # return command['response']

    def GetSpeechTriggeredActions(self):
        return filter(lambda a: "triggerPhrase" in a, self.actions)


if __name__ == "__main__":
    def bla():
        print 'bla'
    acc = ActionCommand(bla)
