

class PropertyModule():

    def __init__(self, ipAddress, serviceMod):
        self.serviceMod = serviceMod

        def InitSpeechParam(paramName):
            return {
                'get': lambda: serviceMod.textToSpeech.getParameter(paramName),
                'set': lambda val: serviceMod.textToSpeech.setParameter(paramName, val),
            }

        def GetIpAddress():
            networks = self.serviceMod.connectionManager.services()
            connectedNetworks = filter(lambda n: n[3][1] == 'online', networks)
            ipInfo = connectedNetworks[0][9]
            return ipInfo[1][1][1]

        self.properties = {
            'all': {
                'get': self.GetBakedProperties
            },
            'ipAddress': {
                'get': GetIpAddress
                # 'get': lambda: ipAddress
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

    def HandleRequest(self, params):

        if 'propertyName' in params:
            prop = self.properties[params['propertyName']]
            # passing paramameters implicitly declares a 'set'
            if 'propertyValue' in params:
                prop['set'](params['propertyValue'])
            val = prop['get']()
            return {'key': params['propertyName'],   'value': val}
        else:
            return self.GetBakedProperties()

    def GetBakedProperties(self):
        bakedProps = {}
        for key, value in self.properties.iteritems():
            if key != 'all':
                bakedProps[key] = value['get']()
        return bakedProps
