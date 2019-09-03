import uuid
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID, TIMESTAMP
from app.db import db

class PostPending(db.Model):
  post_id = db.Column(UUID(as_uuid=True), primary_key=True)
  ts = db.Column(TIMESTAMP(timezone=True), default=datetime.utcnow)
  
