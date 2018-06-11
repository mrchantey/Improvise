
class NaoTest():

    def __init__(self):
        self.properties = {
            'isConnected': True,
            'ipAddress': '69.69.69.69',
            'name': 'Test Robot',
            'volume': 66,
            'behaviors': ['behavior1', 'behavior2'],
            'autoState': 'solitary'
        }

    def GetProperty(self, propName):
        # print 'property requested..', propName
        return self.properties[propName]

    def SetProperty(self, propName, propValue):
        # print 'setting property..', propName, propValue
        self.properties[propName] = propValue

    def DoMethod(self, methName, param1):
        pass
        # print 'doing method', methName, 'with parameter', param1, '..'
