from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    age = db.Column(db.Integer)

    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

# Create database tables
db.create_all()

@app.route('/')
def home():
    return redirect('/users')

@app.route('/users')
def users():
    users = User.query.all()
    return render_template('users.html', users=users)

@app.route('/users/new', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        age = request.form['age']
        user = User(name, email, age)
        db.session.add(user)
        db.session.commit()
        return redirect('/users')
    return render_template('adduser.html')

@app.route('/users/<int:user_id>')
def view_user(user_id):
    user = User.query.get(user_id)
    return render_template('viewuser.html', user=user)

@app.route('/users/<int:user_id>/edit', methods=['GET', 'POST'])
def edit_user(user_id):
    user = User.query.get(user_id)
    if request.method == 'POST':
        user.name = request.form['name']
        user.email = request.form['email']
        user.age = request.form['age']
        db.session.commit()
        return redirect('/users')
    return render_template('edituser.html', user=user)

@app.route('/users/<int:user_id>/delete', methods=['POST'])
def delete_user(user_id):
    user = User.query.get(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect('/users')

if __name__ == '__main__':
    app.run(debug=True)