from flask import Blueprint, render_template,request,redirect,url_for,flash
from model import db, Signup
routes = Blueprint('routes',__name__)

@routes.route("/")
def showhome():
    return render_template('home.html')

@routes.route("/signup")
def showsignup():
    return render_template('signup.html')

@routes.route("/login")
def showLogin():
    return render_template("login.html")


@routes.route("/signupform", methods=["POST"])
def showsignupform():
    email =request.form['email']
    password = request.form['password']
   
    if Signup.query.filter_by(email=email).first():
        return redirect(url_for("routes.showLogin"))
    
    new_user = Signup(email=email, password= password)
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for("routes.showLogin"))


@routes.route("/loginform", methods=["POST"])
def showloginform():
    email = request.form["email"]
    password = request.form["password"]

    user = Signup.query.filter_by(email = email, password = password).first()

    if user:
        return redirect(url_for("routes.showhome"))
    else:
        flash("please signup first...!")
        return redirect(url_for("routes.showsignup"))
