from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
import uuid
from db import db


class OpenAILogModel(db.Model):
    __tablename__ = 'openai_logs'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
    log = db.Column(db.String(1200), unique=False, nullable=True)
    content = db.Column(db.String(1200), unique=False, nullable=True)
    created_at = db.Column(db.DateTime, unique=False, nullable=False, default=datetime.utcnow)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'log': self.log,
            'created_at': self.created_at
        }
