from flask import Flask
from app_init import setup_cors
from .login import app


def setup(main_app: Flask):
    setup_cors(app)
    main_app.register_blueprint(app)
