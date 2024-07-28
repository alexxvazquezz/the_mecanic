from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object('config.Config')

    db.init_app(app)
    jwt.init_app(app)

    with app.app_context():
        from .routes import auth_routes, protected_routes, profile_routes
        app.register_blueprint(auth_routes.bp)
        app.register_blueprint(protected_routes.bp)
        app.register_blueprint(profile_routes.bp)
        db.create_all()
    
    return app