const firebase = require('../services/firebase')
const cors = require('./cors')

// const database = firebase.GetDatabase()
// const database = exports.GetDatabase()

/*This module expects the following request structure:
SET:
    key = req.body.key
    value = req.body.value
GET:
    key = req.body.key
    value = res.body


*/
function ReferenceFromRequest(key) {
    const database = firebase.GetDatabase()
    // const database = admin.database()
    return database.ref(key)
}

//returns promise
exports.SetInternal = function (key, value) {
    const ref = ReferenceFromRequest(key)
    return ref.set(value)
}

//returns promise
exports.GetInternal = function (key) {
    const ref = ReferenceFromRequest(key)
    return new Promise((resolve, reject) => {
        ref.once('value')
            .then(snapshot => resolve(snapshot.val()))
            .catch((err) => {
                console.error(err);
                reject(err)
            })
    })
}

exports.Set = function (req, res) {
    cors.PreflightResponse(req, res)
    // console.log('setting..');
    const ref = ReferenceFromRequest(req.body.key)
    // console.log(ref);
    const value = req.body.value;
    ref.set(value)
        .then((msg) => res.send(msg))
        .catch((err) => {
            res.status(500).send(err)
            console.error(err);
        });
}

exports.Get = function (req, res) {
    cors.PreflightResponse(req, res)
    // console.log('getting..');
    const ref = ReferenceFromRequest(req.body.key)
    exports.GetInternal(req.body.key)
        .then(val => res.send(val))
        .catch(res.status(500).send(err))
}


if (require.main === module) {

    exports.Set(
        {
            body: {
                key: "users/t-rex/banana",
                value: {
                    moreInfo: 39
                }
            }
        },
        {
            set: (val) => console.log(val),
            send: (val) => {
                console.log(val)
            }
        }
    )
    exports.Get(
        {
            body: {
                key: "users/t-rex"
            }
        }
        , {
            set: (val) => console.log(val),
            send: (val) => console.log(val)
        }
    )
}