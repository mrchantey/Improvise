import json
import requests
from pkg.utilities.utility import parseType


def GetJson(url):
    res = requests.get(url)
    uniData = json.loads(res.text)
    return parseType(uniData)


# no 404 etc error handling
def PostJson(url, body):
    # strBody = json.dumps(body)
    # print 'making request'
    headers = {'Content-Type': 'application/json'}
    bodyStr = json.dumps(body)
    res = requests.post(url, data=bodyStr, headers=headers)
    try:
        uniData = json.loads(res.text)
        return parseType(uniData)
    except:
        return parseType(res.text)
    # res = requests.post(url, data=strBody)


# def TryPost(url, body):
#     try:
#         res = requests.post(url, json=body)
#         return True
#     except:
#         return False
