from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import email

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/email', methods=['POST'])
def emails():
    if not email.Email.validated_email(request.form):
        return redirect('/')
    else:
        email.Email.save(request.form)
    return redirect('/success')


@app.route('/success')
def success():
    return render_template('success.html',emails=email.Email.get_all())