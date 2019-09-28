import dotenv
from flask import Flask, request
from .database import db
from .commands import seed_db_command
from .util import CustomErrorHandler, CustomJSONEncoder, jwt
from .blueprints import (
  auth_bp, 
  admin_bp, 
  user_bp, 
  post_bp, 
  prompt_bp
)

dotenv.load_dotenv()

def create_app(config=None):
  app = Flask(__name__)
  app.json_encoder = CustomJSONEncoder

  if config:
    app.config.from_object(config)

  error_handler = CustomErrorHandler()
  
  db.init_app(app)
  error_handler.init_app(app)
  jwt.init_app(app)

  app.cli.add_command(seed_db_command)

  app.register_blueprint(auth_bp, url_prefix='/api/auth')
  app.register_blueprint(admin_bp, url_prefix='/api/admin')
  app.register_blueprint(user_bp, url_prefix='/api/user')
  app.register_blueprint(post_bp, url_prefix='/api/post')
  app.register_blueprint(prompt_bp, url_prefix='/api/prompt')

  html = """
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset"utf-8" />
    <title>Hello From Flask :)</title>
    <style>
      .row {
        display: flex;
        justify-content: center;
        align-content: center;
      }
      h1 {
        font-size: 50px;
      }
    </style>
  </head>
  <body>
    <div class="row">
      <h1>Well hold on now, you need to call the api dude</h1>
    </div>
  </body>
  </html>
  """

  @app.route("/")
  def index():
    return html

  return app