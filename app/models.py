from datetime import datetime, timezone
from flask_login import UserMixin
from . import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime(timezone = True), nullable=False, default=datetime.now(timezone.utc))
    author = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
    comment = db.relationship('Comment', backref = "post", passive_deletes = True)
    likes = db.relationship('Like', backref = "post", passive_deletes = True)
    dislikes = db.relationship('Dislike', backref = "post", passive_deletes = True)

    
    
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default=datetime.now(timezone.utc), nullable=False)
    posts = db.relationship('Post', backref = "user", passive_deletes = True)
    comment = db.relationship('Comment', backref = "user", passive_deletes = True)
    likes = db.relationship('Like', backref = "user", passive_deletes = True)
    dislikes = db.relationship('Dislike', backref = "user", passive_deletes = True)

    
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String(200), nullable=False)
    date_posted = db.Column(db.DateTime(timezone = True), nullable=False, default=datetime.now(timezone.utc))
    author = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id', ondelete="CASCADE"), nullable=False)
 
class Like(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id', ondelete="CASCADE"), nullable=False)

class Dislike(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id', ondelete="CASCADE"), nullable=False)

    