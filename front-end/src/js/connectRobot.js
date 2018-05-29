



export default (robotAddress, messenger) => {
    const robot = {
        sessionId: -1,
        name: undefined,
        ipAddress: undefined,
        behaviors: undefined
    }

    return new Promise((resolve, reject) => {
        messenger.ConnectRobot(robotAddress)
            .then((sessionId) => {
                resolve(robot)
                robot.sessionId = sessionId;
                robot.ipAddress = robotAddress
                messenger.GetRobotBehaviors(sessionId)
                    .then((behaviors) => {
                        robot.behaviors = behaviors
                    })
                messenger.GetRobotName(sessionId)
                    .then((name) => {
                        robot.name = name
                    })
            }, reject)
    })
}