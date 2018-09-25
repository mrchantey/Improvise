from pkg.utilities.utility import OpenJson


class PoseCommand():

    def __init__(self, alMotion):
        self.alMotion = alMotion
        self.poses = OpenJson("data/poses/poses.json")

    def Run(self, command):
        print "POSE COMMAND"
        self.alMotion.setStiffnesses("Body", 1)

        pose = filter(lambda p: p['name'] == command['poseName'], self.poses)[0]
        speed = command['speed'] if 'speed' in command else 1
        if pose == None:
            print 'pose not found:', command['poseName']

        motorNames = map(lambda m: m['name'], pose['motors'])
        motorValues = map(lambda m: m['value'], pose['motors'])

        self.alMotion.angleInterpolation(motorNames, motorValues, speed, True, _async=command['async'])
