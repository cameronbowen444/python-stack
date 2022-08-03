from flask_app import app 
from flask import render_template, request, redirect, session, flash
from flask_app.models import user
from flask_app.models import message
from flask_bcrypt import Bcrypt 


@app.route('/')
def index():
    return render_template('index.html')