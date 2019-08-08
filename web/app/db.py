import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def init_app(app):
  db.init_app(app)
  migrate = Migrate(app=app, db=db)