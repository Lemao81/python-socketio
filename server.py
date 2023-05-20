from eventlet import wsgi
import eventlet
import socketio

sio = socketio.Server()

static_files = {
    '/': 'index.html'
}

app = socketio.WSGIApp(sio, static_files=static_files)


@sio.on('*')
def catch_all_events(event, sid, data):
    print('Event triggered', event, sid, data, flush=True)


@sio.event
def connect(sid, environ, auth):
    print('connect ', sid, environ, auth, flush=True)


@sio.event
def disconnect(sid):
    print('disconnect ', sid, flush=True)


@sio.on('ping')
def on_ping(sid, data):
    print(f'Ping received by {sid}', data, flush=True)
    sio.emit('pong')


if __name__ == '__main__':
    wsgi.server(eventlet.listen(('', 5000)), app)
