const database = require('./functions/database')
const naturalLanguage = require('./functions/naturalLanguage')
const vision = require('./functions/vision')
const dialogflowWebhook = require('./functions/dialogflowWebhook')
const storage = require('./functions/storage')
const storeTextAudio = require('./functions/store-text-audio')


exports.databaseget = database.Get
exports.databaseset = database.Set
exports.languagesentiment = naturalLanguage.DetectSentiment
exports.visionfaces = vision.DetectFaces
exports.dialogflowWebhook = dialogflowWebhook.DialogflowWebhook
exports.storageGet = storage.Get
exports.storageSet = storage.Set
exports.storeTextAudio = storeTextAudio.StoreTextAudio


exports.testget = function (req, res) {
    res.send(__dirname)
}

if (require.main === module) {
    exports.testget(0, { send: (val) => console.log(val) })
    // exports.databaseget()
}