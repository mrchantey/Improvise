from pkg.utilities.utility import OpenJson


class PoseCommand():

    def __init__(self, alMotion):
        self.alMotion = alMotion
        self.poses = OpenJson("data/poses/generatedPoses.json")

    def Run(self, command):
        print "POSE COMMAND"
        self.alMotion.setStiffnesses("Body", 1)

        pose = filter(lambda p: p['fullName'] == command['fullName'], self.poses)[0]
        speed = command['speed'] if 'speed' in command else 2
        if pose == None:
            print 'pose not found:', command['poseName']

        motorNames = map(lambda m: m['name'], pose['motors'])
        # motorValues = map(lambda m: m['value'], pose['motors'])
        motorValues = map(lambda m: [m['value']], pose['motors'])
        # motorSpeeds = map(lambda m: speed, pose['motors'])
        motorSpeeds = map(lambda m: [speed], pose['motors'])
        self.alMotion.angleInterpolation(motorNames, motorValues, motorSpeeds, True, _async=command['async'])
        # self.alMotion.angleInterpolationBezier(motorNames, motorSpeeds, motorValues, _async=command['async'])
