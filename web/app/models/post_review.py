import uuid
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID, TIMESTAMP
from app.db import db

class PostReview(db.Model):
  id = db.Column(UUID(as_uuid=True), primary_key=True)
  ts = db.Column(TIMESTAMP(timezone=True), default=datetime.utcnow)
  user_post_id = db.Column(UUID(as_uuid=True), db.ForeignKey('user_post.id'), nullable=False)
  user_id = db.Column(db.String, nullable=False)
  reviewer_id = db.Column(db.String, nullable=False)
  is_approved = db.Column(db.Boolean, nullable=False)
  reviewer_comments = db.Column(db.String(400))
