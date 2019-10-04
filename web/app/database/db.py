import os
from flask_sqlalchemy import SQLAlchemy, Model
from flask_migrate import Migrate

class DictModel(Model):
  def cols_dict(self):
    return { c.name: getattr(self, c.name) for c in self.__table__.columns }

db = SQLAlchemy(model_class=DictModel)

def init_app(app):
  db.init_app(app)
  migrate = Migrate(app=app, db=db)