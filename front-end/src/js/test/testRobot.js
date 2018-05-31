

import testBehaviors from "./testBehaviors"
import parseActions from "../parseRobotActions"

export default () => {

    const robot = {
        name: "Test Robot",
        ipAddress: "69.69.69.69",
        sessionId: 9999,
        behaviors: testBehaviors
    }
    robot.actions = parseActions(robot.behaviors)
    return robot
}