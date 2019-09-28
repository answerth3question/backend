import uuid
from sqlalchemy.dialects.postgresql import UUID
from app.database.db import db

class RegisteredUser(db.Model):
  id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
  oauth_openid = db.Column(db.String, unique=True) # if the user registered through OAuth2
  username = db.Column(db.String)
  email = db.Column(db.String, unique=True, nullable=False)
  role_id = db.Column(db.Integer, db.ForeignKey('user_role.id'))
  role = db.relationship('UserRole', lazy='joined')
  logins = db.relationship('UserLogin', lazy='dynamic')
  posts = db.relationship('Post', lazy='dynamic')

  def __repr__(self):
    return f"RegisteredUser {self.id} - {self.email} - {self.username} - {self.role}"

  @classmethod
  def get_complete(cls, id):
    user = cls.query.get(id)
    if user:
      return {
        'logins': [l.date_created for l in user.logins.all()],
        'role': user.role,
        'permission': user.role.permission
      }

  def save_to_db(self):
    db.session.add(self)
    db.session.commit()
