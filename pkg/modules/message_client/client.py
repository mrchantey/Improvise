from pkg.utilservices.requestsUtility import TryPost, PostJson


class MessageClient():
    def __init__(self, serverIP):
        self.serverIP = serverIP
        self.clientIP = ''
        self.messageURL = "http://" + self.serverIP + "/message"
        self.isConnected = False
        self.Ping()

    def Ping(self):
        pingStatus = TryPost(self.messageURL, {"heading": "ping"})
        self.isConnected = pingStatus
        print 'ping status:', pingStatus

    def Connect(self, deviceName, deviceIP):
        self.clientIP = deviceIP
        content = {
            "deviceName": deviceName,
            "deviceType": "NAO Robot",
            "deviceIPAddress": self.clientIP
        }
        self.SendMessage("naoRobot", "connect", content)

    def Disconnect(self):
        self.SendMessage("naoRobot", "disconnect", {})

    def SendMessage(self, senderType, heading, content):
        if not self.isConnected:
            return {
                'code': -2,
                'content': "server not connected"
            }
        reqBody = {
            "senderIP": self.clientIP,
            "senderType": senderType,
            "heading": heading,
            "content": content
        }
        resBody = PostJson(self.messageURL, reqBody)
        print resBody
        return resBody


if __name__ == "__main__":
    body = {"name": "captain joe"}
    client = MessageClient("10.50.16.50:3000")
    client.Connect("Jimmy", "10.50.16.50")
    client.Disconnect()
    # res = utility.PostJson("http://10.50.16.50:3000", body)
