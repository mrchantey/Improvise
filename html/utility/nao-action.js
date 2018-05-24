

function LoadJSON(path, onLoadCallback) {
    const xhttp = new XMLHttpRequest();
    xhttp.overrideMimeType("application/json")
    xhttp.open('GET', path, true);
    xhttp.onreadystatechange = function () {
        if (xhttp.readyState == 4 && xhttp.status == "200") {
            const responseJson = JSON.parse(xhttp.responseText)
            onLoadCallback(responseJson)
        }
    }
    xhttp.send(null)
}

function CreateNaoAction(nao, actionInfo) {
    const action = {
        name: actionInfo.name,
        done: []
    }
    switch (actionInfo.type) {
        case 'audio':
            () => {

            }
            break;
        case 'behavior':

            break;
        case 'monologue':

            break;
    }

}