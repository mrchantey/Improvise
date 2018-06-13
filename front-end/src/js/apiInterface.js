import { stat } from "fs";
import FilterEvents from "./EventFilter";

// window.pollEvents = true
window.pollEvents = false


export default (serverAddress, dev) => {
    const naoAddress = serverAddress + "/nao/"

    const robot = {
        name: 'na',
        ipAddress: 'na',
        behaviors: [],
        actions: [],
        isConnected: true,
        volume: -1,
        speechVolume: -1,
        speechSpeed: -1,
        speechPitch: -1,
        speechLog: [],
        autoState: 'na',
        // InitializeRobot,
        SetProperty,
        DoMethod,
        RunAction
        // GetProperty,
    }

    setInterval(() => {
        if (pollEvents)
            DrainEvents().then((events) => FilterEvents(robot, events))
    }, 5000)


    const apiInterface = {
        robot,
        connectionStatus: "not connected",
    }

    InitializeRobot()

    // GetProperty('Volume')
    // DoMethod('Dance')
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

    function InitializeRobot() {
        const urlProp = naoAddress + 'property'
        MakeRequest(urlProp)
            .then((props) => {
                console.log('All properties received')
                //this apparently does not lead to losing references
                Object.assign(apiInterface.robot, props)
                apiInterface.connectionStatus = true
            })
        const urlAction = naoAddress + 'action'
        MakeRequest(urlAction)
            .then((actions) => {
                apiInterface.robot.actions = actions
            })
    }
    //not sure when this is ever used
    // function GetProperty(propName) {
    //     const url = naoAddress + "/property/" + propName
    //     MakeRequest(url)
    //         .then((prop) => console.log(prop))
    // }

    function SetProperty(propName, propValue) {
        const url = naoAddress + "property/" + propName
        MakeRequest(url, { 'value': propValue })
            .then((prop) => robot[propName] = prop['value'])
    }

    function DoMethod(methName, params) {
        const url = naoAddress + "method/" + methName
        MakeRequest(url, { 'params': params })
            .then((resBody) => console.log(resBody))
    }

    function RunAction(actionId) {
        const url = naoAddress + "action/" + actionId
        MakeRequest(url)
            .then((resBody) => console.log(resBody))
    }

    function DrainEvents() {
        const url = naoAddress + 'events'
        MakeRequest(url, { 'drain': true })
            .then((resBody) => console.log(resBody))
    }

    return apiInterface
}
