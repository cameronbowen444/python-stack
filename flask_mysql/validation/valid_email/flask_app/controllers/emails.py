from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import email

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/addme', methods=['POST'])
def adding():
    if not email.User.validate_user(request.form):
        return redirect('/')
    email.User.save(request.form)
    return redirect('/result')


@app.route('/result')
def result():
    return render_template('results.html', user=email.User.get_last())