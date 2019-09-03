import uuid
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID, TIMESTAMP
from app.db import db

class UserPost(db.Model):
  id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
  body = db.Column(db.String(1000) , nullable=False)
  ts = db.Column(TIMESTAMP(timezone=True), default=datetime.utcnow)
  prompt_id = db.Column(UUID(as_uuid=True), nullable=False, db.ForeignKey('prompt.id'))
  user_id = db.Column(db.String, nullable=False, db.ForeignKey('registered_user.id'))

  def save_to_db(self):
    db.session.add(self)
    db.session.commit()