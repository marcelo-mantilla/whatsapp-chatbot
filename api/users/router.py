from flask import request, Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError
from models.user import UserModel

from db import db


users_router = Blueprint('users', __name__, url_prefix='/users')

@users_router.route('/<string:user_id>', methods=['GET'])
def get_user(user_id):
    user = UserModel.query.get_or_404(user_id)
    return user

@users_router.route('/', methods=['POST'])
def post_user():
    request_data = request.get_json()
    user = UserModel(**request_data)

    try:
        db.session.add(user)
        db.session.commit()
    except SQLAlchemyError as e:
        abort(500, f"Internal Server Error: {e.__dict__['orig']}")

    return user
