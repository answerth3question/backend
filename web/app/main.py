import dotenv
from flask import Flask

from . import db

from .util import CustomErrorHandler, CustomJSONEncoder, jwt
from .blueprints import auth_bp, admin_bp

dotenv.load_dotenv()

def create_app(config=None):
  app = Flask(__name__)
  app.json_encoder = CustomJSONEncoder

  # r = redis.Redis(host=os.environ.get('REDIS_HOST'), port=6379, db=0, decode_responses=True)

  if config:
    app.config.from_object(config)

  error_handler = CustomErrorHandler()
  
  
  db.init_app(app)
  error_handler.init_app(app)
  jwt.init_app(app)

  app.register_blueprint(auth_bp, url_prefix='/api/user')
  app.register_blueprint(admin_bp, url_prefix='/api/admin')

  @app.route("/")
  def index():
    return "Hello from flask!"

  return app