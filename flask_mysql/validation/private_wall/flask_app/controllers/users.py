from flask_app import app 
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_app.models.message import Message
from flask_bcrypt import Bcrypt 
bcrypt = Bcrypt(app)


@app.route('/')
def index():
    return render_template("main.html")

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/validate', methods=['POST'])
def validation():
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)

    data = {
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "email" : request.form['email'],
        "password" : pw_hash
    }

    if not User.validate_registration(request.form):
        return redirect('/register')


    user_id = User.save(data)
    session['user_id'] = user_id
    return redirect('/dashboard')


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/valid', methods=['POST'])
def validate():
    data = {
        "email" : request.form['email']
    }
    users = User.find_email(data)

    if not users:
        flash("Invaild Email Address/Password","login")
        return redirect('/login')

    if not bcrypt.check_password_hash(users.password, request.form['password']):
        flash("Invaild Email Address/Password","login")
        return redirect('/login')
    
    
    session['user_id'] = users.id
    return redirect('/dashboard')



@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id" : session['user_id']
    }
    return render_template("dashboard.html", user=User.find_id(data), all_users=User.get_users())


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


