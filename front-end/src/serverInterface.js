import io from "socket.io-client"



export default (serverAddress, dev) => {

    const serverInterface = {
        serverURL: ''
    }

    console.log("Connecting to server at " + serverAddress)
    const socket = io(serverAddress)

    socket.on("connect", () => {
        if (dev) console.log("socket connected to server")
        //FOR TESTING
        serverInterface.ConnectRobot('10.50.16.67')
    })

    socket.on('ConnectRobotFail', () => {
        console.log('connection failed..')
    })

    socket.on('ConnectRobotSuccess', (id) => {
        console.log('connection succeeded with session id ' + id)
    })


    serverInterface.ConnectRobot = (ipAddress) => {
        socket.emit("ConnectRobot", {
            ipAddress
        })

    }

    serverInterface.SendMessage = (msg) => {
        socket.send(msg)
        if (dev) {
            console.log("message sent to server:")
            console.log(msg)
        }
    }

    return serverInterface
}