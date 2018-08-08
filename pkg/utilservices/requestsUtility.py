import json
import requests
from pkg.utilservices.utility import parseType


def GetJson(url):
    res = requests.get(url)
    uniData = json.loads(res.text)
    return parseType(uniData)


# no 404 etc error handling
def PostJson(url, body):
    res = requests.post(url, json=body)
    return parseType(res.text)


def TryPost(url, body):
    try:
        res = requests.post(url, json=body)
        return True
    except:
        return False
