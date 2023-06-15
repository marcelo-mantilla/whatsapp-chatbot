from src.helpers.prompts import system_prompt
from models.message import MessageModel
from models.user import UserModel
from db import db


def get_or_initialize_chat(user: UserModel):
    chat = MessageModel.query.filter_by(user=user).all()

    if len(chat) > 0:
        return chat

    message = MessageModel(
        user=user,
        origin='SYSTEM',
        category='TEXT',
        message=system_prompt(user.name),
    )

    db.session.add(message)
    db.session.commit()

    return [message]
