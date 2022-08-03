from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.message import Message
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/create', methods=['POST'])
def created_message():
    data = {
        "content" : request.form['content'],
        "location": request.form['location'],
        "user_id" : session['user_id']
    }
    Message.save(data)
    return redirect('/dashboard')