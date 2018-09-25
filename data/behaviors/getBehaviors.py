import qi
import json

ipAddress = '192.168.0.121'

app = qi.Application()
session = qi.Session()
session.connect("tcp://" + ipAddress + ":9559")
behaviorManager = session.service("ALBehaviorManager")
behaviors = behaviorManager.getInstalledBehaviors()

with open('behaviors.json', 'w') as file:
    json.dump(behaviors, file)
