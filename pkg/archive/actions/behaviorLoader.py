def LoadBehaviors(behaviorPaths):
    rootItem = {
        'name': 'Behaviors',
        'type': 'collection',
        'items': []
    }
    for path in behaviorPaths:
        CreateItem(rootItem, path)
#     # actions = sorted(actions, key=lambda a: str.lower(a['name']))
    return rootItem


def CreateItem(rootItem, path):
    splitPath = path.split('/')
    parentItem = rootItem
    for i in range(0, len(splitPath)-1):
        parentItem = GetParentItem(parentItem, splitPath[i])
    parentItem['items'].append({
        "name": splitPath[len(splitPath)-1],
        "type": "behavior",
        'tags': splitPath[:-1],
        "path": path
    })


def GetParentItem(parentItem, dirName):
    # print 'PARENT', parentItem
    collectionItems = filter(lambda i: i['type'] == 'collection', parentItem['items'])
    matchingNames = filter(lambda i: i['name'] == dirName, collectionItems)
    if len(matchingNames) == 0:
        newDir = {
            'name': dirName,
            'type': 'collection',
            'items': []
        }
        # print 'NEW DIR', dirName
        parentItem['items'].append(newDir)
        return newDir
    else:
        return matchingNames[0]


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

    item = LoadBehaviors(behaviorPaths)
    # print item
