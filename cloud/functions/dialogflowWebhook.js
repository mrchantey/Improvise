const openWeather = require('../services/openWeather')
const news = require('../services/newsAPI')
const time = require('../services/time')
const cors = require('./cors')

function sendResponsePhrase(res, phrase) {
    const body = {
        "fulfillmentText": phrase
    }
    res.json(body)
}

exports.DialogflowWebhook = function (req, res) {
    cors.PreflightResponse(req, res)
    const queryResult = req.body.queryResult
    if (!queryResult) {
        res.status(400).send("No queryResult object in body.")
    } else {
        if (queryResult.action === 'log') {
            console.log(req.body);
            sendResponsePhrase(res, 'The request has been logged')
        }
        else if (queryResult.action === 'weather.get') {
            openWeather.RequestConversationalWeather()
                .then(phrase => sendResponsePhrase(res, phrase))
        }
        else if (queryResult.action === 'news.get') {
            news.requestNewsConversational()
                .then(phrase => sendResponsePhrase(res, phrase))
        }
        else if (queryResult.action === 'time.get') {
            time.RequestTimeConversational()
                .then(phrase => sendResponsePhrase(res, phrase))
        }
        else {
            res.status(400).send("Unknown query action: " + queryResult.action)
        }
    }
}