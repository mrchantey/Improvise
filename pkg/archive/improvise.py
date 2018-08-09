import sys
from pkg import server
from pkg.modules.dialog import Dialog
from pkg.modules.weather import Weather
from pkg.modules.news import News
from pkg.modules.time import Time
from pkg.modules.activities import Activities
from pkg.modules.nao.nao import Nao


class Improvise():
    def __init__(self, ipAddress=None):
        self.weather = Weather()
        self.news = News()
        self.time = Time()
        self.activities = Activities()
        self.dialog = Dialog(self.weather, self.news, self.activities)
        if ipAddress != None:
            self.nao = Nao(ipAddress)
            if self.nao.isConnected == True:
                self.dialog.naoSayCallback = self.nao.methods.Say

        server.OnModuleRequest = self.OnRequest

    def Run(self):
        server.app.run(port=server.PORT, host="0.0.0.0")

    def OnRequest(self, moduleName, requestBody):
        attr = getattr(self, moduleName)
        return attr.OnRequest(requestBody)
        # return self.modules[moduleName].OnRequest(requestBody)


if __name__ == "__main__":
    improvise = Improvise(sys.argv[1]) if len(sys.argv) > 1 else Improvise()
    improvise.Run()
