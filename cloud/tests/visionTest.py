import requests
from VideoCapture import Device
import base64
import requests


def SendRequest(img64):
    jsonBody = {
        "image": {
            "content": img64
        }
    }

    res = requests.post("https://us-central1-improvise-communicate.cloudfunctions.net/visionfaces", json=jsonBody)

    print res.status_code
    result = res.json()[0]
    print result


# imgWrite = open('selfie64.txt', 'w')
# base64.encode(img, imgWrite)
# img = open('image.jpg', 'r').read()
# img64 = base64.encodestring(img)
# img64 = base64.


# print len(img64)
# img64 = open('selfie64.txt').read()
# print len(img64)
cam = Device()
cam.saveSnapshot('image.jpg')
imgFile = open('image.jpg', 'rb')
img = imgFile.read()
img64 = base64.b64encode(img)

SendRequest(img64)


# >>> r = requests.post('http://httpbin.org/post', json={"key": "value"})
# >>> r.status_code
# 200
# >>> r.json()

# base64.encode(img, output)
