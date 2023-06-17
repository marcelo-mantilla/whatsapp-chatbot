from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
import uuid

from db import db


class UserModel(db.Model):
    __tablename__ = 'user'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
    name = db.Column(db.String(80), unique=False, nullable=True)
    phone_number = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=True)
    google_calendar_id = db.Column(db.String(120), unique=True, nullable=True)
    messages = db.relationship('MessageModel', back_populates='user', lazy='dynamic')
    created_at = db.Column(db.DateTime, unique=False, nullable=False, default=datetime.utcnow)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'phone_number': self.phone_number,
            'created_at': self.created_at
        }
