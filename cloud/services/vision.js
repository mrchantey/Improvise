const vision = require('@google-cloud/vision')
const gcp = require('./gcp')

const client = new vision.ImageAnnotatorClient({ keyFilename: gcp.keyFilename })


exports.GetClient = function () {
    return client;
}