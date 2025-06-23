from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from server.models import db 
from server.config import Config

from server.controllers.auth_controller import auth_bp
from server.controllers.guest_controller import guest_bp
from server.controllers.episode_controller import episode_bp
from server.controllers.appearance_controller import appearance_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app)

    db.init_app(app)
    Migrate(app, db)
    JWTManager(app)

    app.register_blueprint(auth_bp, url_prefix="/")
    app.register_blueprint(guest_bp, url_prefix="/")
    app.register_blueprint(episode_bp, url_prefix="/")
    app.register_blueprint(appearance_bp, url_prefix="/")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(port=5555, debug=True)