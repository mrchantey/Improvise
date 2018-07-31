import datetime


class Time():
    def __init__(self):
        pass

    def OnRequest(self, requestBody):
        return self.GetTime()

    def GetTime(self):
        now = datetime.datetime.now()
        return {"currentTime": str(now)}
