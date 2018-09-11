

class RunBehaviorCommand():

    def __init__(self, behaviorManagerService):
        self.behaviorManagerService = behaviorManagerService
        self.behaviors = self.behaviorManagerService.getInstalledBehaviors()
        # for behavior in self.behaviors:
        #     print behavior

    def Run(self, command):
        if not command['path'] in self.behaviors:
            print 'behavior not installed', command['path']
            return
        isRunning = self.behaviorManagerService.isBehaviorRunning(command['path'])
        if isRunning:
            print 'behavior already running:', command['path']
        else:
            self.behaviorManagerService.runBehavior(command['path'], _async=command['async'])
