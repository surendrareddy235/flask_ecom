from flask import Flask, render_template
from routes import routes
from db import db, app

app.register_blueprint(routes)

with app.app_context(): 
    db.create_all()
    print("uploadfolder_table is created successfully")
app.secret_key = "surendra"

if __name__ == '__main__':
    app.run(debug=True)
