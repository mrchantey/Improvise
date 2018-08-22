
const fs = require('fs')
const speechToText = require('@google-cloud/speech')
const gcp = require('./gcp');

const client = new speechToText.SpeechClient({ keyFilename: gcp.keyFilename })




exports.Recognize = function (audioBytes) {
    const audio = {
        content: audioBytes
    }

    const config = {
        encoding: 'LINEAR16',
        sampleRateHertz: 16000,
        languageCode: gcp.languageCode
    }

    const request =
    {
        audio,
        config
    }

    return new Promise((resolve, reject) => {
        client
            .recognize(request)
            .then(data => {
                const response = data[0]
                const transcription = response.results
                    .map(r => r.alternatives[0].transcript)
                    .join('\n')
                // console.log(`Transcription: ${transcription}`)
                resolve(transcription)
            })
            .catch(err => console.error(`ERROR: ${err}`))
    });
}

if (require.main === module) {
    const fileName = './last_sentence.wav'

    const file = fs.readFileSync(fileName)
    const audioBytes = file.toString('base64')
    // fs.writeFileSync('audioBytes.txt', audioBytes)
    exports.Recognize(audioBytes)
        .then(response => console.log(response))
}