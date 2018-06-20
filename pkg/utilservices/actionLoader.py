import utility


def LoadActionInfo(behaviorPaths):
    idCount = 0
    actions = []
    fileResults = ParseFile(idCount)
    idCount = fileResults['idCount']
    actions += fileResults['actions']
    behaviorResults = ParseBehaviors(behaviorPaths, idCount)
    idCount = behaviorResults['idCount']
    actions += behaviorResults['actions']
    # actions.append(result['actions'])
    return actions


def ParseFile(idCount):
    actionData = utility.OpenJson('pkg/data/actions.json')
    actions = actionData['actions']
    for action in actions:
        action['id'] = idCount
        idCount += 1
        try:
            action['type']
        except:
            action['type'] = 'UNKNOWN'
            print 'unknown action type', action
    return {'idCount': idCount, 'actions': actions}


def ParseBehaviors(behaviorPaths, idCount):
    behaviorPaths = sorted(behaviorPaths, key=str.lower)
    actions = []
    for path in behaviorPaths:
        splitPath = path.split('/')
        actions.append({
            'id': idCount,
            'name': splitPath[len(splitPath)-1],
            'type': 'behavior',
            'tags': splitPath[:-1],
            'path': path
        })
        idCount += 1
    # actions = sorted(actions, key=lambda a: str.lower(a['name']))
    return {'idCount': idCount, 'actions': actions}


if __name__ == '__main__':
    behaviorPaths = [
        ".lastUploadedChoregrapheBehavior/behavior_1",
        "animationMode",
        "animations/SitOnPod/Emotions/Neutral/Hello_1",
        "animations/SitOnPod/Gestures/Yes_1",
        "animations/SitOnPod/Gestures/Me_7",
        "animations/SitOnPod/Gestures/Yes_2",
        "dialog_switch_language/bhr_switch_language",
        "dialog_switch_language/bhr_check_language_packs",
        "dialog_touch/headster_egg",
        "dialog_touch/animations/head_touched",
        "exploration",
        "fall-recovery/recover",
        "fall-recovery/plugin",
        "follow-me",
        "go-to-rest",
        "grasping",
        "grasping/animations/ExtendHand",
        "grasping/animations/Missed",
        "grasping/animations/ThankYou",
        "grasping/animations/ObserveObject2"]
    actions = LoadActionInfo(behaviorPaths)
    for action in actions:
        print action['name']
