from flask import Blueprint, render_template,redirect,url_for,request,flash
import re
from app import db
from app.models import User
from flask_bcrypt import Bcrypt
from flask_login import login_user, logout_user, login_required
auth = Blueprint("auth", __name__)
bcrypt = Bcrypt()


@auth.route("/login", methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        
        user = User.query.filter_by(email = email).first()
        
        if user and bcrypt.check_password_hash(user.password, password): 
            login_user(user, remember=True)
            flash("Login Successfull." , "Success")
            return redirect(url_for("views.home"))
        else:
            flash("Invalid Email or Password", "Error")
            
    return render_template("login.html")

@auth.route("/register", methods = ["POST", "GET"])
def register():
    if request.method == "POST":
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password'] 
        
        print(username, email, password)   
        
        user_email = User.query.filter_by(email = email).first()
        user_pass = User.query.filter_by(username = username).first()

        
        if user_email or user_pass:
            flash("Account Already Exist.", "Error")
            return redirect(url_for("auth.login"))
        
        elif password != confirm_password:
            flash("Password do not Match.", "Error")
            
        elif len(password) < 6:
            flash("Password Too Short.", "Error")
            
        elif not re.fullmatch(regex, email):
            flash("Invalid Email.", "Error")
            
        else:
            hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
            new_user = User(email = email, username = username, password = hashed_password)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash("Account Successfully Created.", "Success")
            return redirect(url_for("auth.login"))
        
        
    return render_template("register.html")


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("views.home"))

