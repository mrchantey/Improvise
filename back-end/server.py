from flask import Flask, send_from_directory
from flask_socketio import SocketIO
import threading
import sys
import signal
import naoInterface
import utility


def signal_handler(signal, frame):
    print('\nprogram terminated')
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


app = Flask(__name__, static_url_path='')
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)

socketEvents = []


@socketio.on('connect')
def handleConnect():
    print 'socket connected'
    socketEvents.append(('connect', 'connection info here'))


@socketio.on('disconnect')
def handleDisconnect():
    print 'socket disconnected'
    socketEvents.append(('disconnect', 'disconnection info here'))


@socketio.on('message')
def handleMessage(msg):
    print 'socket message:', msg
    socketEvents.append(('message', msg))
    # send(msg, broadcast=True)


@socketio.on('ConnectRobot')
def handleRobotConnect(uniIpAddress):
    ipAddress = utility.unicodeToAscii(uniIpAddress)
    print 'socket robot connect attempt at', ipAddress, '..'
    print type(ipAddress)
    sessionId = naoInterface.beginSession(ipAddress)
    print 'session id:', sessionId
    if(sessionId == -1):
        socketio.emit('ConnectRobotReject')
    else:
        socketio.emit('ConnectRobotResolve', sessionId)


@socketio.on('GetRobotBehaviors')
def handleGetRobotStatus(sessionId):
    #    sessionId = obj['sessionId']
    print 'retreiving robot behaviors'
    behaviors = naoInterface.getInstalledBehaviors(sessionId)
    socketio.emit('SetRobotBehaviors', behaviors)


@socketio.on('GetRobotName')
def handleGetRobotName(sessionId):
    name = naoInterface.getName(sessionId)
    socketio.emit('SetRobotName', name)


def run():
    print("Server running on port 5000")
    socketio.run(app)


if __name__ == '__main__':
    # run()
    runThread = threading.Thread(target=run)
    runThread.daemon = True
    runThread.start()
    while True:
        pass
