



export default (robotAddress, socketClient) => {
    const robotProxy = {
        sessionId: -1,
        name: undefined,
        ipAddress: undefined,
        behaviors: undefined,
        actions: undefined
    }

    return new Promise((resolve, reject) => {
        socketClient.ConnectRobot(robotAddress)
            .then((sessionId) => {
                robotProxy.sessionId = sessionId;
                robotProxy.ipAddress = robotAddress
                resolve(robotProxy)
                //return immediately

                socketClient.GetRobotName(sessionId)
                    .then((name) => {
                        robotProxy.name = name
                    })
                socketClient.GetRobotBehaviors(sessionId)
                    .then((behaviors) => {
                        robotProxy.behaviors = behaviors
                    })
            }, reject)
    })
}