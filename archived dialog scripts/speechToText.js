log('initializing...')

const speechToText = {
    OnResult: (text) => 'Speech To Text On Result dependency not set'
}

const SpeechRecognition = webkitSpeechRecognition || SpeechRecognition
// const SpeechGrammarList = SpeechGrammarList || webkitSpeechGrammarList
// const SpeechRecognitionEvent = SpeechRecognitionEvent || webkitSpeechRecognitionEvent

const recogntion = new SpeechRecognition()
recogntion.lang = 'en-AU'
recogntion.interimResults = false
recogntion.continuous = true
recogntion.start()
recogntion.onresult = function (event) {
    log('new result')
    console.log('result!')
    const speech = event.results[event.results.length - 1][0]
    formattedTranscript = removeInitialWhiteSpace(speech.transcript)
    log(formattedTranscript)
    console.log("\nspeech:" + formattedTranscript + "\nconfidence: " + speech.confidence)
    speechToText.OnResult(formattedTranscript)
    // recogntion.start()
}
console.log(recogntion)

function log(msg) {
    const elt = document.createElement("div")
    elt.innerHTML = msg
    document.body.appendChild(elt)
}

bodyMessages()

function removeInitialWhiteSpace(s) {
    while (s.charAt(0) === ' ') {
        s = s.substr(1)
    }
    return s
}

function bodyMessages() {
    recogntion.onstart = () => log('recognition started')
    recogntion.onend = () => {
        log('recognition ended')
        recogntion.start()
    }
    recogntion.onspeechstart = () => log('speech started')
    recogntion.onspeechend = () => log('speech ended')
    recogntion.onaudiostart = () => log('audio started')
    recogntion.onaudioend = () => log('audio ended')
    recogntion.onsoundstart = () => log('sound started')
    recogntion.onsoundend = () => log('sound ended')
    recogntion.onerror = (err) => log("error:" + err.error)
}


function consoleMessages() {
    recogntion.onstart = () => console.log('recognition started')
    recogntion.onend = () => {
        console.log('recognition ended')
        recogntion.start()
    }
    recogntion.onspeechstart = () => console.log('speech started')
    recogntion.onspeechend = () => console.log('speech ended')
    recogntion.onaudiostart = () => console.log('audio started')
    recogntion.onaudioend = () => console.log('audio ended')
    recogntion.onsoundstart = () => console.log('sound started')
    recogntion.onsoundend = () => console.log('sound ended')
    recogntion.onerror = (err) => console.log("error:" + err.error)
}
