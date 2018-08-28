const storage = require('./storage')
const textToSpeech = require('../services/text-to-speech')
const fs = require('fs')
const cors = require('./cors')


exports.StoreTextAudioInternal = function (text, destPath) {
    return new Promise((resolve, reject) => {
        textToSpeech.Synthesize(text)
            .then(audioData => {
                const tempPath = '/tmp/store_text_audio.raw'
                fs.writeFileSync(tempPath, audioData)
                return storage.SetInternal(tempPath, destPath)
                // console.log(audioData);
                // database.SetInternal(destPath,)
            })
            .then(storeResult => resolve(storeResult))
            .catch(err => reject(err));
    });
}

/*
STORE TEXT AUDIO
req.body.text = text
req.body.destinationPath = destPath
*/

exports.StoreTextAudio = function (req, res) {
    cors.PreflightResponse(req, res)
    exports.StoreTextAudioInternal(req.body.text, req.body.destinationPath)
        .then(result => res.send(result))
        .catch(err => {
            res.status(500).send(err)
            console.error(err);
        })
}


if (require.main === module) {
    exports.StoreTextAudioInternal('hey there rockstar', 'robots/next-phrase.wav')
        .then(val => {
            console.log(val[0].name)
            return storage.GetInternal(val[0].name)
        })
        .then(data => {
            fs.writeFileSync('tmp/downloaded.wav', data)
        })
        .catch(val => console.error(val))
}


// }