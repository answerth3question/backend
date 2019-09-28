import uuid
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID, TIMESTAMP
from app.database.db import db

class Prompt(db.Model):
  id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
  date_created = db.Column(TIMESTAMP(timezone=True), default=datetime.utcnow)
  created_by = db.Column(UUID(as_uuid=True), db.ForeignKey('registered_user.id'), nullable=False)
  content = db.Column(db.String(240), nullable=False)
  status = db.Column(db.String, db.ForeignKey('review_status_kind.name'), default='pending')
  posts = db.relationship('Post', lazy='dynamic', 
                          backref=db.backref('prompt', lazy='joined', uselist=False))
  reviews = db.relationship('PromptReview', lazy='dynamic')