const fs = require('fs');
const textToSpeech = require('@google-cloud/text-to-speech');
const gcp = require('./gcp')
const client = new textToSpeech.TextToSpeechClient({ keyFilename: gcp.keyFilename });

exports.Synthesize = function (text, requestParams = {}) {
    const request = {
        input: { text: text },
        voice: { languageCode: gcp.languageCode, name: "en-AU-Wavenet-A" },
        // Select the type of audio encoding[ LINEAR16 , MP3 , OGG_OPUS ]
        // audioConfig: { audioEncoding: 'MP3' }, 
        // audioConfig: { audioEncoding: 'OGG_OPUS' },//NAO cannot play ogg files
        // audioConfig: { audioEncoding: 'MP3' },
        audioConfig: {
            audioEncoding: 'LINEAR16',
            //-20,20 semitones
            pitch: 0,
            // 0.25,4 x
            speaking_rate: 0
            //gender ['MALE','FEMALE','NEUTRAL']
            // voice: { languageCode: gcp.languageCode, ssmlGender: 'MALE' },    
        },
    };
    if (requestParams.audioConfig)
        Object.assign(request.audioConfig, requestParams.audioConfig)
    // const request = Object.assign(requestDefault, requestParams)
    return new Promise((resolve, reject) => {
        client.synthesizeSpeech(request, (err, response) => {
            if (err) {
                console.error('ERROR:', err);
                reject(err);
                return;
            } else {
                //returns binary data
                resolve(response.audioContent)
            }
        });
    })
}


if (require.main == module) {
    const text = 'wow, what a terrific audience'

    for (let i = 0; i <= 10; i += 1) {
        const filePath = `tmp/testSpeech_${i}.wav`
        const requestParams = {
            audioConfig: {
                pitch: i
            }
        }
        exports.Synthesize(text, requestParams)
            .then(audioContent => {
                // Write the binary audio content to a local file
                fs.writeFile(filePath, audioContent, 'binary', err => {
                    if (err) {
                        console.error('ERROR:', err);
                        return;
                    }
                });
            })
            .catch(err => console.error(err))
    }
}