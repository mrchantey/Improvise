

from commands.say import SayCommand
from commands.naoqi import NaoQiCommand
from commands.property import PropertyCommand
from commands.action import ActionCommand
from commandListeners.internalSpeech import InternalSpeechCommandListener


class CommandModule:
    def __init__(self, serviceModule, eventModule, speechRecognitionModule):
        self.commands = {
            'say': SayCommand(serviceModule, eventModule),
            'naoqi': NaoQiCommand(serviceModule),
            'property': PropertyCommand(serviceModule),
            'action': ActionCommand(self.Run)
        }
        speechTriggeredActions = self.commands['action'].GetSpeechTriggeredActions()
        self.commandListeners = {
            'internalSpeech': InternalSpeechCommandListener(
                eventModule,
                speechRecognitionModule,
                self.Run,
                speechTriggeredActions)
        }
        pass

    def StartAllListeners(self):
        for listener in self.commandListeners:
            self.commandListeners[listener].StartListening()

    def StopAllListeners(self):
        for listener in self.commandListeners:
            self.commandListeners[listener].StopListening()

    def Run(self, command):
        command = self.SetDefaultParameterts(command)
        response = self.commands[command['commandName']].Run(command)
        self.ResponseAction(command, response)
        print 'command has run:'
        print response
        return response

    def ResponseAction(self, command, response):
        responsePhrase = None
        if 'responsePhrase' in command:
            responsePhrase = command['responsePhrase']
        if not 'sayResponsePhrase' in command:
            print 'No say response phrase'
        elif (command['sayResponsePhrase'] == True and
              not command['commandName'] == 'say' and
              'responsePhrase' in response):
            responsePhrase = response['responsePhrase']
        if responsePhrase != None:
            self.Run({
                "commandName": "say",
                "async": True,
                "phrase": response['responsePhrase']
            })

    def SetDefaultParameterts(self, command):
        if not 'async' in command:
            command['async'] = False
        if 'responsePhrase' in command:
            command['sayResponsePhrase'] = False
        return command
