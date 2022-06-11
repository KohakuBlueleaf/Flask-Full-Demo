from flask import Flask, g
from flask_login import (
    LoginManager, UserMixin,
    current_user as c_user
)
from database.db import UserDB


class User(UserMixin):
    pass


def load_user(uid):
    if (user_db :=
            UserDB.objects(id=uid).first()) is None:
        return

    user = User()
    user.id = str(user_db.id)
    return user


def setup_middlewares(app: Flask, login_view: str):
    login_manager = LoginManager(app)
    login_manager.login_view = login_view
    login_manager.user_loader(load_user)

    @app.before_request
    def middleware():
        if c_user.is_anonymous or not c_user.is_authenticated:
            g.user = None
            return
        g.user = UserDB.objects(id=c_user.id).first()
