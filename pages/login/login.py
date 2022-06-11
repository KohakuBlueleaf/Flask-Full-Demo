from flask import (
    redirect, url_for,
    request, session, g
)
from flask_login import (
    login_user, logout_user, current_user as c_user
)

from pages import create_page_app
from middleware import User
from database.db import UserDB
from utils.crypto import sha

c_user:User
app, page_renderer = create_page_app('login')


@app.route('', methods=['GET'])
@app.route('/', methods=['GET'])
def main():
    return page_renderer(
        'login.html',
        login_fail=session.pop('login_fail', False),
        ac_not_found=session.pop('ac_not_found', False)
    )


@app.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('login.main'))


def login(user):
    new_user = User()
    new_user.id = user.id
    login_user(new_user)


@app.route('/auth', methods=['POST'])
def auth():
    session.pop('login_fail', None)
    session.pop('ac_not_found', None)

    account = request.values['ac']
    pswd = sha(request.values['pswd']).hex()

    if UserDB.objects(name=account).first():
        if user := UserDB.objects(name=account, pswd=pswd).first():
            login(user)
            return redirect(url_for('chat.main'))
        else:
            session['login_fail'] = True
            return redirect(url_for('login.main'))

    else:
        session['ac_not_found'] = True
        return redirect(url_for('login.main'))


@app.route('/register', methods=['GET'])
def reg():
    return page_renderer(
        f'register.html',
        ac_fail=session.pop('ac_fail', False),
        pswd_fail=session.pop('pswd_fail', False)
    )


@app.route('/register/submit', methods=['POST'])
def submit_new_account():
    print(request.values)
    account = request.values['ac']
    pswd = request.values['pswd']
    pswd_c = request.values['pswd_c']

    if pswd != pswd_c:
        session['pswd_fail'] = True
        return redirect(url_for('login.reg'))
    print(UserDB.objects(name=account).first())
    if UserDB.objects(name=account).first():
        session['ac_fail'] = True
        return redirect(url_for('login.reg'))
    else:
        user = UserDB(
            name=account,
            pswd=sha(pswd).hex()
        )
        user.save()
        login(user)
        return redirect(url_for('chat.main'))