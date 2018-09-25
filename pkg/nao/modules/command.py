

from commands.say import SayCommand
from commands.naoqi import NaoQiCommand
from commands.property import PropertyCommand
from commands.action import ActionCommand
from commands.runBehavior import RunBehaviorCommand
from commands.pose import PoseCommand
from commands.internal import InternalCommand
from commands.loopAction import LoopActionCommand
from commands.loop import CommandLoop
from commands.sequence import CommandSequence
from commands.event import EventCommand

from commandListeners.internalSpeech import InternalSpeechCommandListener
from commandListeners.tactile import TactileCommandListener
from commandListeners.firebase import FirebaseCommandListener


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
            'tactile': TactileCommandListener(eventModule, self.Run),
            'firebase': FirebaseCommandListener(self.Run)
        }

        self.commands = {
            'say': SayCommand(serviceModule, eventModule),
            'naoqi': NaoQiCommand(serviceModule),
            'property': PropertyCommand(serviceModule),
            'action': actionCommand,
            'event': EventCommand(eventModule),
            'runBehavior': RunBehaviorCommand(serviceModule.services['ALBehaviorManager']),
            'pose': PoseCommand(serviceModule.services['ALMotion']),
            'commandSequence': CommandSequence(self.Run),
            'commandLoop': CommandLoop(self.Run),
            'internal': InternalCommand(ExitProgramCallback, self.commandListeners['internalSpeech']),
            'loopAction': LoopActionCommand(self.Run)
        }

    def StartAllListeners(self):
        self.commandListeners['tactile'].StartListening()
        print "only tactile listening"
        # self.commandListeners['firebase'].StartListening()
        # for listener in self.commandListeners:
        # self.commandListeners[listener].StartListening()

    def StopAllListeners(self):
        for listener in self.commandListeners:
            self.commandListeners[listener].StopListening()

    def Run(self, command):
        # print 'RUNNING COMMAND', c`ommand['commandName']
        if not 'async' in command:
            command['async'] = False
        response = self.commands[command['commandName']].Run(command)
        # print 'COMMAND HAS RUN`:
        # print response
        self.RunFollowupCommands(response)
        returnData = {
            "command": command,
            "response": response
        }
        return returnData

    def RunFollowupCommands(self, response):
        if response == None:
            return
        if not 'followupCommands' in response:
            return
        for command in response['followupCommands']:
            self.Run(command)
