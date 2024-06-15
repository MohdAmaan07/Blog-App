from flask import Blueprint, render_template,redirect, request, flash,redirect,url_for
from .models import Post,Comment, Like,Dislike
from app import db
from datetime import timezone, datetime
from flask_login import login_required, current_user

views = Blueprint("views", __name__)

@views.route("/")
@views.route("/home")
def home():
    posts = Post.query.all()
    # comment = Comment.query.filter_by
    return render_template("index.html", posts = posts)

@views.route("/create-post", methods = ["POST", "GET"])
@login_required
def create_post():
    if request.method == "POST":
        title = request.form['title']
        content = request.form['content']
        
        if not title:
            flash("Title cannot be Empty", "Error")
        elif not content:
            flash("Content cannot be Empty", "Error")
        
    
        else:
            post = Post(title = title, content = content, author = current_user.id)
            db.session.add(post)
            db.session.commit()
            flash("Post Created", "Success")
            return redirect(url_for("views.home"))
            
            
    return render_template("create_post.html")
    

@views.route("/view/<int:id>")
@login_required
def view_post(id):
    posts = Post.query.filter_by(author = id).all()
    return render_template("view_post.html", posts = posts)



@views.route("/delete/<int:id>")
@login_required
def delete_post(id):
    post = Post.query.filter_by(id = id).first()
    
    if not post:
        flash("Post does not Exist", "Error")
        return redirect(url_for("views.home"))
    
    db.session.delete(post)
    db.session.commit()
    
    flash("Post Deleted Successfully", "Success")

    return redirect(url_for("views.home"))


@views.route("/create-comment/<int:id>" , methods= ["POST"])
@login_required
def create_comment(id):
    content = request.form['comment']
    if not content:
        flash("Comment Empty", "Error")
        return redirect(url_for("views.home"))
        
    else:
        comment = Comment(content = content, author = current_user.id, post_id = id, date_posted = datetime.now(timezone.utc))
        db.session.add(comment)
        db.session.commit()
        flash("Comment Added!!", "Success")
        
    return redirect(url_for("views.home"))
        
@views.route("/delete-comment/<int:id>")
@login_required
def delete_comment(id):
    comment = Comment.query.filter_by(id = id).first()
    if not comment:
        flash("Comment does not Exist", "Error")
        return redirect(url_for("views.home"))
    else:
        db.session.delete(comment)
        db.session.commit()
        flash("Comment Deleted", "Success")
    
    return redirect(url_for("views.home"))

@views.route('/like/<int:id>', methods=['GET'])
@login_required
def like_post(id):
    like = Like.query.filter_by(author=current_user.id, post_id=id).first()
    if like:
        db.session.delete(like)
        db.session.commit()
    else:
        like = Like(author=current_user.id, post_id=id)
        db.session.add(like)
        db.session.commit()
    return redirect(url_for('views.home'))

@views.route('/dislike/<int:id>', methods=['GET'])
@login_required
def dislike_post(id):
    dislike = Dislike.query.filter_by(author=current_user.id, post_id=id).first()
    if dislike:
        db.session.delete(dislike)
        db.session.commit()
    else:
        dislike = Dislike(author=current_user.id, post_id=id)
        db.session.add(dislike)
        db.session.commit()
    return redirect(url_for('views.home'))


    