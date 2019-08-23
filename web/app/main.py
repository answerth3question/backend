import dotenv
from flask import Flask, request

from . import db
from .util import CustomErrorHandler, CustomJSONEncoder, jwt
from .blueprints import auth_bp, admin_bp

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

  # @app.before_request
  # def before():
  #   print(request.headers)

  app.register_blueprint(auth_bp, url_prefix='/api/auth')
  app.register_blueprint(admin_bp, url_prefix='/api/admin')

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