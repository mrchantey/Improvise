import { stat } from "fs";
import FilterEvents from "./EventFilter";

window.pollEvents = false
// window.pollEvents = false


export default (serverAddress, dev) => {
    const naoAddress = serverAddress + "/nao/"

    const robot = {
        properties: {},
        speechLog: [],
        // InitializeRobot,
        SetProperty,
        DoMethod,
        RunAction,
        FetchEvents
        // GetProperty,
    }

    setInterval(() => {
        if (pollEvents)
            FetchEvents(true).then((events) => FilterEvents(robot, events))
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
        const urlAllProperties = naoAddress + 'properties/all'
        MakeRequest(urlAllProperties)
            .then((res) => {
                console.log('All properties received')
                //this apparently does not lead to losing references
                // Object.assign(apiInterface.robot, props)
                apiInterface.robot.properties = res.value
                apiInterface.connectionStatus = 'connected'
            })
        const urlAllActions = naoAddress + 'actions/all'
        MakeRequest(urlAllActions)
            .then((actions) => {
                console.log('All actions received')
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
        const url = naoAddress + "properties/" + propName
        MakeRequest(url, { 'params': { 'value': propValue } })
            .then((prop) => robot.properties[propName] = prop['value'])
    }

    function DoMethod(methName, params) {
        const url = naoAddress + "methods/" + methName
        MakeRequest(url, { 'params': params })
            .then((resBody) => console.log(resBody))
    }

    function RunAction(actionId) {
        const url = naoAddress + "actions/" + actionId
        MakeRequest(url)
            .then((resBody) => console.log(resBody))
    }

    function FetchEvents(drain) {
        return new Promise((resolve, reject) => {
            const url = naoAddress + 'events/fetch'
            MakeRequest(url, { 'params': { 'drain': drain } })
                .then((resBody) => resolve(resBody['events']))
        })
    }

    return apiInterface
}
