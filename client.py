import socketio

sio = socketio.Client()


@sio.event
def connect():
    print('connection established')


@sio.event
def disconnect():
    print('disconnected from server')


@sio.on('pong')
def on_pong():
    print('pong received by server')


sio.connect('http://localhost:5000')
# sio.wait()

command = ''
while command != 'exit':
    command = input("Input a command: ")
    if command == 'ping':
        sio.emit('ping', {'payload': 'thepayload'})

sio.disconnect()
