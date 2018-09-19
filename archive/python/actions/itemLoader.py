from pkg.utilities import utility, itemUtils
from monologLoader import LoadMonologs
from behaviorLoader import LoadBehaviors


def LoadItems(behaviorPaths):
    rootItem = {
        'name': 'root',
        'type': 'collection',
        'items': []
    }
    rootItem['items'].append(LoadMonologs('pkg/data/monologues.json'))
    rootItem['items'].append(utility.OpenJson('pkg/data/albums.json'))
    rootItem['items'].append(LoadBehaviors(behaviorPaths))
    RecursivelyAssignId(rootItem)

    return rootItem


def RecursivelyAssignId(item, idCount=0):
    idCount += 1
    item['id'] = idCount
    if item['type'] == 'collection':
        for subItem in item['items']:
            idCount = RecursivelyAssignId(subItem, idCount)
    return idCount


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
    item = LoadItems(behaviorPaths)

    def printFunc(item):
        print item['id'], item['name']

    itemUtils.DoRecursive(item, printFunc)
