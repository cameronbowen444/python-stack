from flask_app import app 
from flask import render_template, redirect, request, session, flash
from flask_app.models import user
from flask_app.models import recipe
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    data = {
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "email" : request.form['email'],
        "password" : bcrypt.generate_password_hash(request.form['password'])
    }
    if not user.User.validate_user(request.form):
        return redirect('/')
    
    user_id = user.User.save(data)
    session['user_id'] = user_id

    return redirect('/dashboard')

@app.route('/login', methods=['POST'])
def login():
    
    users = user.User.get_email(request.form)

    if not users:
        flash('Invalid Email/Password')
        return redirect('/')
    if not bcrypt.check_password_hash(users.password, request.form['password']):
        flash('Invaild Email/Password')
        return redirect('/')
    
    session['user_id'] = users.id

    return redirect('/dashboard')

@app.route('/dashboard')
def dash():
    if 'user_id' not in session:
        return redirect('/logout')
    return render_template('dashboard.html', recipe=recipe.Recipe.get_recipes_with_users())


@app.route('/show')
def show():

    if 'user_id' not in session:
        return redirect('/logout')
    return render_template('recipes.html')


@app.route('/edit')
def edit():

    if 'user_id' not in session:
        return redirect('/logout')
    return render_template('edit.html')


@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect('/')