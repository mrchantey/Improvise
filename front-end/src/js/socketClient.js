import io from "socket.io-client"
import { resolve } from "url";
import { rejects } from "assert";
import { Socket } from "net";//dont think we need this

export default (serverAddress) => {

    const client = {}
    // const socket = io(serverAddress)
    const socket = io(serverAddress, { reconnection: false })

    client.DisconnectServer = () => socket.close()
    // client.ConnectServer()


    client.ConnectRobot = (robotAddress) => {
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

    client.DisconnectRobot = (sessionId) => {
        socket.emit("DisconnectRobot", sessionId)
    }

    client.GetRobotBehaviors = (sessionId) => {
        socket.emit("GetRobotBehaviors", sessionId)
        return new Promise((resolve, reject) => {
            socket.on("SetRobotBehaviors", (behaviors) => resolve(behaviors))
        })
    }

    client.GetRobotName = (sessionId) => {
        socket.emit("GetRobotName", sessionId)
        return new Promise((resolve, reject) => {
            socket.on("SetRobotName", (name) => resolve(name))
        })
    }

    socket.on("connect", () => {
        console.log("Connected to server at " + serverAddress)
        if (client.onConnect !== undefined)
            client.onConnect()
    })
    socket.on("disconnect", () => {
        console.log("Disconnected from server at " + serverAddress)
        if (client.onDisconnect !== undefined)
            client.onDisconnect()
    })
    return client
}
