
function SortBehaviors(behaviorPaths) {

    behaviorPaths.sort()
    // console.log(behaviorPaths)

    const behaviors = {}
    behaviors.All = GetAllBehaviors()
    // behaviors.Animations = FilterBehaviorsByPath(behaviors.All, "animations/Stand")
    behaviors.IdleAnimations = FilterBehaviorsByPath(behaviors.All, "animations/Stand/Waiting")
    return behaviors

    function GetAllBehaviors() {
        const splitPaths = behaviorPaths.map(b => b.split('/'))

        const rootContents = { name: "Installed Behaviors", contents: [] }
        splitPaths.forEach(sp => {
            let parentDir = rootContents
            for (let i = 0; i < sp.length; i++) {
                let thisDir = parentDir.contents.filter(dir => dir.name === sp[i])[0]
                if (thisDir === undefined) {
                    thisDir = { name: sp[i], contents: [], path: CreatePath(sp, i) }
                    parentDir.contents.push(thisDir)
                }
                parentDir = thisDir
            }
        })

        // SortAlphabetical(rootContents)

        return rootContents
    }

    function SortAlphabetical(behavior) {

        behavior.contents.sort(compare)
        behavior.contents.forEach(b => SortAlphabetical(b))

        function compare(a, b) {
            // Use toUpperCase() to ignore character casing
            const nameA = a.name.toUpperCase();
            const nameB = b.name.toUpperCase();

            let comparison = 0;
            if (nameA > nameB) {
                comparison = 1;
            } else if (nameA < nameB) {
                comparison = -1;
            }
            return comparison;
        }


    }


    function CreatePath(splitPath, maxIndex) {
        let path = ''
        for (let i = 0; i <= maxIndex; i++) {
            if (i !== 0) path += '/'
            path += splitPath[i]
        }
        return path
    }

    function FilterBehaviorsByPath(behaviors, path) {
        const arr = [];
        RecursiveFlattenBehaviors(arr, behaviors)

        const filtered = arr.filter(b => b.path.includes(path))

        return filtered;

        function RecursiveFlattenBehaviors(arr, behavior) {
            behavior.contents.forEach(b => {
                arr.push(b)
                RecursiveFlattenBehaviors(arr, b)
            })
        }
    }


    //   console.log(rootContents)
}




