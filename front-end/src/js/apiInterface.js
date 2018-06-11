import { stat } from "fs";

export default (serverAddress, dev) => {

    const robot = {
        name: 'na',
        ipAddress: 'na',
        behaviors: [],
        isConnected: false,
        volume: -1,
        autoState: 'na',
        InitializeProperties,
        DoMethod,
        GetProperty,
        SetProperty,
        GetEvents
    }

    const apiInterface = {
        robot,
        connectionStatus: "not connected",
    }

    InitializeProperties()

    // GetProperty('Volume')
    // DoMethod('Dance')
    // MakeRequest(serverAddress + '/cors')
    function MakeRequest(url, body = undefined) {
        const request = (body == undefined) ? {} : {
            headers: {
                'content-type': "application/json"
            },
            method: 'POST',
            body: JSON.stringify(body)
        }
        const reqPrint = body == undefined ? '\nGET\n' : '\nPOST\n'
        console.log(reqPrint + url)
        return new Promise((resolve, reject) => {
            fetch(url, request)
                .then((response) => {
                    // console.log(response)
                    if (response.status == 200) {
                        const contentType = response.headers.get('content-type')
                        if (contentType == 'application/json') {
                            response.json().then((jsonBody) => {
                                resolve(jsonBody)
                            })
                        } else {
                            resolve(response.body)
                        }
                    } else if (response.status == 204)
                        console.log(response.status.toString() + '\nserver: connected\nrobot: disconnected')
                    else if (response.status >= 400)
                        console.log(response.status.toString() + '\noh moit just give up')
                })
                .catch((reason) => console.log(reason + "\nlikely server is unresponsive"))
        })
    }

    function InitializeProperties() {
        const url = serverAddress + '/property'
        MakeRequest(url)
            .then((props) => {
                console.log('All properties received')
                console.log(props.volume)
                //this apparently does not lead to losing references
                Object.assign(apiInterface.robot, props)
                apiInterface.connectionStatus = true
            })
    }

    function GetProperty(propName) {
        const url = serverAddress + "/property/" + propName
        MakeRequest(url)
            .then((prop) => console.log(prop))
    }

    function SetProperty(propName, propValue) {
        const url = serverAddress + "/property/" + propName
        MakeRequest(url, { 'value': propValue })
            .then((prop) => robot[propName] = prop['value'])
            .catch((status, err) => console.log(status, err))
    }

    function DoMethod(methName, param1) {
        const url = serverAddress + "/method/" + methName
        MakeRequest(url, { 'param1': param1 })
            .then((resBody) => console.log(resBody))
            .catch((status, err) => console.log(status + err))
    }

    function GetEvents(eventName) {
        const url = serverAddress + '/event'
        MakeRequest(url)
            .then((body) => console.log(body))
            .catch((status, err) => console.log(err))
    }

    return apiInterface
}
