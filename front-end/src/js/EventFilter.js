export default (robot, drainedEvents) => {
    // console.log('events occured:')
    drainedEvents.forEach(event => {
        // console.log(event)
        processEvent(robot, event)
    })
}


function processEvent(robot, event) {
    switch (event.key) {
        case 'ALTextToSpeech/CurrentSentence':
            const cleanText = cleanUpSpeech(event.value)
            if (cleanText != '')
                robot.speechLog.push(cleanText)
    }
}


function cleanUpSpeech(speech) {
    const splitSpeech = speech.split('\\')
    let newSpeech = ''
    for (let i = 0; i < splitSpeech.length; i += 2) {
        newSpeech += splitSpeech[i]
    }
    return newSpeech
}