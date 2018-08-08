


const devices = []

function CheckDeviceConnected(message) {
    return devices.find(d => d.ipAddress === message.senderIP) !== undefined
}

function CreateDeviceInfo(message) {
    return {
        name: message.content.deviceName,
        ipAddress: message.content.deviceIPAddress,
        deviceType: message.content.deviceType
    }
}

function CreateResponse(code, content) {
    return {
        code,
        content
    }
}

function HandleConnect(message) {
    if (!CheckDeviceConnected(message)) {
        const device = CreateDeviceInfo(message)
        devices.push(device)
        return CreateResponse(0, 'device connected')
    } else {
        return CreateResponse(-1, "device already connected")
    }
}

function HandleDisconnect(message) {
    if (CheckDeviceConnected(message)) {
        const device = devices.find(d => d.ipAddress === message.ipAddress)
        const index = devices.indexOf(device)
        devices.splice(index, 1)
        return CreateResponse(0, "device disconnected")
    } else {
        return CreateResponse(-1, "device not connected")
    }
}

function DirectMessage(message) {
    switch (message.heading) {
        case "ping":
            return CreateResponse(0, "success")
        case "connect":
            return HandleConnect(message)
        case "disconnect":
            return HandleDisconnect(message)
    }
}

module.exports = {
    HandleMessage: function (message) {
        response = DirectMessage(message)
        console.log(`message handled with code: ${response.code}`)
        return response
    }

}