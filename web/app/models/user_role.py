from app.db import db

class UserRole(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String)

  def __repr__(self):
    return f"UserRole {self.id} - {self.name}"

  def save_to_db(self):
    db.session.add(self)
    db.session.commit()