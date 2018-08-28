const admin = require('firebase-admin')
const serviceAccount = require('./keys/improvise-project-owner.json')

// const uniqueDate = new Date()
if (admin.apps.length == 0) {
    admin.initializeApp({
        credential: admin.credential.cert(serviceAccount),
        databaseURL: 'https://improvise-communicate.firebaseio.com',
        storageBucket: 'improvise-communicate.appspot.com'
        // }, uniqueDate.toString())
    })
    console.log("DEFAULT FIREBASE APP INITIALIZED: \t" + new Date())
}

const database = admin.database()
// const storage =


exports.GetDatabase = function () {
    return database
}

exports.storageBucket = admin.storage().bucket()

// exports.getServiceAccount = function () {
//     return serviceAccount
// }

// admin.initializeApp(functions.config().firebase)
if (require.main === module) {



}
