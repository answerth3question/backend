import uuid
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID, TIMESTAMP
from app.db import db

class PostStatus(db.Model):
  id = db.Column(UUID(as_uuid=True), primary_key=True)
  status = db.Column(db.Integer, default=0)
  post = db.relationship('UserPost', uselist=False, lazy='joined')  
  