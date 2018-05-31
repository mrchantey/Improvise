import SocketClient from "./socketClient";
import RobotProxy from "./robotProxy"
import testRobot from "./test/testRobot"

export default (serverAddress, dev) => {

    const serverInterface = {
        connectedRobots: []
    }


    ////------------------TESTING STUFF----------------------
    const socketClient = {}

    serverInterface.connectedRobots.push(testRobot())
    serverInterface.connectedRobots.push(testRobot())
    serverInterface.connectedRobots.push(testRobot())
    serverInterface.connectedRobots.push(testRobot())
    serverInterface.connectedRobots.push(testRobot())
    //DISABLED FOR TESTING
    //    const socketClient = SocketClient(serverAddress)
    //----------------------

    serverInterface.ConnectRobot = (robotIP) => {
        RobotProxy(robotIP, socketClient).then((robot) => {
            console.log('robot created!')
            // console.log(robot)
            serverInterface.connectedRobots.push(robot)
        }, () => console.log('could not connect to robot at ' + robotIP))
    }

    socketClient.onConnect = () => {
        // console.log(serverInterface)
        //TESTING ONLY
        serverInterface.ConnectRobot("10.50.16.81")
    }
    socketClient.onDisconnect = () => {
        connectedRobots = []
    }

    return serverInterface
}
