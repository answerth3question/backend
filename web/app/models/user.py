from app.db import db

class RegisteredUser(db.Model):
  id = db.Column(db.String, primary_key=True, unique=True, nullable=False)
  username = db.Column(db.String)
  email = db.Column(db.String, unique=True, nullable=False)
  role_id = db.Column(db.Integer, db.ForeignKey('user_role.id'))
  role = db.relationship('UserRole', lazy='select')
  logins = db.relationship('UserLogin', lazy='dynamic')

  def __repr__(self):
    return f"RegisteredUser {self.id} - {self.email} - {self.username} - {self.role}"

  @classmethod
  def find(cls, id):
    return cls.query.get(id)

  def save_to_db(self):
    db.session.add(self)
    db.session.commit()
