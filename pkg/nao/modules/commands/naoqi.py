

class NaoQiCommand:
    def __init__(self, serviceModule):
        self.services = serviceModule.services

    def Run(self, command):
        method = getattr(self.services[command['serviceName']], command['methodName'])
        if 'param2' in command:
            returnVal = method(command['param1'], command['param2'], _async=command['async'])
        elif 'param1' in command:
            returnVal = method(command['param1'], _async=command['async'])
        else:
            returnVal = method(_async=command['async'])
        response = {
            "value": returnVal,
        }
        return response
