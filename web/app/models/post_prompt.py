import uuid
from sqlalchemy.dialects.postgresql import UUID
from app.db import db

class PostPrompt(db.Model):
  id = db.Column(UUID(as_uuid=True), primary_key=True)
  body = db.Column(db.String(140), nullable=False, unique=True)

  def __repr__(self):
    body_sample = self.body if len(self.body) < 20 else self.body[:20]
    return f"PostPrompt {self.id} - {body_sample}"
  
  def save_to_db(self):
    db.session.add(self)
    db.session.commit()