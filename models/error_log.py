from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
import uuid

from db import db


class ErrorLogModel(db.Model):
    __tablename__ = 'error_logs'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
    traceback = db.Column(db.String(1000), unique=False, nullable=True)
    chat_id = db.Column(UUID, db.ForeignKey('chats.id'), unique=False, nullable=True)
    chat = db.relationship('ChatModel', back_populates='error_logs', lazy='dynamic')

    created_at = db.Column(db.DateTime, unique=False, nullable=False, default=datetime.utcnow)
