from db import db

class Signup(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

class uploadfolder_table(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name= db.Column(db.String(100), nullable=False)
    email= db.Column(db.String(100), nullable=False)
    language= db.Column(db.String(50), nullable=False)
    folder_path= db.Column(db.String(255), nullable=False)
    