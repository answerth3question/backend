import os

class BaseConfig:
  JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')

  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
  SQLALCHEMY_TRACK_MODIFICATINS = False