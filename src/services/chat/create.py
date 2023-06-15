from models import UserModel
from models import MessageModel
from src.services.chat.initialize import get_or_initialize_chat
from db import db


def save_message(user: UserModel, message: str, category: str, origin: str, wa_created_at: str = None) -> MessageModel:
    print('saving message:', message)
    message = MessageModel(
        user=user,
        origin=origin,
        message=message,
        category=type_map(category),
        wa_created_at=wa_created_at
    )
    db.session.add(message)
    db.session.commit()

    return message


def type_map(type: str):
    match type:
        case 'text':
            return 'TEXT'
        case 'image':
            return 'IMAGE'
        case _:
            return type
