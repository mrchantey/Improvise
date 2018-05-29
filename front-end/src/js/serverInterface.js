
import socketMessenger from "./socketMessenger";
import connectRobot from "./connectRobot"
import io from "socket.io-client"

export default (serverAddress, dev) => {

    const serverInterface = {
        connectedRobots: []
    }

    const messenger = socketMessenger(serverAddress)

    serverInterface.ConnectRobot = (robotIP) => {
        connectRobot(robotIP, messenger).then((robot) => {
            console.log('robot created!')
            // console.log(robot)
            serverInterface.connectedRobots.push(robot)
        }, () => console.log('could not connect to robot at ' + robotIP))
    }

    messenger.onConnect = () => {
        console.log(serverInterface)
        serverInterface.ConnectRobot("10.50.16.67")
    }
    messenger.onDisconnect = () => {
        connectedRobots = []
    }

    return serverInterface
}
