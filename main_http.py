from flask import redirect, url_for, g

from app_init import app
from pages import login, chat


# only bind http route
login.setup(app)
chat.setup(app)


@app.route('/')
def home():
    if g.user is None:
        return redirect(url_for('login.main'))
    else:
        return redirect(url_for('chat.main'))


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
