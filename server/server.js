const express = require("express")
const app = express()
const PORT = "3000"

app.use(express.json())

let onMessage = (message) => {
    console.warn("message handler unassigned")
}

app.use(function (req, res, next) {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    next();
});

app.get('/', (req, res) => {
    res.send({ message: "howdy cowgirl" })
})

app.post('/message', (req, res) => {
    const body = req.body
    responseBody = onMessage(body)
    res.send(responseBody)
})

module.exports = {
    Run: () => {
        app.listen(PORT, '0.0.0.0', () => console.log(`app listening on port ${PORT}`))
    },
    SetMessageHandler(handler) {
        onMessage = handler
    }


}

