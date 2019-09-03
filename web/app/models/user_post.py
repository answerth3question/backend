import uuid
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID, TIMESTAMP
from app.db import db

class UserPost(db.Model):
  id = db.Column(UUID(as_uuid=True), primary_key=True)
  ts = db.Column(TIMESTAMP(timezone=True), default=datetime.utcnow)
  status = db.Column(db.Integer, default=0)
  user_id = db.Column(db.String, db.ForeignKey('registered_user.id'), nullable=False)
  post_prompt_id = db.Column(UUID(as_uuid=True), db.ForeignKey('post_prompt.id'), nullable=False)
  content = db.relationship('PostContent', uselist=False, lazy='joined')
  reviews = db.relationship('PostReview', lazy='select')
  

  def __repr__(self):
    content_slice = self.content.text[:20] if len(self.content.text) > 20 else self.content.text
    return f'UserPost {self.id} - {self.user_id} - {content_slice}'

  def save_to_db(self):
    db.session.add(self)
    db.session.commit()