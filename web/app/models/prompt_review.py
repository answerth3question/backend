import uuid
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID, TIMESTAMP
from app.db import db

class PromptReview(db.Model):
  id = db.Column(UUID(as_uuid=True), primary_key=True)
  ts = db.Column(TIMESTAMP(timezone=True), default=datetime.utcnow)
  post_prompt_id = db.Column(UUID(as_uuid=True), db.ForeignKey('post_prompt.id'), nullable=False)
  user_id = db.Column(db.String, nullable=False)
  reviewer_id = db.Column(db.String, nullable=False)
  is_approved = db.Column(db.Boolean, nullable=False)
  reviewer_comments = db.Column(db.String(400))