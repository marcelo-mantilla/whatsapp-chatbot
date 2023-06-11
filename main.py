from flask import Flask
from flask_migrate import Migrate

from src.router.status import status
from src.router.users import users
from src.router.whatsapp import whatsapp
from db import db

import os


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    Migrate(app, db)

    app.register_blueprint(status)
    app.register_blueprint(users)
    app.register_blueprint(whatsapp)

    return app

create_app().run(port=5000)
