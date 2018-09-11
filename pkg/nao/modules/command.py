

from commands.say import SayCommand
from commands.naoqi import NaoQiCommand
from commands.property import PropertyCommand
from commands.action import ActionCommand
from commands.runBehavior import RunBehaviorCommand
from commands.pose import PoseCommand
from commands.internal import InternalCommand
from commands.loopAction import LoopActionCommand

from commandListeners.internalSpeech import InternalSpeechCommandListener
from commandListeners.tactile import TactileCommandListener


class CommandModule:
    def __init__(self, serviceModule, eventModule, speechRecognitionModule, ExitProgramCallback):

        actionCommand = ActionCommand(self.Run)
        speechTriggeredActions = actionCommand.GetSpeechTriggeredActions()
        internalSpeechCommandListener = InternalSpeechCommandListener(
            eventModule,
            speechRecognitionModule,
            self.Run,
            speechTriggeredActions)

        self.commandListeners = {
            'internalSpeech': internalSpeechCommandListener,
            'tactile': TactileCommandListener(eventModule, self.Run)
        }

        self.commands = {
            'say': SayCommand(serviceModule, eventModule),
            'naoqi': NaoQiCommand(serviceModule),
            'property': PropertyCommand(serviceModule),
            'action': actionCommand,
            'runBehavior': RunBehaviorCommand(serviceModule.services['ALBehaviorManager']),
            'pose': PoseCommand(serviceModule.services['ALMotion']),
            'internal': InternalCommand(ExitProgramCallback, self.commandListeners['internalSpeech']),
            'loopAction': LoopActionCommand(self.Run)
        }
        pass

    def StartAllListeners(self):
        for listener in self.commandListeners:
            self.commandListeners[listener].StartListening()

    def StopAllListeners(self):
        for listener in self.commandListeners:
            self.commandListeners[listener].StopListening()

    def Run(self, command):
        # print 'RUNNING COMMAND', command['commandName']
        if not 'async' in command:
            command['async'] = False
        # command = self.SetDefaultParameterts(command)
        response = self.commands[command['commandName']].Run(command)
        # self.ResponseAction(command, response)
        # print 'command has run:'
        # print response
        self.RunFollowupCommands(response)
        return {
            "command": command,
            "response": response
        }

    def RunFollowupCommands(self, response):
        if response == None:
            return
        if not 'followupCommands' in response:
            return
        for command in response['followupCommands']:
            self.Run(command)
