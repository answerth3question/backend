import uuid
from sqlalchemy.dialects.postgresql import UUID
from app.db import db

class PostPending(db.Model):
  id = db.Column(UUID(as_uuid=True), primary_key=True)
  post_id = db.Column(UUID(as_uuid=True), nullable=False, unique=True)