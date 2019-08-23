from app.db import db

user_role = db.Table('user_role',
  db.Column('role_id', db.Integer, db.ForeignKey('role.id'), primary_key=True),
  db.Column('user_id', db.String, db.ForeignKey('user.id'), primary_key=True)
)

