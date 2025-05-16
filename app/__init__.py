from flask import Flask 
from app.config import Config
from .extensions import jwt

def create_app ():
    app = Flask(__name__)
    app.config.from_object(Config)

    jwt.init_app(app)
    
    from .routes.auth import auth_bp
    app.register_blueprint(auth_bp)
    return app