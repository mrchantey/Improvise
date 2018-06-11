


export default () => {

    return {
        parseBehaviors(behaviorPaths) {
            behaviorPaths.sort()

            const actions = []
            for (let i = 0; i < behaviorPaths.length; i++) {
                const splitPath = behaviorPaths[i].split('/')
                const action = {
                    name: splitPath[splitPath.length - 1],
                    type: "Behavior",
                    tags: GetBehaviorTags(splitPath)
                }
                actions.push(action)
            }

            function GetBehaviorTags(splitPath) {
                if (splitPath.some(s =>
                    s.includes('animations') ||
                    s.includes('dialog'))) {
                    splitPath.pop()
                    return splitPath
                }
                // console.log(splitPath.splice(-1,1))
                else
                    return []
            }

            return actions
        }

    }

}