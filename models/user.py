from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
import uuid

from db import db


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
    name = db.Column(db.String(80), unique=False, nullable=True)
    phone_number = db.Column(db.String(20), unique=True, nullable=False)
    chats = db.relationship('ChatModel', back_populates='user', lazy='dynamic')
    category = db.Column(db.String(20), unique=False, nullable=False)

    created_at = db.Column(db.DateTime, unique=False, nullable=False, default=datetime.utcnow)
