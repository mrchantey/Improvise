



const fs = require('fs');

// // Imports the Google Cloud client library
const textToSpeech = require('@google-cloud/text-to-speech');
const gcp = require('./gcp')
// // Creates a client
const client = new textToSpeech.TextToSpeechClient({ keyFilename: gcp.keyFilename });

exports.Synthesize = function (text, filePath) {
    const request = {
        input: { text: text },
        //-20,20 semitones
        pitch: 0,
        // 0.25,4 x
        speaking_rate: 0,
        //gender ['MALE','FEMALE','NEUTRAL']
        voice: { languageCode: gcp.languageCode, ssmlGender: 'NEUTRAL' },
        // Select the type of audio encoding
        audioConfig: { audioEncoding: 'MP3' },
    };

    client.synthesizeSpeech(request, (err, response) => {
        if (err) {
            console.error('ERROR:', err);
            return;
        }
        // Write the binary audio content to a local file
        fs.writeFile(filePath, response.audioContent, 'binary', err => {
            if (err) {
                console.error('ERROR:', err);
                return;
            }
        });
    })
}


if (require.main == module) {
    // const text = 'Hello, world!';
    const text = 'WINONA Ryder has revealed how she and Keanu Reeves ‘actually got married’ 25 years ago while making one of Hollywood’s biggest horror film'
    exports.Synthesize(text, 'testSpeech.mp3')
}