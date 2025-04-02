from flask import Flask
from app.api.v1.auth.login import auth_blueprint
from app.api.v1.dashboard.summary import dashboard_blueprint
from app.api.v1.ecs.clusters import ecs_blueprint
from config.settings import Config
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    app.config.from_object(Config)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(dashboard_blueprint)
    app.register_blueprint(ecs_blueprint)
    return app