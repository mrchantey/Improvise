const gcpDialogflow = require('./gcp_dialogflow');
const gcpSpeech = require('./gcp_speech');






function DetectIntent(queryText) {

    return new Promise((resolve, reject) => {
        gcpDialogflow.DetectIntent(queryText)
            .then(result => {
                if (result.action === 'weather.get') {

                } else {
                    const responseBody = {
                        type: 'phrase',
                        text: result.fulfillmentText
                    }
                    resolve(responseBody)
                }
            })
    });
}

exports.ConverseText = function (queryText) {
    return DetectIntent(queryText)
}

// exports.ConverseAudioBits = function(audioBits) {
//     audioBytes = audioBits.toString('base64')
//     return exports.ConverseAudioBytes(audioBytes)
// }


exports.ConverseAudioBytes = function (audioBytes) {
    return new Promise((resolve, reject) => {
        gcpSpeech.Recognize(audioBytes)
            .then(queryText => {
                if (queryText === '') {
                    console.log('no speech recognized');
                    const responseBody = {
                        type: 'error',
                        value: 'no speech recognized'
                    }
                    resolve(responseBody)
                } else {
                    console.log(`speech recognized: ${queryText}`);
                    DetectIntent(queryText)
                        .then(responseBody => {
                            resolve(responseBody)
                        })
                }
            })
    });
}
