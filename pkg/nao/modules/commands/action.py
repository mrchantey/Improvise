
from pkg.utilities.utility import OpenJson


class ActionCommand():
    def __init__(self, RunCommandCallback):
        self.RunCommandCallback = RunCommandCallback
        self.actions = OpenJson('pkg/data/actions.json')

    def Run(self, command):
        subResponse = ''
        for subCommand in command['subCommands']:
            subResponse = self.RunCommandCallback(subCommand)
        if 'responsePhrase' in command:
            return{"responsePhrase": command['responsePhrase']}
        else:
            return {"responsePhrase": subResponse}

    def GetSpeechTriggeredActions(self):
        return filter(lambda a: "triggerPhrase" in a, self.actions)


if __name__ == "__main__":
    def bla():
        print 'bla'
    acc = ActionCommand(bla)
