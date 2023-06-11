from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
import uuid

from db import db


class ChatModel(db.Model):
    __tablename__ = 'chats'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
    message = db.Column(db.String(1200), unique=False, nullable=False)
    origin = db.Column(db.String(20), unique=False, nullable=False)  # LLM, SYSTEM, USER
    category = db.Column(db.String(20), unique=False, nullable=False)  # TEXT, REACTION, VIDEO, AUDIO
    user_id = db.Column(UUID, db.ForeignKey('user.id'), unique=False, nullable=False)
    user = db.relationship('UserModel', back_populates='chats')
    # errors = db.relationship('ErrorLogModel', back_populates='chat')
    wa_created_at = db.Column(db.DateTime, unique=False, nullable=True)

    created_at = db.Column(db.DateTime, unique=False, nullable=False, default=datetime.utcnow)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'message': self.message,
            'origin': self.origin,
            'format': self.format,
            'user_id': self.user_id,
            'sequence': self.sequence,
            'wa_created_at': self.wa_created_at,
            'created_at': self.created_at
        }
