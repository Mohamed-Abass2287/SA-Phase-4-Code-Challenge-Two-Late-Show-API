from flask import Flask
from server.config import Config
from server.extensions import db, migrate, jwt
from server.controllers.auth_controller import auth_bp
from server.controllers.appearance_controller import appearance_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # Register Blueprints inside the create_app function
    app.register_blueprint(auth_bp)
    app.register_blueprint(appearance_bp)

    @app.route("/")
    def index():
        return {"message": "Welcome to the Late Show API!"}, 200

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)