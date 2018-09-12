const openWeather = require('../services/openWeather')
const news = require('../services/newsAPI')
const time = require('../services/time')
const cors = require('./cors')
const database = require('./database')
// const storeTextAudio = require('./store-text-audio')
// const textToSpeech = require('../services/text-to-speech')

const commandQueueKey = "robot/commandQueue"

exports.DialogflowWebhook = function (req, res) {
    cors.PreflightResponse(req, res)
    const queryResult = req.body.queryResult
    if (!queryResult) {
        res.status(400).send("No queryResult object in body.")
    } else {
        if (queryResult.action === 'log') {
            console.log(req.body);
            FulfillQuery(res, 'The request has been logged')
        }
        else if (queryResult.action === 'weather.get') {
            openWeather.RequestConversationalWeather()
                .then(phrase => FulfillQuery(res, phrase))
        }
        else if (queryResult.action === 'news.get') {
            news.requestNewsConversational()
                .then(phrase => FulfillQuery(res, phrase))
        }
        else if (queryResult.action === 'time.get') {
            time.RequestTimeConversational()
                .then(phrase => FulfillQuery(res, phrase))
        }
        else {
            res.status(400).send("Unknown query action: " + queryResult.action)
        }
    }
}


function FulfillQuery(res, phrase) {
    AppendFirebaseCommands(phrase)
    //SEND RESPONSE
    res.json({
        "fulfillmentText": phrase
    })
}

function AppendFirebaseCommands(phrase) {

    database.GetInternal(commandQueueKey)
        .then((commandQueue) => {
            if (commandQueue.constructor !== Array)
                commandQueue = []
            const command = {
                "commandName": 'say',
                phrase
            }
            commandQueue.push(command)
            database.SetInternal(commandQueueKey, commandQueue)
        })
    // console.log(`command queue type: ${typeof (commandQueue)}. Is Array: ${commandQueue.constructor === Array}`)
    // console.log(commandQueue)
}

if (require.main === module) {
    req = {
        body: {
            queryResult: {
                action: "weather.get"
            }
        }
    }
    res = {
        set: console.log,
        send: console.log,
        json: console.log
    }

    exports.DialogflowWebhook(req, res);

}





// function FulfillQueryAudioStorage(phrase) {
//     const firebaseStoragePath = 'robot/next-phrase.wav'
//     const databasePhraseQueue = [{
//         type: 'audio',
//         firebaseStoragePath
//     }]
//     storeTextAudio.StoreTextAudioInternal(phrase, firebaseStoragePath)
//         .then(val => {
//             console.log("audio stored: " + val)
//             database.SetInternal("robot/phraseQueue", databasePhraseQueue)
//         })
//         .catch(err => console.error(err))
// }

// function FulfillQueryAudioDatabase(phrase) {
//     textToSpeech.Synthesize(phrase)
//         .then(audioData => {
//             const data64 = audioData.toString('base64')

//             const databasePhraseQueue = [{
//                 type: 'audio-database',
//                 data: data64
//             }]

//         })

// }
