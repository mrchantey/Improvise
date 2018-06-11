import sys
import time


from naoqi import ALProxy
from naoqi import ALBroker
from naoqi import ALModule

from optparse import OptionParser

NAO_IP = "10.50.16.55"
#NAO_IP = "nao.local"


#tts = ALProxy("ALTextToSpeech", NAO_IP, 9559)
#tts.say("Hello, world!")

HumanGreeter = None
memory = None


class HumanGreeterModule(ALModule):

    def __init__(self, name):
        ALModule.__init__(self, name)
        self.tts = ALProxy("ALTextToSpeech")

        global memory
        memory = ALProxy("ALMemory")
        memory.subscribeToEvent("FaceDetected",
                                "HumanGreeter",
                                "onFaceDetected")

    def onFaceDetected(self, *_args):
        memory.unsubscribeToEvent("FaceDetected",
                                  "HumanGreeter")

       # self.tts.say("yay, a person!")
        print(time.clock())

        memory.subscribeToEvent("FaceDetected",
                                "HumanGreeter",
                                "onFaceDetected")


def main():
    parser = OptionParser()
    parser.add_option("--pip",
                      help="Parent broker port. The IP address or your robot",
                      dest="pip")
    parser.add_option("--pport",
                      help="Parent broker port. The port  NAOqi is listening to",
                      dest="pport",
                      type="int")
    parser.set_defaults(
        pip=NAO_IP,
        pport=9559)

    (opts, args_) = parser.parse_args()
    pip = opts.pip
    pport = opts.pport

    myBroker = ALBroker("myBroker",
                        "0.0.0.0",
                        0,
                        pip,
                        pport)

    global HumanGreeter
    HumanGreeter = HumanGreeterModule("HumanGreeter")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print
        print "Key Pressed, Exiting"
        myBroker.shutdown()
        sys.exit(0)


if __name__ == "__main__":
    main()
