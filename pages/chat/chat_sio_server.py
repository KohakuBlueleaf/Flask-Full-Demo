from flask import request, session
from flask_socketio import emit
from flask_login import current_user as c_user

from mongoengine.connection import get_connection, get_db

from app_init import AES_TEXT
from database.db import UserDB, MessageDB
from utils.clocks import utc_time
from utils import parse_object_id


cli = {}


def client_msg(msg):
    '''SIO handle client message'''
    print()
    print(request.sid)
    print(parse_object_id(c_user.id))
    print()

    if msg['data'].rstrip() == '':
        return
    message = msg['data'].rstrip()
    enc_mes = AES_TEXT.encrypt(message)
    mestime = utc_time()

    user = UserDB.objects(id=cli[request.sid]).first()
    new_msg = MessageDB(
        author=user,
        time=mestime,
        content=enc_mes
    )
    new_msg.save()

    emit(
        'new_message',
        {
            'author': user.name,
            'time': mestime,
            'content': message
        },
        broadcast=True
    )


def connected_msg(msg):
    '''handle client connect event'''
    print()
    print(msg, session, c_user.is_authenticated, c_user.is_anonymous)
    print()

    if not c_user.is_authenticated or c_user.is_anonymous:
        emit('reload_require', {})
        return

    cli[request.sid] = c_user.id

    emit(
        'sid_set',
        {'sid': request.sid}
    )
    emit(
        'server_response',
        {'data': 'connected'}
    )
