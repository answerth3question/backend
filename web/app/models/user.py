from app.db import db

class RegisteredUser(db.Model):
  id = db.Column(db.String, primary_key=True, unique=True, nullable=False)
  username = db.Column(db.String)
  email = db.Column(db.String, unique=True, nullable=False)
  role_id = db.Column(db.Integer, db.ForeignKey('user_role.id'))
  role = db.relationship('UserRole', lazy='joined')
  logins = db.relationship('UserLogin', lazy='dynamic')
  posts = db.relationship('UserPost', lazy='dynamic')

  def __repr__(self):
    return f"RegisteredUser {self.id} - {self.email} - {self.username} - {self.role}"

  @classmethod
  def get_complete(cls, id):
    user = cls.query.get(id)
    if user:
      return {
        'logins': [l.ts for l in user.logins.all()],
        'role': user.role,
        'permission': user.role.permission
      }

  # def save_to_db(self):
  #   db.session.add(self)
  #   db.session.commit()
