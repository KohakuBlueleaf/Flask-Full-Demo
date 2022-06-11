# import eventlet
# eventlet.monckey_patch()
from pages import chat
from app_init import app, CORS_ORIGINS
from flask_socketio import SocketIO
from gevent import monkey
monkey.patch_all()


# create sio extension
sio = SocketIO(
    app,
    message_queue="redis://localhost:6666",
    cors_allowed_origins=CORS_ORIGINS
)

# only bind socket.io
chat.setup_ws(sio)
