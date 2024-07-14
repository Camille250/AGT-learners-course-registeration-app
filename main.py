from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Configuration for the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    course = db.Column(db.String(50), nullable=False)

# Create the database and tables
with app.app_context():
    db.create_all()

# Default course options
course_options = ["DevOps", "Cloud Computing", "Data Science", "Machine Learning"]
color = os.environ.get('APP_COLOR')
@app.route("/", methods=["GET", "POST"])
def main():
    model = {"title": "Welcome to AGT DevOps Bootcamp"}
    users = User.query.all()  # Retrieve all records from the User table
    
    return render_template('index.html', model=model, users=users, courses=course_options, color=color)

@app.route("/add_user", methods=["POST"])
def add_user():
    name = request.form.get("name")
    email = request.form.get("email")
    course = request.form.get("course")

    if name and email and course:
        new_user = User(name=name, email=email, course=course)
        db.session.add(new_user)
        db.session.commit()
    
    return redirect(url_for('main'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True, threaded=True)
