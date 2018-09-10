

class RunBehaviorCommand():

    def __init__(self, behaviorManagerService):
        self.behaviorManagerService = behaviorManagerService

    def Run(self, command):
        isRunning = self.behaviorManagerService.isBehaviorRunning(command['path'])
        if isRunning:
            print 'behavior already running:', command['path']
        else:
            self.behaviorManagerService.runBehavior(command['path'], _async=command['async'])
