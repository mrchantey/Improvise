# from naoProxy import NaoProxy
from naoSession import NaoSession
# import unicodedata

activeSessions = []


def beginSession(ipAddress):
    naoSession = NaoSession()

    if(naoSession.Connect(ipAddress)):
        # naoSession.Say('session connected?')
        print ipAddress, 'fully connected!'
        activeSessions.append(naoSession)
        return len(activeSessions) - 1
    else:
        print ipAddress, 'failed to fully connect'
        return -1


if __name__ == '__main__':
    beginSession('10.50.16.67')


def getInstalledBehaviors(sessionId):
    installedBehaviors = activeSessions[sessionId].BehaviorManager.getInstalledBehaviors(
    )
    return installedBehaviors


def getName(sessionId):
    return activeSessions[sessionId].System.robotName()
