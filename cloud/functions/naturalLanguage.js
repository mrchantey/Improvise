const naturalLanguage = require('../services/naturalLanguage')
const cors = require('./cors')
const client = naturalLanguage.GetClient()

exports.DetectSentiment = function (req, res) {
    cors.PreflightResponse(req, res)
    // const text = 'Hello, world. I am so happy to be here. I am over the moon. This is the best day of my life!';
    // res.send('yea boii')
    const text = req.body.text
    const document = {
        content: text,
        type: 'PLAIN_TEXT',
    };
    client
        .analyzeSentiment({ document: document })
        .then(results => {
            const sentiment = results[0].documentSentiment;
            res.send(results)
            // res.send(sentiment)
            // console.log(`Text: ${text}`);
            // console.log(`Sentiment score: ${sentiment.score}`);
            // console.log(`Sentiment magnitude: ${sentiment.magnitude}`);
        })
        .catch((err) => {
            res.status(500).send(err)
            console.error(err);
        });
}