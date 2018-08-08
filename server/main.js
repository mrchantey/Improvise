const server = require('./server.js')
const messages = require('./messages.js')

server.SetMessageHandler(messages.HandleMessage)
server.Run()



