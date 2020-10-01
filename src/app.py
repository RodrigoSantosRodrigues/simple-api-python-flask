from flask import Flask
from .config import app_config

from .controllers.HomeController import home_api

def create_app(env_name):
  """
    param: env_name 

    Create app
  """
  # app initiliazation
  app = Flask(__name__)
  app.config.from_object(app_config[env_name])

  app.register_blueprint(home_api, url_prefix='/v1/api/home')

  @app.route('/')
  def index():
    return 'My first Server Works!'
    
  @app.route('/greet')
  def hello():
    return 'Hello from Server'

  return app
