from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_login import LoginManager
from config import config
import json

db = SQLAlchemy()

login_manager = LoginManager()
login_manager.session_protection = 'strong'

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    CORS(app, supports_credentials=True)
    db.init_app(app)
    login_manager.init_app(app)

    from .view.user import user_blueprint
    app.register_blueprint(user_blueprint, url_prefix='/user')

    from .view.qualitative import qualitative_blueprint
    app.register_blueprint(qualitative_blueprint,  url_prefix='/qualitative')

    from .view.quantify import quantify_blueprint
    app.register_blueprint(quantify_blueprint, url_prefix='/quantify')

    return app


SPECIAL_ARGS=[
    'page',
    'token',
    'password'
]


def check_args(f,s):

    return set(f+SPECIAL_ARGS) > set(s)

def std_json(d):

    r = {}
    for k, v in d.items():
        r[k] = json.loads(v)

    return r