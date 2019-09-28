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
  prompts = db.relationship('Prompt', lazy='dynamic')

  def __repr__(self):
    return f"RegisteredUser {self.id} - {self.email} - {self.username} - {self.role}"

  @classmethod
  def get_profile_user(cls, user_id):
    '''Use this method to fetch data to display when any given logged on user views 
    their profile information'''
    user = cls.query.get(user_id)
    if user:
      return dict(
        id=user.id,
        username=user.username,
        email=user.email,
        role=user.role,
        posts=[p for p in user.posts.all()],
        prompts=[p for p in user.prompts.all()],
      )

  @classmethod
  def get_profile_admin(cls, user_id):
    '''Use this method to fetch data about users for admins to review/use in their tasks'''
    user = cls.query.get(user_id)
    if user:
      return dict(
        id=user.id,
        username=user.username,
        email=user.email,
        role=user.role,
        posts=[p.with_reviews() for p in user.posts.all()],
        prompts=[p.with_reviews() for p in user.prompts.all()],
        logins=[l for l in user.logins.all()],
      )

  def save_to_db(self):
    db.session.add(self)
    db.session.commit()
