import uuid
from sqlalchemy.dialects.postgresql import UUID
from app.db import db

class UserPost(db.Model):
  id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
  body = db.Column(db.String(1000) , nullable=False)
  prompt_id = db.Column(UUID(as_uuid=True), nullable=False, db.ForeignKey('prompt.id'))
  user_id = db.Column(db.String, nullable=False, db.ForeignKey('registered_user.id'))

  def save_to_db(self):
    db.session.add(self)
    db.session.commit()