from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
import uuid

from db import db


class ChatModel(db.Model):
    __tablename__ = 'chats'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
    message = db.Column(db.String(1200), unique=False, nullable=False)
    origin = db.Column(db.String(20), unique=False, nullable=False)  # AI, SYSTEM, USER
    format = db.Column(db.String(20), unique=False, nullable=False)  # TEXT, REACTION, VIDEO, AUDIO
    user_id = db.Column(UUID, db.ForeignKey('users.id'), unique=False, nullable=False)
    user = db.relationship('UserModel', back_populates='chats', lazy='dynamic')
    errors = db.relationship('ErrorModel', back_populates='chat', lazy='dynamic')
    sequence = db.Column(db.Integer, unique=False, nullable=False)
    wa_created_at = db.Column(db.DateTime, unique=False, nullable=True)

    created_at = db.Column(db.DateTime, unique=False, nullable=False, default=datetime.utcnow)
