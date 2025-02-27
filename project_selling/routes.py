from flask import Blueprint, render_template,request,redirect,url_for,flash
from model import db, Signup
routes = Blueprint('routes',__name__)

@routes.route("/")
def showhome():
    return render_template('home.html')

@routes.route("/signup")
def showsignup():
    return render_template('signup.html')


@routes.route("/signupform", methods=["POST"])
def showsignupform():
    email =request.form['email']
    password = request.form['password']
   
    if Signup.query.filter_by(email=email).first():
        flash ("email is registerd alredy please login","error")
        return redirect(url_for("routes.showLogin"))
    
    new_user = Signup(email=email, password= password)
    db.session.add(new_user)
    db.session.commit()
    flash("you are signup successfully")
    return redirect(url_for("routes.showLogin"))

@routes.route("/login")
def showLogin():
    return render_template("login.html")