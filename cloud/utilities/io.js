const fs = require('fs')


exports.ReadFileTo64 = function (path) {
    const file = fs.readFileSync(path)
    return new Buffer(file).toString('base64')
}

if (require.main === module) {
    const encoded = exports.ReadFileTo64('resources/selfie.jpg')
    console.log(encoded.length);
}
