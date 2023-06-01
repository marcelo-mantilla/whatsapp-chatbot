from flask import Flask
from flask_migrate import Migrate
from api.status.router import status_router
from api.users.router import users_router
from api.whatsapp.router import whatsapp_router
from db import db

import os


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    migrate = Migrate(app, db)

    app.register_blueprint(status_router)
    app.register_blueprint(users_router)
    app.register_blueprint(whatsapp_router)

    return app


create_app().run(port=5000)
