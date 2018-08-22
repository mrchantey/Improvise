const language = require('@google-cloud/language')
const gcp = require('./gcp')

const client = new language.LanguageServiceClient({ keyFilename: gcp.keyFilename })

exports.GetClient = function () {
    return client
}



// // Detects the sentiment of the text