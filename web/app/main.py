import os
import redis
from flask import Flask

from .util import CustomErrorHandler, CustomJSONEncoder

def create_app(config=None):
  app = Flask(__name__)
  app.json_encoder = CustomJSONEncoder

  r = redis.Redis(host=os.environ.get('REDIS_HOST'), port=6379, db=0, decode_responses=True)

  if config:
    app.config.from_object(config)

  error_handler = CustomErrorHandler()

  error_handler.init_app(app)

  @app.route("/")
  def index():
    return "Hello from flask!"

  @app.route("/hello/")
  @app.route("/hello/<name>")
  def hello(name=None):
    if name:
      r.set('name', name)
      return dict(name=r.get('name'), holla='back')
    return "Hello"

  return app