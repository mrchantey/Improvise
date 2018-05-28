# from naoProxy import NaoProxy
from naoSession import NaoSession
# import unicodedata

activeSessions = []


def beginSession(ipAddress):
    naoSession = NaoSession()

    if(naoSession.Connect(ipAddress)):
        naoSession.Say('session connected?')
        activeSessions.append(naoSession)
        return len(activeSessions) - 1
    else:
        return -1


if __name__ == '__main__':
    beginSession('10.50.16.67')
