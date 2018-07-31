import sys
from pkg.utilservices import itemUtils
from itemLoader import LoadItems


class ActionModule():

    def __init__(self,  propertyMod, methodMod):
        behaviorPaths = propertyMod.properties['behaviors']['get']()
        behaviorPaths.sort()
        # print type(behaviorPaths)
        # behaviorPaths = behaviorPaths.sort()
        # behaviorPaths = [
        #     ".lastUploadedChoregrapheBehavior/behavior_1",
        #     "animationMode",
        #     "animations/SitOnPod/Emotions/Neutral/Hello_1",
        #     "animations/SitOnPod/Gestures/Yes_1",
        #     "animations/SitOnPod/Gestures/Me_7",
        #     "animations/SitOnPod/Gestures/Yes_2"]

        def ClosureSafeRunAssignment(item):
            def noAction():
                print 'no matching action for type', item['type']
            if item['type'] == 'speech':
                return lambda: methodMod.DoMethod('Say', {"phrase": item['text'], "animated": True})
            elif item['type'] == 'behavior':
                return lambda: methodMod.DoMethod('RunBehavior', {"path": item['path']})
            elif item['type'] == 'audio':
                return lambda: methodMod.DoMethod('PlayAudio', {"path": item['path']})
            else:
                return noAction

        def CreateActions():
            rootItem = LoadItems(behaviorPaths)
            flatItems = itemUtils.RecursiveFlatten(rootItem)
            actions = map(
                lambda i: {"info": i, "run": ClosureSafeRunAssignment(i)}, flatItems)
            return actions

        self.actions = CreateActions()

    def HandleRequest(self, params):
        if 'id' in params:
            self.RunAction(params['id'])
            return {'success': True, 'info': self.ActionById(params['id'])['info']}
        else:
            return self.GetBakedActions()

    def ActionById(self, actionId):
        idMatches = filter(lambda a: a['info']['id'] == actionId, self.actions)
        if len(idMatches) != 1:
            print 'action id error, mismatched id', actionId, idMatches
        return idMatches[0]

    def RunAction(self, actionId):
        action = self.ActionById(actionId)
        if action != None:
            action['run']()
        else:
            print 'No action with id', actionId, 'found'

    def GetBakedActions(self):
        bakedActions = map(lambda a: a['info'], self.actions)
        return bakedActions


if __name__ == "__main__":
    pass
