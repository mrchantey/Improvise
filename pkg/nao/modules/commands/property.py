

class PropertyCommand():

    def __init__(self, serviceModule):
        self.serviceModule = serviceModule

        def InitSpeechParam(paramName):
            return {
                'get': lambda: serviceModule.textToSpeech.getParameter(paramName),
                'set': lambda val: serviceModule.textToSpeech.setParameter(paramName, val),
            }

        def GetIpAddress():
            networks = self.serviceModule.connectionManager.services()
            connectedNetworks = filter(lambda n: n[3][1] == 'online', networks)
            ipInfo = connectedNetworks[0][9]
            return ipInfo[1][1][1]

        self.properties = {
            'all': {
                'get': self.GetBakedProperties
            },
            'ipAddress': {
                'get': GetIpAddress
            },
            'name': {
                'get': serviceModule.system.robotName,
                'set': serviceModule.system.setRobotName
            },
            'volume': {
                'get': serviceModule.audioDevice.getOutputVolume,
                'set': serviceModule.audioDevice.setOutputVolume
            },
            'speechVolume': InitSpeechParam('volume'),
            'speechSpeed': InitSpeechParam('speed'),
            'speechPitch': InitSpeechParam('pitch'),
            'behaviors': {
                'get': serviceModule.behaviorManager.getInstalledBehaviors
            },
            'autoState':
            {
                'get': serviceModule.autonomousLife.getState,
                'set': serviceModule.autonomousLife.setState
            }
        }

    def Run(self, command):

        if 'propertyName' in command:
            prop = self.properties[command['propertyName']]
            # passing paramameters implicitly declares a 'set'
            if 'propertyValue' in command:
                prop['set'](command['propertyValue'])
            val = prop['get']()
            return {
                'propertyName': command['propertyName'],
                'propertyValue': val,
                'responsePhrase': "the value of " + command['propertyName'] + " is " + str(val)
            }
        else:
            return {
                "propertyName": "all",
                "propertyValue": self.GetBakedProperties(),
                'responsePhrase': "all properties retrieved"
            }

    def GetBakedProperties(self):
        bakedProps = {}
        for key, value in self.properties.iteritems():
            if key != 'all':
                bakedProps[key] = value['get']()
        return bakedProps
