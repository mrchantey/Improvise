const firebase = require('../services/firebase')
const fs = require('fs')
const cors = require('./cors')

exports.SetInternal = function (srcPath, destPath) {
    // destPath = destPath == undefined ? srcPath : destPath
    return firebase.storageBucket
        .upload(srcPath, { destination: destPath })
}


exports.GetInternal = function (path) {
    return new Promise((resolve, reject) => {
        firebase.storageBucket
            .file(path)
            .download()
            .then(data => resolve(data[0]))
            .catch(err => reject(err))
    });
}

/*
SET:
data = req.body.data
destPath = req.body.destinationPath
*/

exports.Set = function (req, res) {
    cors.PreflightResponse(req, res)
    const tempPath = '/tmp/storage_set.raw'
    const buffData = new Buffer(req.body.data, 'base64')
    fs.writeFileSync(tempPath, buffData)
    exports.SetInternal(tempPath, req.body.destinationPath)
        .then(result => {
            res.send(result)
        })
        .catch(err => {
            res.status(500).send(err)
            console.error(err);
        })
}

/*
srcPath = req.body.sourcePath
*/

exports.Get = function (req, res) {
    cors.PreflightResponse(req, res)
    exports.GetInternal(req.body.sourcePath)
        .then(data => {
            const dataBase64 = data.toString('base64')
            console.log(data);
            console.log(dataBase64);
            res.send(dataBase64)
        })
        .catch(err => {
            res.status(500).send(err)
            console.error(err);
        })
}


if (require.main === module) {
    // exports.SetInternal('testSpeech.ogg', "speeches/testSpeech.ogg")
    exports.GetInternal('robots/next-phrase')
        .then(data => {
            const dataBase64 = data.toString('base64')
            console.log(data);
            console.log('NOW FORE THE 64 --------------------------');
            console.log(dataBase64);
            // fs.writeFileSync('tmp/downloaded2.ogg', data)
        })
        .catch(err => console.error(err))
}