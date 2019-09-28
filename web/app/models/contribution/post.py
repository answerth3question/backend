import uuid
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID, TIMESTAMP
from app.db import db

class Post(db.Model):
  id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
  date_created = db.Column(TIMESTAMP(timezone=True), default=datetime.utcnow)
  created_by = db.Column(UUID(as_uuid=True), db.ForeignKey('registered_user.id'), nullable=False)
  content = db.Column(db.String(1000), nullable=False)
  prompt_id = db.Column(UUID(as_uuid=True), db.ForeignKey('prompt.id'), nullable=False)
  