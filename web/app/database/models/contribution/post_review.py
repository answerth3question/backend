import uuid
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID, TIMESTAMP
from app.database.db import db

class PostReview(db.Model):
  id = db.Column(UUID(as_uuid=True), primary_key=True)
  post_id = db.Column(UUID(as_uuid=True), db.ForeignKey('post.id'), nullable=False)
  date_created = db.Column(TIMESTAMP(timezone=True), default=datetime.utcnow)
  date_modified = db.Column(TIMESTAMP(timezone=True))
  created_by = db.Column(UUID(as_uuid=True), db.ForeignKey('registered_user.id'), nullable=False)
  is_approved = db.Column(db.Boolean, nullable=False)
  comments = db.Column(db.String(400))