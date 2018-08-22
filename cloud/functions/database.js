const firebase = require('../services/firebase')
const cors = require('./cors')

// const database = firebase.GetDatabase()
// const database = exports.GetDatabase()

function ReferenceFromRequest(req) {
    const database = firebase.GetDatabase()
    // const database = admin.database()
    return database.ref(req.body.key)
}

exports.Set = function (req, res) {
    cors.PreflightResponse(req, res)
    // console.log('setting..');
    const ref = ReferenceFromRequest(req)
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
    const ref = ReferenceFromRequest(req)
    ref.once('value')
        .then(snapshot => res.send(snapshot.val()))
        .catch((err) => {
            res.status(500).send(err)
            console.error(err);
        });
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