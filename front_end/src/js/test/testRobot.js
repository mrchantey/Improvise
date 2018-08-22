

import testBehaviors from "./testBehaviors"
import ActionParser from "../ActionParser"

export default () => {

    // fetch("testMusic.json")
    // .then(()=>console.log('success'))
    // .cacth(()=>console.log('no dice'))



    const actionParser = ActionParser()

    const robot = {
        name: "Test Robot",
        ipAddress: "69.69.69.69",
        sessionId: 9999,
        behaviors: testBehaviors
    }
    robot.actions = actionParser.parseBehaviors(robot.behaviors)
    return robot
}