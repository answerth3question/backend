import uuid
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID, TIMESTAMP
from app.db import db

class PostReviewStatus(db.Model):
  post_id = db.Column(UUID(as_uuid=True), db.ForeignKey('post.id'), primary_key=True)
  status = db.Column(db.String, db.ForeignKey('review_status_kind.name'), default='pending')