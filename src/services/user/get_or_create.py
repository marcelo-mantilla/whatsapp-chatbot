from db import db
from models.user import UserModel


def get_or_create_user(name: str, phone_number: str):
    user = UserModel.query.filter_by(phone_number=phone_number).first()
    if user:
        return user
    user = UserModel(name=name, phone_number=phone_number)
    db.session.add(user)
    db.session.commit()
    return user
