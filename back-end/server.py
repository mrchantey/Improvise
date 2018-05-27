from flask import Flask, send_from_directory
from flask_socketio import SocketIO, send
import threading
import sys
import signal
import nao


def signal_handler(signal, frame):
    print('\nprogram terminated')
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


app = Flask(__name__, static_url_path='')
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)


@socketio.on('connect')
def handleConnect():
    print('new connection')


@socketio.on('disconnect')
def handleDisconnect():
    print('disconnected')


@socketio.on('message')
def handleMessage(msg):
    print('message from client: ' + msg)
    send(msg, broadcast=True)


def run():
    print("Server running on port 5000")
    socketio.run(app)


nao.test()

# if __name__ == '__main__':
#   run()
# runThread = threading.Thread(target=run)
# runThread.daemon = True
# runThread.start()
# while True:
#     pass
