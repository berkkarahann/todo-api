from flask import Flask
from flask_cors import CORS
from flask_httpauth import HTTPBasicAuth
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_swagger_ui import get_swaggerui_blueprint

from config import config

# initialize packages for the api
db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()
basic_auth = HTTPBasicAuth()


# creating flask app instance
def create_app(config_name):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)
    migrate.init_app(app, db=db)
    ma.init_app(app)
    from .usecase import auth_blueprint as ab, task_lists_blueprint as tlb
    app.register_blueprint(ab, url_prefix="/auth")
    app.register_blueprint(tlb, url_prefix="/task-lists")

    SWAGGER_URL = '/docs'
    API_URL = '/static/swagger.json'
    SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': "TodoList API"
        }
    )
    app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

    return app
