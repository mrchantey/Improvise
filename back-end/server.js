const express = require('express')

const app = express()

const PORT = 3000

app.get('/', (req, res) => res.send('bang'))

app.listen(PORT, '0.0.0.0', () => console.log(`server listening on port ${PORT}`))