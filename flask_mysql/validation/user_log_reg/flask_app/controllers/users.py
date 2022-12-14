from flask_app import app 
from flask import render_template, redirect, request, session, flash
from flask_app.models import user
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def registering():

    if not user.User.validate_user(request.form):
        return redirect('/')

    data = {
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "age" : request.form['age'],
        "email" : request.form['email'],
        "password" : bcrypt.generate_password_hash(request.form['password'])
    }
    
    user_id = user.User.save(data)

    session['user_id'] = user_id
    return redirect('/dashboard')


@app.route('/login', methods=['POST'])
def loginuser():
    user_in_db = user.User.get_email(request.form)

    if not user_in_db:
        flash("Invaild Email/Password", 'login')
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Email/Password", 'login')
        return redirect('/')

    session['user_id'] = user_in_db.id
    return redirect('/dashboard')



@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect ('/logout')
    data = {
        'id' : session['user_id']
    }
    return render_template('dashboard.html', user = user.User.get_id(data))

@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect('/')