

class PropertyModule():

    def __init__(self, ipAddress, serviceMod):
        self.serviceMod = serviceMod

        def InitSpeechParam(paramName):
            return {
                'get': lambda: serviceMod.textToSpeech.getParameter(paramName),
                'set': lambda val: serviceMod.textToSpeech.setParameter(paramName, val),
            }
        self.properties = {
            'all': {
                'get': self.GetBakedProperties
            },
            'ipAddress': {
                'get': lambda: ipAddress
            },
            'name': {
                'get': serviceMod.system.robotName,
                'set': serviceMod.system.setRobotName
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

    def HandleRequest(self, kwargs):
        propName = kwargs['reqName']
        prop = self.properties[propName]
        print kwargs
        # passing paramameters implicitly declares a 'set'
        if 'params' in kwargs:
            prop['set'](kwargs['params']['value'])
        val = prop['get']()
        return {'key': propName,   'value': val}

    def GetBakedProperties(self):
        bakedProps = {}
        for key, value in self.properties.iteritems():
            if key != 'all':
                bakedProps[key] = value['get']()
        return bakedProps
