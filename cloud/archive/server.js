const express = require('express')

const app = express()

app.use(express.json())
// app.use(express.bodyParser())

app.use(function (req, res, next) {
    console.log(req.method);

    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    next();
});

app.get('/', (req, res) => {
    requestCallback(req.query)
        .then(responseBody => {
            // responseBody.query = req.query
            res.send(responseBody)
        })
})

app.post('/', (req, res) => {
    // console.log(req.body);
    requestCallback(req.body)
        .then(responseBody => {
            // responseBody.query = req.body
            res.send(responseBody)
        })
})

let requestCallback

const defaultRequestCallback = (val) => {
    console.warn("No Request Callback Set")
    return new Promise((resolve, reject) => {
        resolve({
            type: 'error',
            value: 'request callback not set'
        })
    });
};

exports.Run = function (_requestCallback = defaultRequestCallback, PORT = 3000) {
    requestCallback = _requestCallback
    app.listen(PORT, '0.0.0.0', () => console.log(`server listening on port ${PORT}`))
}



if (require.main === module) {
    exports.Run()
}