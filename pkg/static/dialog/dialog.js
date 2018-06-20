
const url = "http://127.0.0.1:5000/dialog/"

speechToText.OnResult = DialogRequest

window.$MakeRequest = DialogRequest

function DialogRequest(phrase) {
    const parsedPhrase = phrase.replace(/ /g, '_')
    console.log('about to fetch..\n', url + parsedPhrase)
    fetch(url + parsedPhrase)
        .then((res) => {
            console.log('response:')
            res.json()
                .then((jsonRes) => console.log(jsonRes))
                .catch((err) => console.log(err))
        })
        .catch((err) => {
            console.log('error')
            console.log(err)
        })


}

