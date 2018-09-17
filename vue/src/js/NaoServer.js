


export default {
    ServerRequest,
}

function ServerRequest(body) {

    // const url = "http://192.168.0.121:5000/command"
    // const url = "http://127.0.0.1:5000/ping"
    const url = "http://127.0.0.1:5000/command"

    const request = {
        headers: {
            'Content-Type': "application/json"
        },
        method: 'POST',
        body: JSON.stringify(body)
    }
    console.log("request made:");
    console.log(request);

    return new Promise((resolve, reject) => {
        fetch(url, request)
            .then((response) => {
                console.log("response received: ", response, response.body);
                if (response.status == 200) {
                    const contentType = response.headers.get('content-type');
                    if (contentType == 'application/json') {
                        response
                            .json()
                            .then(jsonBody => resolve(jsonBody))
                    } else {
                        resolve(response.body)
                    }
                } else {
                    console.error("server request error:", response);
                }
            })
            .catch(err => console.error("server connection error:", err))
    });
}