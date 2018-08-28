const fs = require('fs');
const textToSpeech = require('@google-cloud/text-to-speech');
const gcp = require('./gcp')
const client = new textToSpeech.TextToSpeechClient({ keyFilename: gcp.keyFilename });

exports.Synthesize = function (text) {
    const request = {
        input: { text: text },
        //-20,20 semitones
        pitch: 0,
        // 0.25,4 x
        speaking_rate: 0,
        //gender ['MALE','FEMALE','NEUTRAL']
        // voice: { languageCode: gcp.languageCode, ssmlGender: 'MALE' },
        voice: { languageCode: gcp.languageCode, name: "en-AU-Wavenet-A" },
        // Select the type of audio encoding[ LINEAR16 , MP3 , OGG_OPUS ]
        // audioConfig: { audioEncoding: 'MP3' }, 
        // audioConfig: { audioEncoding: 'OGG_OPUS' },//NAO cannot play ogg files
        // audioConfig: { audioEncoding: 'MP3' },
        audioConfig: { audioEncoding: 'LINEAR16' },
    };
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
    const text = 'lets party'
    const filePath = 'tmp/testSpeech.wav'
    exports.Synthesize(text)
        .then(audioContent => {
            // Write the binary audio content to a local file
            fs.writeFile(filePath, audioContent, 'binary', err => {
                if (err) {
                    console.error('ERROR:', err);
                    return;
                }
            });
        })
}