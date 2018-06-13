# from naoInterface import NaoInterface
import sys
sys.path.append("C:/Users/yellowcat/Documents/GitHub/Improvise/back-end")
import naoInterface
from utilservices import actionLoader


class ActionModule():

    def __init__(self, serviceMod, propertyMod, methodMod):
        behaviorPaths = propertyMod.GetProperty('behaviors')
        # behaviorPaths = [
        #     ".lastUploadedChoregrapheBehavior/behavior_1",
        #     "animationMode",
        #     "animations/SitOnPod/Emotions/Neutral/Hello_1",
        #     "animations/SitOnPod/Gestures/Yes_1",
        #     "animations/SitOnPod/Gestures/Me_7",
        #     "animations/SitOnPod/Gestures/Yes_2"]

        def ClosureSafeRunAssignment(info):
            def noAction():
                print 'no matching action for type', info['type']

            if info['type'] == 'speech':
                return lambda: methodMod.DoMethod('Say', [info['text'], True])
            elif info['type'] == 'behavior':
                return lambda: methodMod.DoMethod('RunBehavior', [info['path']])
            elif info['type'] == 'audio':
                return lambda: methodMod.DoMethod('PlayAudio', [info['path']])
            else:
                return noAction

        actionInfos = actionLoader.LoadActionInfo(behaviorPaths)
        self.actions = []

        for info in actionInfos:
            self.actions.append({
                'info': info,
                'Run': ClosureSafeRunAssignment(info)
            })

    def RunAction(self, actionId):
        idMatches = filter(lambda a: a['info']['id'] == actionId, self.actions)
        if len(idMatches) != 1:
            print 'run action error, mismatched id', actionId, idMatches
            return
        action = idMatches[0]
        print 'running action..', action['info']['name']
        action['Run']()

    def GetBakedActions(self):
        bakedActions = map(lambda a: a['info'], self.actions)
        return bakedActions


if __name__ == "__main__":
    ipAddress = "10.50.16.54"
    nao = naoInterface.NaoInterface(ipAddress)
    # print nao.actionMod
    # nao.actionMod.RunAction(1)

    # nao.actionMod.RunAction(615)
    # nao.actionMod.RunAction(467)
    # try:
    #     while True:
    #         pass
    # except KeyboardInterrupt:
    #     pass
