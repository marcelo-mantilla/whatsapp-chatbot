from src.helpers.prompts import system_prompt
from models.chat import ChatModel
from models.user import UserModel
from db import db


def get_or_initialize_chat(user: UserModel):
    chat = ChatModel.query.filter_by(user=user).all()
    prompt = system_prompt(user.name)

    if len(chat) > 0:
        return chat

    chat = ChatModel(
        user=user,
        origin='SYSTEM',
        category='TEXT',
        message=prompt,
    )

    db.session.add(chat)
    db.session.commit()

    return chat
