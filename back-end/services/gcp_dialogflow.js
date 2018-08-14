const fs = require('fs');
const dialogflow = require('dialogflow');
const gcp = require('./gcp')

const projectID = 'improvise-communicate'


const sessionID = 'my-session'

const client = new dialogflow.SessionsClient({ keyFilename: gcp.keyFilename })

const sessionPath = client.sessionPath(projectID, sessionID)



exports.DetectIntent = function (queryText) {
    const queryInput = {
        text: {
            text: queryText,
            languageCode: gcp.languageCode
        }
    }

    const request = {
        session: sessionPath,
        queryInput
    }

    const promise = new Promise((resolve, reject) => {
        client
            .detectIntent(request)
            .then(responses => {
                const response = responses[0]
                resolve(response.queryResult)
                // const fulfillmentText = response.queryResult.fulfillmentText
                // resolve(fulfillmentText)
            })
            .catch(err => {
                console.error(`ERROR: ${err}`)
                //reject(err)
            })
    })
    return promise
}

if (require.main === module) {
    const queryText = 'hows the weather today?'
    exports
        .DetectIntent(queryText)
        .then(result => console.log(result))
}

/*
{ fulfillmentMessages:
    [ { platform: 'PLATFORM_UNSPECIFIED',
        text: [Object],
        message: 'text' } ],
   outputContexts: [],
   queryText: 'hows the weather today?',
   speechRecognitionConfidence: 0,
   action: 'weather.get',
   parameters: { fields: { date: [Object], 'weather-condition': [Object] } },
   allRequiredParamsPresent: true,
   fulfillmentText: 'use parameters to fetch the weather',
   webhookSource: '',
   webhookPayload: null,
   intent:
    { inputContextNames: [],
      events: [],
      trainingPhrases: [],
      outputContexts: [],
      parameters: [],
      messages: [],
      defaultResponsePlatforms: [],
      followupIntentInfo: [],
      name: 'projects/improvise-communicate/agent/intents/d711c856-e609-4143-90eb-61c108361dab',
      displayName: 'weather.get',
      priority: 0,
      isFallback: false,
      webhookState: 'WEBHOOK_STATE_UNSPECIFIED',
      action: '',
      resetContexts: false,
      rootFollowupIntentName: '',
      parentFollowupIntentName: '',
      mlDisabled: false },
   intentDetectionConfidence: 0.9100000262260437,
   diagnosticInfo: null,
   languageCode: 'en-au' }

   */