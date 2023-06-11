from models import UserModel
from models import ChatModel
from src.services.chat.initialize import get_or_initialize_chat
from db import db


def create_message(user: UserModel, message: str, category: str, origin: str, wa_created_at: str):
    message = ChatModel(
        user=user,
        origin=origin,
        message=message,
        category=category,
    )
    db.session.add(message)
    db.session.commit()

    return message
