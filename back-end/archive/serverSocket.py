# from flask import Flask, send_from_directory
# from flask_socketio import SocketIO

# import threading
# import sys
# import utility
# import signal
# from naoInterface import NaoInterface
# from eventListener import CreateEventListener
# import utility

# PORT = 5000
# nao = NaoInterface("__", "__")
# eventListener = None


# def signal_handler(signal, frame):
#     print('\nprogram terminated')
#     sys.exit(0)


# signal.signal(signal.SIGINT, signal_handler)

# app = Flask(__name__, static_url_path='')
# app.config['SECRET_KEY'] = 'mysecret'
# socketio = SocketIO(app)
# print socketio


# @socketio.on('connect')
# def handleConnect():
#     print 'socket connected'
#     socketio.emit("RobotSend", nao.properties)


# @socketio.on('disconnect')
# def handleDisconnect():
#     print 'socket disconnected'


# @socketio.on('message')
# def handleMessage(msg):
#     print 'socket message:', msg
#     # send(msg, broadcast=True)


# @socketio.on('RobotPropertyGet')
# def handleRobotPropertyGet(data):
#     propName = utility.parseUnicode(data['property'])
#     propVal = nao.GetProperty(propName)
#     returnData = {
#         'property': propName,
#         'value': propVal
#     }
#     # print 'sending data..', returnData


# @socketio.on('RobotPropertySet')
# def handleRobotPropertySet(data):
#     socketio.send("yodellaeeeyhhhoooo")
#     socketio.emit('RobotPropertySend', "returnData")
#     propName = utility.parseUnicode(data['property'])
#     propVal = utility.parseUnicode(data['value'])
#     nao.SetProperty(propName, propVal)
#     # SEND RESULT BACK
#     handleRobotPropertyGet(data)


# @socketio.on('RobotMethodDo')
# def handleRobotMethodDo(data):
#     methName = utility.parseUnicode(data['method'])
#     param1 = utility.parseUnicode(data['param1'])
#     nao.DoMethod(methName, param1)


# def emitEvent(eventName, eventValue):
#     data = {
#         'event': eventName,
#         'value': eventValue
#     }
#     print 'triggering event', data
#     socketio.emit("RobotEventTrigger", data)


# def ConnectRobot(ipAddress):
#     ipAddress = utility.parseUnicode(ipAddress)
#     print 'Robot connect attempt at', ipAddress, '..'
#     global nao
#     if nao.properties['isConnected'] == True:
#         nao.CloseSession()
#     nao = NaoInterface(ipAddress, emitEvent)

#     if nao.properties['isConnected'] == True:
#         print 'nao connection succeeded..'
#         #socketio.emit("RobotConnected", nao.properties)
#         global eventListener
#         eventListener = CreateEventListener(emitEvent)
#     else:
#         print 'nao connection failed..'


# def run():
#     print"Server running on port", PORT
#     socketio.run(app, port=PORT)


# if __name__ == '__main__':
#     if len(sys.argv) > 1:
#         ConnectRobot(sys.argv[1])
#     if len(sys.argv) > 2:
#         PORT = sys.argv[2]
#     runThread = threading.Thread(target=run)
#     runThread.daemon = True
#     runThread.start()
#     while True:
#         pass
