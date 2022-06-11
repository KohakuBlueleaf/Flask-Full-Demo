from flask import Flask
from middleware import setup_middlewares
from utils.crypto import AesCrypt
from flask_cors import CORS


def setup_cors(app):
    CORS(
        app, 
        resources = {r"*": {"origins": CORS_ORIGINS}}
    )


SECRET_KEY = "Rice305604"
AES_TEXT = AesCrypt(SECRET_KEY, for_text=True)
AES = AesCrypt(SECRET_KEY)
CORS_ORIGINS = ["*"]

app = Flask(
    __name__,
    static_folder='pages/_static'
)
app.secret_key = SECRET_KEY
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SESSION_COOKIE_DOMAIN'] = False

setup_cors(app)
setup_middlewares(app, 'login.main')