from app.db import db
from app.models.user_role import user_role

class User(db.Model):
  id = db.Column(db.String, primary_key=True, unique=True, nullable=False)
  username = db.Column(db.String)
  email = db.Column(db.String, unique=True, nullable=False)
  roles = db.relationship('Role', secondary=user_role, lazy='select')
  logins = db.relationship('UserLogin', lazy='dynamic')

  def __repr__(self):
    return f"User {self.id} - {self.email} - {self.username} - {self.role}"

  @classmethod
  def find(cls, id):
    return cls.query.get(id)

  def save_to_db(self):
    db.session.add(self)
    db.session.commit()


























# class User(db.Model):
#   id = db.Column(db.String, primary_key=True, unique=True, nullable=False)
#   username = db.Column(db.String)
#   email = db.Column(db.String, unique=True, nullable=False)
#   role_ids = db.Column(ARRAY(db.Integer), db.ForeignKey('user_role.id'), default=[1])
#   roles = db.relationship('UserRole', lazy='select', foreign_keys=role_ids)
#   logins = db.relationship('UserLogin', lazy='dynamic')

#   def __repr__(self):
#     return f"User {self.id} - {self.email} - {self.username} - {self.role}"

#   @classmethod
#   def find(cls, id):
#     return cls.query.get(id)

#   def save_to_db(self):
#     db.session.add(self)
#     db.session.commit()