from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config
import os

db = SQLAlchemy()

def create_app(config_class = Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    db.init_app(app)
    
    from app.views import views
    from app.auth import auth
    from app.models import User, Post, Comment, Like, Dislike
    app.register_blueprint(views, url_prefix = "/")
    app.register_blueprint(auth, url_prefix = "/")
    
    create_db(app)
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def login_user(id):
        return User.query.get(int(id))
    
    
    return app


def create_db(app):
    if not os.path.exists("app/database.db"):
        with app.app_context():
            db.create_all()
    