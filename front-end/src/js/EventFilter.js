export default (robot, drainedEvents) => {
    console.log('events occured:')
    drainedEvents.forEach(event => {
        console.log(event)
        processEvent(robot, event)
    })
}


function processEvent(robot, event) {
    switch (event.key) {
        case 'ALTextToSpeech/CurrentSentence':
            robot.speechLog.push(event.value)
    }




}