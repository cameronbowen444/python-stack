from flask_app import app 
from flask import render_template, request, redirect, session, flash
from flask_app.models import user, show
from flask_bcrypt import Bcrypt 
bcrypt = Bcrypt(app) 


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():

    if not user.User.vaildate_form(request.form):
        return redirect('/')
    
    data = {
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "email" : request.form['email'],
        "password" : bcrypt.generate_password_hash(request.form['password'])
    }
    id = user.User.save(data)

    session['user_id'] = id
    return redirect('/dashboard')


@app.route('/login', methods=['POST'])
def login():
    data = {
        "email" : request.form['email']
    }
    user_in_db = user.User.get_email(data)

    if not user_in_db:
        flash("Invaild Email/Password", 'login')
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invaild Email/Password", 'login')
        return redirect('/')

    session['user_id'] = user_in_db.id
    return redirect('/dashboard')

@app.route('/dashboard')
def dash():

    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id' : session['user_id']
    }
    return render_template('dashboard.html',user=user.User.get_id(data), shows=show.Show.get_shows_with_user())


@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect('/')