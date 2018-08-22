const dialogService = require('./services/dialog_service');
const server = require('./server')



function OnRequest(requestBody) {
    // console.log(
    //     `Request Made: ${requestBody}`
    // );
    if (requestBody.audioBytes)
        return dialogService.ConverseAudioBytes(requestBody.audioBytes)
    if (requestBody.audioBits)
        return dialogService.ConverseAudioBits(requestBody.audioBits)
    else if (requestBody.queryText)
        return dialogService.ConverseText(requestBody.queryText)

    return new Promise((resolve, reject) => {
        resolve(
            {
                type: 'error',
                value: 'no available response'
            }
        )
    });
}




if (require.main === module) {
    server.Run(OnRequest)
}


