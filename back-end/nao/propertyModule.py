

class PropertyModule():

    def __init__(self, ipAddress, serviceMod):
        self.serviceMod = serviceMod

        def InitSpeechParam(paramName):
            return {
                'get': lambda: serviceMod.textToSpeech.getParameter(paramName),
                'set': lambda val: serviceMod.textToSpeech.setParameter(paramName, val),
            }
        self.properties = {
            'ipAddress': {
                'get': lambda: ipAddress
            },
            'name': {
                'get': serviceMod.system.robotName
            },
            'volume': {
                'get': serviceMod.audioDevice.getOutputVolume,
                'set': serviceMod.audioDevice.setOutputVolume
            },
            'speechVolume': InitSpeechParam('volume'),
            'speechSpeed': InitSpeechParam('speed'),
            'speechPitch': InitSpeechParam('pitch'),
            'behaviors': {
                'get': serviceMod.behaviorManager.getInstalledBehaviors
            },
            'autoState':
            {
                'get': serviceMod.autonomousLife.getState,
                'set': serviceMod.autonomousLife.setState
            }
        }

    def GetProperty(self, propName):
        propValue = self.properties[propName]['get']()
        return propValue

    def SetProperty(self, propName, propValue):
        self.properties[propName]['set'](propValue)
        return self.properties[propName]['get']()

    def GetBakedProperties(self):
        bakedProps = {}
        for key, value in self.properties.iteritems():
            bakedProps[key] = value['get']()
        return bakedProps


# class PropertyModule():

#     def __init__(self, ipAddress, serviceMod):
#         self.serviceMod = serviceMod
#         self.properties = {
#             'ipAddress': ipAddress,
#             'name': serviceMod.system.robotName(),
#             'volume': serviceMod.audioDevice.getOutputVolume(),
#             'behaviors': serviceMod.behaviorManager.getInstalledBehaviors(),
#             'autoState': serviceMod.autonomousLife.getState()
#         }

#     def GetProperty(self, propName):
#         if propName == 'volume':
#             propValue = self.serviceMod.audioDevice.getOutputVolume()
#             self.properties[propName] = propValue
#             return propValue

#     def SetProperty(self, propName, propValue):
#         if propName == 'volume':
#             self.serviceMod.audioDevice.setOutputVolume(propValue)
#             self.properties[propName] = propValue
