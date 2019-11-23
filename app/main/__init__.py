import os
from flask import Blueprint, Flask, render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .auth import auth as auth_bp  # can't import db otherwise in model.User


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

    db.init_app(app)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    os.makedirs(app.instance_path, exist_ok=True)

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)

    return app


main_bp = Blueprint('main_bp', __name__)


@main_bp.route('/')
def index():
    return render_template('index.html')


app = create_app()
db.create_all(app=app)