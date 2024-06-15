import secrets

class Config:
    SECRET_KEY = secrets.token_urlsafe(32)
    SQLALCHEMY_DATABASE_URI = f"sqlite:///database.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False