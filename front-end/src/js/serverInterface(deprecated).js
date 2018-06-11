import io from "socket.io-client"

export default (serverAddress, dev) => {

    const serverInterface = {
        robot: { name: 'na', ipAddress: 'na', behaviors: [], isConnected: false, volume: -1, autoState: 'na' },
        connectionStatus: "not connected"
    }


    //const socket = io(serverAddress, { reconnection: false })
    const socket = io(serverAddress)

    socket.on("connect", () => {
        console.log("Connected to server at " + serverAddress)
    })

    socket.on("disconnect", () => {
        console.log("Disconnected from server at " + serverAddress)
        serverInterface.robot.isConnected = false
    })

    socket.on("message", (msg) => console.log('message received: ', msg))

    //This should return a robot object with lots of data
    socket.on('RobotSend', (robot) => {
        // serverInterface.robot = robot
        console.log("Connected to robot at " + robot.ipAddress)
        console.log(robot)
        serverInterface.robot.name = robot.name
        serverInterface.robot.ipAddress = robot.ipAddress
        serverInterface.robot.volume = robot.volume
        serverInterface.robot.autoState = robot.autoState
        serverInterface.robot.behaviors = robot.behaviors
        serverInterface.robot.isConnected = true
        // serverInterface.robot.GetProperty = (property) =>
        //     socket.emit("RobotPropertyGet", {
        //         property
        //     })

        serverInterface.robot.SetProperty = (property, value) => {
            console.log('sending..\nproperty: ' + property + "\nvalue: " + value)
            socket.emit("RobotPropertySet", {
                property,
                value
            })
        }
        serverInterface.robot.DoMethod = (method, param1) => {
            console.log('doing..\nmethod: ' + method + '\nparameter: ' + param1)
            socket.emit("RobotMethodDo", {
                method,
                param1
            })
        }

        //TESTING AREA ON CONNECT-----------------------------------

        //  robot.DoMethod("setAutoState", "disabled")
        // robot.GetProperty("volume")
        serverInterface.robot.DoMethod("SayPhrase", "howdy")
        serverInterface.robot.SetProperty("volume", 15)

        //----------------------------------------------------------
    })

    socket.on('RobotPropertySend', (data) => {
        console.log('data received')
        console.log(data)
        serverInterface.robot[data.property] = data.value
    })

    socket.on('RobotEventTrigger', (data) => {
        console.log('event triggered..')
        console.log(data)
    })

    return serverInterface
}
