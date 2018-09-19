import requests
import json
from utilities.requestsUtility import PostJson


class BackEndClient():
    def __init__(self, serverAddress):
        self.serverAddress = "http://" + serverAddress

    def MakeRequest(self, body):
        print 'making request..'
        response = PostJson(self.serverAddress, body)
        print 'response revieved'
        return response


if __name__ == "__main__":
    backendClient = BackEndClient("localhost:3000")
    # body = {
    #     'queryText': 'whats going on'
    # }    }

    response = backendClient.MakeRequest(body)
    print response
