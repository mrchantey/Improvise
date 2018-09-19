
from pkg.utilities.utility import OpenJson


class CommandSequence():
    def __init__(self, RunCommandCallback):
        self.RunCommandCallback = RunCommandCallback
        # basicActions = OpenJson('pkg/data/actions/basic.json')
        # physioActions = OpenJson('pkg/data/actions/physio.json')
        # self.actions = basicActions + physioActions

    def Run(self, commandSequence):
        for command in commandSequence['commands']:
            self.RunCommandCallback(command)
        # return command['response']

    # def GetSpeechTriggeredActions(self):
    #     return filter(lambda a: "triggerPhrase" in a, self.actions)


# if __name__ == "__main__":
#     def bla():
#         print 'bla'
#     acc = ActionCommand(bla)
