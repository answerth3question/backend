from datetime import datetime
from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy import text
from app.db import db

class UserLogin(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  ts = db.Column(TIMESTAMP(timezone=True), default=datetime.utcnow)
  user_id = db.Column(db.String, db.ForeignKey('user.id'), nullable=False)

  def __repr__(self):
    return f"UserLogin {self.user_id} - {self.ts}"

  def save_to_db(self):
    db.session.add(self)
    db.session.commit()