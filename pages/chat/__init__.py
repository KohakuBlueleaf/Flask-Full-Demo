from flask import Flask
from flask_socketio import SocketIO
from app_init import setup_cors
from .chat_server import app
from .chat_sio_server import client_msg, connected_msg


def setup(main_app: Flask):
    setup_cors(app)
    main_app.register_blueprint(app)


def setup_ws(sio: SocketIO):
    # since chat_sio_server.py import
    sio.on_event('client_event', client_msg, namespace='/chat')
    sio.on_event('connect_event', connected_msg, namespace='/chat')
