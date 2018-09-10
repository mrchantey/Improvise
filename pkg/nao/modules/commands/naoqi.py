

class NaoQiCommand:
    def __init__(self, serviceModule):
        self.services = serviceModule.services

    def Run(self, command):
        method = getattr(self.services[command['serviceName']], command['methodName'])
        returnVal = method(command['param1'], _async=command['async'])
        response = {
            "value": returnVal,
            "responsePhrase": "naoqi command has run successfully, the return value is " + str(returnVal)
        }
        return response
