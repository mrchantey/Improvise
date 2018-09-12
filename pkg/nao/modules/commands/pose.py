from pkg.utilities.utility import OpenJson


class PoseCommand():

    def __init__(self, alMotion):
        self.alMotion = alMotion
        poses_raw = OpenJson("pkg/data/poses/poses.json")
        folders = poses_raw['ChoregraphePositionLibrary']['folder']
        self.poses = self.FilterPoseMotors(folders)

        # self.alMotion.stiffnessInterpolation('Body', 1, 0.01)
        # self.alMotion.angleInterpolation('HeadYaw', [-1, 1], [1, 2], True, _async=False)
        # self.alMotion.angleInterpolation(['LWristYaw'], [1.82134], 1, True)
        # alMotion.rest()
        # alMotion.wakeUp()
        # self.Run({"poseName": "Head/look_down_right", "async": False})

    def Run(self, command):
        pose = filter(lambda p: p['name'] == command['poseName'], self.poses)[0]
        speed = command['speed'] if 'speed' in command else 1
        if pose == None:
            print 'pose not found:', command['poseName']
        motorNames = map(lambda m: m['name'], pose['motors'])
        motorValues = map(lambda m: m['value'], pose['motors'])
        self.alMotion.angleInterpolation(motorNames, motorValues, speed, True, _async=command['async'])

    def FilterPoseMotors(self, folders):
        poseFilters = OpenJson("pkg/data/poses/poseFilters.json")
        poses = []
        for folder in folders:
            poseFilter = poseFilters[folder['title']]
            rawPoses = folder['position'] if type(folder['position']) == list else [folder['position']]
            for pose in rawPoses:
                rawMotors = pose["Motors"]["Motor"]
                motors = filter(lambda m: m['name'] in poseFilter['motors'], rawMotors)
                name = folder['title'] + '/' + pose['name']
                poses.append({
                    "name": name,
                    "motors": motors
                })
        return poses


if __name__ == "__main__":
    postureCommand = PoseCommand(None)
