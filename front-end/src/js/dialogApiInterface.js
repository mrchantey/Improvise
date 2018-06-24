import WebSpeechInterface from "./webSpeechInterface"
import MakeRequest from "./apiRequest"

export default (serverAddress) => {

    const wsInterface = WebSpeechInterface()

    const dialogUrl = serverAddress + "/dialog/"
    function SendDialog(text) {
        let parsedText = text.replace(/ /g, '_')
        if (parsedText.charAt(0) === "_")
            parsedText = parsedText.substring(1)
        const url = dialogUrl + parsedText
        MakeRequest(url).then((response) => {
            console.log("Response received")
            console.log(response)
        })
    }


    wsInterface.onResult = SendDialog
    return wsInterface
}