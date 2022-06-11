from json import dumps

from flask import g, request
from flask_login import login_required

from app_init import AES_TEXT
from database.db import *
from pages import create_page_app

app, page_renderer = create_page_app('chat')


@app.route('', methods=['GET'])
@app.route('/', methods=['GET'])
@login_required
def main():
    '''Main render function for chat page'''
    return page_renderer(
        'chat.html',
        user=g.user.name,
        id=str(g.user.id)
    )


@app.route('/api/record', methods=['POST'])
@login_required
def get_mes_record():
    st = request.values['start_from']
    if st == '':
        messages = MessageDB.objects()
    else:
        messages = MessageDB.objects(id__lt=st)
    messages = messages.order_by('-id').limit(10)

    data = [
        {
            'id': str(message.id),
            'author': message.author.name,
            'time': message.time,
            'content': AES_TEXT.decrypt(message.content)
        } for message in messages
    ]

    return dumps(data)
