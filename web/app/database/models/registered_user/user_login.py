from datetime import datetime
from sqlalchemy.dialects.postgresql import TIMESTAMP, UUID
from app.database.db import db

class UserLogin(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  date_created = db.Column(TIMESTAMP(timezone=True), default=datetime.utcnow)
  user_id = db.Column(UUID(as_uuid=True), db.ForeignKey('registered_user.id'), nullable=False)

  def __repr__(self):
    return f"UserLogin {self.user_id} - {self.date_created}"

  def save_to_db(self):
    db.session.add(self)
    db.session.commit()