
export default (devMode = true) => {
    if ((!'webkitSpeechRecognition' in window)) {
        console.log('web speech not supported')
        return
    }

    const recognition = new webkitSpeechRecognition()
    recognition.continuous = true
    recognition.interimResults = false
    recognition.lang = 'en-AU'

    const wsInterface = {
        hasStarted: false,
        hasAudioStarted: false,
        hasSpeechStarted: false,
        hasSoundStarted: false,
        autoRestart: true,
        setContinuous(val) { recognition.continuous = val },
        setInterim(val) { recognition.interimResults = val },
        onResult(text) { console.log('recognition proxy __onResult__ not yet set') },
        speechLog: [],
        errorLog: [],
        currentSentence: '',
        lastSentence: '',
        phraseTimeout: 500,
        lastWordTimestamp: new Date()
    }
    wsInterface.start = () => {
        if (!wsInterface.hasStarted) {
            console.log('starting')
            recognition.start()
        }
    }
    wsInterface.stop = () => {
        if (wsInterface.hasStarted) {
            console.log('stopping')
            recognition.stop()
        }
    }

    recognition.start()

    attatchToggleEvent('onspeechstart', 'onspeechend', 'hasSpeechStarted')
    attatchToggleEvent('onaudiostart', 'onaudioend', 'hasAudioStarted')
    attatchToggleEvent('onsoundstart', 'onsoundend', 'hasSoundStarted')

    attatchToggleEvent('onstart', 'onend', 'hasStarted', undefined, () => {
        if (wsInterface.autoRestart) {
            console.log(wsInterface)
            recognition.start()
        }
    }
    )
    recognition.onerror = (err) => {
        if (err.error === "no-speech")

            console.log("error:" + err.error)
    }
    function attatchToggleEvent(onStartName, onEndName, propName, startCallback, endCallback) {
        recognition[onStartName] = () => {
            if (devMode)
                console.log('event ' + onStartName)
            wsInterface[propName] = true
            if (startCallback)
                startCallback()
        }
        recognition[onEndName] = () => {
            if (devMode)
                console.log('event ' + onEndName)
            if (endCallback)
                endCallback()
            wsInterface[propName] = false
        }
    }

    recognition.onresult = (event) => {
        wsInterface.currentSentence = ''
        wsInterface.lastWordTimestamp = new Date()
        for (let i = event.resultIndex; i < event.results.length; ++i) {
            if (event.results[i].isFinal) {
                const sentence = event.results[i][0].transcript
                wsInterface.lastSentence = sentence
                wsInterface.speechLog.push(wsInterface.lastSentence)
                wsInterface.currentSentence = ''
                console.log('phrase concluded')
                wsInterface.onResult(sentence)
            }
            else {
                wsInterface.currentSentence += event.results[i][0].transcript
            }
        }
    }


    // setInterval(() => {
    //     if (wsInterface.currentSentence == '')
    //         return
    //     const now = new Date()
    //     const delay = now - wsInterface.lastWordTimestamp

    //     if (delay > wsInterface.phraseTimeout) {
    //         console.log('Phrase Timed out' + delay)
    //         wsInterface.lastWordTimestamp = new Date()
    //         wsInterface.lastSentence = wsInterface.currentSentence
    //         wsInterface.speechLog.push(wsInterface.lastSentence)
    //         wsInterface.currentSentence = ''
    //     }
    // }, 50)
    return wsInterface
}

