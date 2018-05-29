import io from "socket.io-client"
import { resolve } from "url";
import { rejects } from "assert";
import { Socket } from "net";

export default (serverAddress) => {

    const messenger = {}
    const socket = io(serverAddress)

    //   messenger.ConnectServer = () => socket = io(serverAddress)
    messenger.DisconnectServer = () => socket.close()

    // messenger.ConnectServer()


    messenger.ConnectRobot = (robotAddress) => {
        console.log("Connecting to robot at " + robotAddress + "..")
        socket.emit("ConnectRobot", robotAddress)
        return new Promise((resolve, reject) => {
            socket.on('ConnectRobotResolve', (sessionId) => {
                console.log("Connected to robot at " + robotAddress + "\nSession id: " + sessionId)
                resolve(sessionId)
            })
            socket.on('ConnectRobotReject', () => {
                console.log("Unable to connect to robot at " + robotAddress)
                reject(robotAddress)
            })
        })
    }

    messenger.DisconnectRobot = (robot) => {
        socket.emit("DisconnectRobot", robot)
    }

    messenger.GetRobotBehaviors = (sessionId) => {
        socket.emit("GetRobotBehaviors", sessionId)
        return new Promise((resolve, reject) => {
            socket.on("SetRobotBehaviors", (behaviors) => resolve(behaviors))
        })
    }

    messenger.GetRobotName = (sessionId) => {
        socket.emit("GetRobotName", sessionId)
        return new Promise((resolve, reject) => {
            socket.on("SetRobotName", (name) => resolve(name))
        })
    }

    socket.on("connect", () => {
        console.log("Connected to server at " + serverAddress)
        if (messenger.onConnect !== undefined)
            messenger.onConnect()
    })
    socket.on("disconnect", () => {
        console.log("Disconnected from server at " + serverAddress)
        if (messenger.onDisconnect !== undefined)
            messenger.onDisconnect()
    })
    return messenger
}
