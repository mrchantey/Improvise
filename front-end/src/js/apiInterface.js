import { stat } from "fs";
import FilterEvents from "./EventFilter";
import MakeRequest from "./apiRequest";

window.pollEvents = false
// window.pollEvents = false

//TO RENAME AS NAOAPIINTERFACE

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


    function InitializeRobot() {
        const urlAllProperties = naoAddress + 'properties/all'
        MakeRequest(urlAllProperties)
            .then((res) => {
                if (res === "nao request not set")
                    return
                console.log('All properties received')
                //this apparently does not lead to losing references
                // Object.assign(apiInterface.robot, props)
                apiInterface.robot.properties = res.value
                apiInterface.connectionStatus = 'connected'
            })
        const urlAllActions = naoAddress + 'actions/all'
        MakeRequest(urlAllActions)
            .then((actions) => {
                if (actions === "nao request not set")
                    return
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
