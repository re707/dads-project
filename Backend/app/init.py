from flask import Flask
from .extensions import db
from .routes_main import main_bp
from .routes_admin import admin_bp
from .routes_auth import auth_bp
import os

def create_app():
    app = Flask(__name__)

    # Load configs
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "dev_key")
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL", "sqlite:///ngo.db")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'backend', 'uploads')

    # Initialize DB
    db.init_app(app)

    # Register blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(admin_bp, url_prefix="/admin")
    app.register_blueprint(auth_bp, url_prefix="/auth")

    return app
