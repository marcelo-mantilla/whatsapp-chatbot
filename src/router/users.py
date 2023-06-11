from flask import request, Blueprint, abort, jsonify
from sqlalchemy.exc import SQLAlchemyError

from src.services.user.validations import validate_category_enum
from models.user import UserModel

from db import db

users = Blueprint('user', __name__, url_prefix='/user')


@users.route('/<string:user_id>', methods=['GET'])
def get_user(user_id: str):
    user = UserModel.query.get_or_404(user_id)
    return jsonify(user.serialize), 200


@users.route('/', methods=['POST'])
def post_user():
    request_data = request.get_json()
    user = UserModel(**request_data)

    try:
        validate_category_enum(user.category)
        db.session.add(user)
        db.session.commit()
        return jsonify(user.serialize), 201
    except SQLAlchemyError as e:
        abort(400, f"Bad Request: {e.__dict__['orig']}")
    except ValueError as e:
        abort(400, f"Bad Request: {e}")


@users.route('/<string:user_id>/chats', methods=['GET'])
def get_chats(user_id: str):
    user = UserModel.query.get_or_404(user_id)
    loaded_chats = user.chats
    chats = [chat.serialize for chat in loaded_chats]

    # chats.sort

    return chats, 200
