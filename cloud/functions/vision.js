const vision = require('../services/vision')
const io = require('../utilities/io')
const fs = require('fs')
const client = vision.GetClient()
const cors = require('./cors')

// client.labelDetection('./resources/indian_street_photography_45.jpg')
//     .then((result) => {
//         const labels = result[0].labelAnnotations
//         labels.forEach(l => console.log(l))
//     }).catch((err) => {
//         console.log(err);
//     });

exports.DetectFaces = function (req, res) {
    cors.PreflightResponse(req, res)
    client.faceDetection({ image: req.body.image })
        .then((result) => {
            const faces = result[0].faceAnnotations
            // faces.forEach(f => console.log(f))
            res.send(faces)
            // res.send(result)
        }).catch((err) => {
            res.status(500).send(err)
            console.error(err);
        });
}

if (require.main === module) {
    const content = fs.readFileSync('selfie64.txt').toString()
    const req = {
        body: {
            image: {
                content
            }
        }
    }
    const res = {
        send: (res) => console.log(res),
        set: (val) => console.log(val)
    }
    exports.DetectFaces(req, res)
}


// const image64 = io.ReadFileTo64('resources/selfie.jpg')

// const image = { content: image64 }

