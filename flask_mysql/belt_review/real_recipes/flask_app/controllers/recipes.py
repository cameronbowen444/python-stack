from flask_app import app 
from flask import render_template, redirect, request, session, flash
from flask_app.models import recipe
from flask_app.models import user


@app.route('/new')
def new():
    if 'user_id' not in session:
        return redirect('/logout')
    return render_template('new.html')


@app.route('/add_recipe', methods=['POST'])
def newrecipe():
    data = {
        "name" : request.form['name'],
        "description" : request.form['description'],
        "instructions" : request.form['instructions'],
        "date" : request.form['date'],
        "under30" : request.form['under30'],
        session['']
    }
    return redirect('/dashboard')