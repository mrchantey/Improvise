const express = require('express')
const app = express()
const port = 5000
const server = app.listen(port)

app.use(express.static('html'))

console.log('server running on port ' + port)