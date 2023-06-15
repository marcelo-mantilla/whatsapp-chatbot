from flask import Flask
from flask_migrate import Migrate

from src.router.status import status
from src.router.users import users
from src.router.whatsapp import whatsapp
from db import db

import os


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
Migrate(app, db)

app.register_blueprint(status)
app.register_blueprint(users)
app.register_blueprint(whatsapp)

port = os.getenv('PORT', 8000)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
