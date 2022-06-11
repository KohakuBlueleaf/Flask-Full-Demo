from flask import redirect, url_for, g
from flask_socketio import SocketIO
from app_init import app, CORS_ORIGINS
from pages import login, chat


# load blueprint
login.setup(app)
chat.setup(app)


@app.route('/')
def home():
    if g.user is None:
        return redirect(url_for('login.main'))
    else:
        return redirect(url_for('chat.main'))


# make a SIO extension for dev(no message queue)
sio_dev = SocketIO(
    app, logger=True
)
chat.setup_ws(sio_dev)


def main():
    # run Flask-SocketIO builtin server
    sio_dev.run(
        app,
        host='127.0.0.1', port=9999,
        use_reloader=True, debug=True
    )


if __name__ == '__main__':
    main()