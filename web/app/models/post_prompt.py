import uuid
from sqlalchemy.dialects.postgresql import UUID
from app.db import db

class PostPrompt(db.Model):
  id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
  text = db.Column(db.String(140), nullable=False, unique=True)
  posts = db.relationship('UserPost', lazy='dynamic',
                          backref=db.backref('post_prompt', lazy='select', uselist=False))

  def __repr__(self):
    text_sample = self.text if len(self.text) < 20 else self.text[:20]
    return f"PostPrompt {self.id} - {text_sample}"
  
  def save_to_db(self):
    db.session.add(self)
    db.session.commit()