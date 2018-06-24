

export default (url, body = undefined) => {
    const request = (body == undefined) ? {} : {
        headers: {
            'content-type': "application/json"
        },
        method: 'POST',
        body: JSON.stringify(body)
    }
    const reqPrint = body == undefined ? '\nGET\n' : '\nPOST\n'
    console.log(reqPrint + url)
    return new Promise((resolve, reject) => {
        fetch(url, request)
            .then((response) => {
                // console.log(response)
                if (response.status == 200) {
                    const contentType = response.headers.get('content-type')
                    if (contentType == 'application/json') {
                        response.json().then((jsonBody) => {
                            resolve(jsonBody)
                        })
                    } else {
                        resolve(response.body)
                    }
                }
                // } else if (response.status == 204)
                //     console.log(response.status.toString() + '\nserver: connected\nrobot: disconnected')
                else if (response.status >= 400)
                    console.log(response.status.toString() + '\noh moit just give up')
            })
            .catch((reason) => console.log(reason + "\nlikely server is unresponsive"))
    })
}