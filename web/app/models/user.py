from app.db import db

class User(db.Model):
  id = db.Column(db.String, primary_key=True, unique=True, nullable=False)
  username = db.Column(db.String)
  email = db.Column(db.String, unique=True, nullable=False)
  role_id = db.Column(db.Integer, db.ForeignKey('user_role.id'), default=1)
  role = db.relationship('UserRole', lazy='select', foreign_keys=role_id, uselist=False)

  def __repr__(self):
    return f"User {self.id} - {self.email} - {self.username} - {self.role}"

  @classmethod
  def find(cls, id):
    return cls.query.get(id)

  def save_to_db(self):
    db.session.add(self)
    db.session.commit()