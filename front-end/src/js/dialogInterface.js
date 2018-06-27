import WebSpeechInterface from "./webSpeechInterface"
import MakeRequest from "./apiRequest"

export default (serverAddress) => {

    const wsInterface = WebSpeechInterface()

    const dialogUrl = serverAddress + "/modules/dialog"
    function SendDialog(queryText) {
        return new Promise((resolve, reject) => {
            // let parsedqueryText = queryText.replace(/ /g, '_')
            if (queryText.charAt(0) === " ")
                queryText = queryText.substring(1)
            const params = {
                queryText
            }
            MakeRequest(dialogUrl, params).then((response) => {
                console.log("Response received")
                console.log(response)
                resolve(response['responseText'])
            })
        })
    }


    wsInterface.onResult = SendDialog
    return wsInterface
}