import { stat } from "fs";
import FilterEvents from "./EventFilter";
import MakeApiRequest from "./apiRequest";

export default (serverAddress, dev) => {
    const naoAddress = serverAddress + "/modules/nao"

    const MakeRequest = MakeApiRequest


    const robot = {
        properties: {},
        actions: [],
        speechLog: [],
        // InitializeRobot,
        SetProperty,
        DoMethod,
        RunAction,
        eventListeningEnabled: false,
        eventIntervalId: undefined
        // FetchEvents
        // // GetProperty,
    }


    robot.SetEventListening = (val) => {
        function FetchEvents(drain) {
            return new Promise((resolve, reject) => {
                MakeRequest(naoAddress, { 'module': 'events', 'drain': drain })
                    .then((resBody) => resolve(resBody['events']))
            })
        }
        if (val == true) {
            robot.eventListeningEnabled = true
            robot.eventIntervalId = setInterval(() => {
                FetchEvents(true).then((events) => FilterEvents(robot, events))
            }, 5000)
        } else if (robot.eventIntervalId != undefined) {
            robot.eventListeningEnabled = false
            clearInterval(robot.eventIntervalId)
        }
    }
    // robot.SetEventListening(true)

    const naoInterface = {
        robot,
        connectionStatus: "not connected",
    }

    InitializeRobot()

    function InitializeRobot() {

        //BEGIN TOMORROW DO ALL LIKE THIS ONE SMILEY FACE :)
        const allPropsParams = { "module": "properties" }

        MakeRequest(naoAddress, allPropsParams)
            .then((res) => {
                if (res === "nao request not set")
                    return
                console.log('All properties received')
                //this apparently does not lead to losing references
                // Object.assign(naoInterface.robot, props)
                naoInterface.robot.properties = res
                naoInterface.connectionStatus = 'connected'
            })
        const allActionsParams = { "module": "actions" }
        MakeRequest(naoAddress, allActionsParams)
            .then((actions) => {
                if (actions === "nao request not set")
                    return
                console.log('All actions received')
                naoInterface.robot.actions = actions
            })
    }
    //not sure when this is ever used
    // function GetProperty(propName) {
    //     const url = naoAddress + "/property/" + propName
    //     MakeRequest(url)
    //         .then((prop) => console.log(prop))
    // }

    function SetProperty(propertyName, propertyValue) {
        const params = {
            module: 'properties',
            propertyName,
            propertyValue
        }
        MakeRequest(naoAddress, params)
            .then((prop) => robot.properties[propertyName] = prop['value'])
    }

    function DoMethod(methodName, params) {
        const fullParams = Object.assign({
            module: "methods",
            methodName
        }, params)
        MakeRequest(naoAddress, fullParams)
            .then((resBody) => console.log(resBody))
    }

    function RunAction(id) {
        const params = {
            module: 'actions',
            id
        }
        MakeRequest(naoAddress, params)
            .then((resBody) => console.log(resBody))
    }

    return naoInterface
}
