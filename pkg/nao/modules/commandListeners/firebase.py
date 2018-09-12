
from threading import Thread
from pkg.utilities.requestsUtility import PostJson
import time
commandQueueKey = "robot/commandQueue"


class FirebaseCommandListener():
    def __init__(self, RunCommandCallback):
        self.RunCommandCallback = RunCommandCallback
        self.clear = False
        self.delay = 0
        self.killFlag = False

    def StartListening(self):
        print 'firebase listener listening'
        self.pollThread = Thread(name="firebasePollThread", target=self.PollFirebaseCommands)
        self.pollThread.setDaemon(True)
        self.pollThread.start()

    def StopListening(self):
        self.killFlag = True

    def PollFirebaseCommands(self):
        while self.killFlag == False:
            print 'polling firebase...'
            startTime = time.time()
            commands = self.GetCommandQueue()
            endTime = time.time()
            if self.clear:
                self.SetCommandQueue([])
            deltaTime = endTime - startTime
            print 'firebase data retrieved in', deltaTime, 'seconds'
            for command in commands:
                self.RunCommandCallback(command)

            time.sleep(self.delay)

    def GetCommandQueue(self):
        body = {
            "key": commandQueueKey
        }
        url = 'http://us-central1-improvise-communicate.cloudfunctions.net/databaseget'
        return PostJson(url, body)

    def SetCommandQueue(self, value):
        body = {
            "key": commandQueueKey,
            "value": value
        }
        url = 'http://us-central1-improvise-communicate.cloudfunctions.net/databaseset'
        return PostJson(url, body)


if __name__ == '__main__':
    def PrintCommand(command):
        print command
    firebaseCommandListener = FirebaseCommandListener(PrintCommand)
    firebaseCommandListener.StartListening()
    # firebaseCommandListener.SetCommandQueue([
    #     {
    #         "commandName": "say",
    #         "phrase": "here there be dragons"
    #     }
    # ])
