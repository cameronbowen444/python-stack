from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.user import User
from flask import jsonify

@app.route('/')
def index():
    return render_template('dashboard.html', users=User.get_all())

@app.route('/create', methods=['POST'])
def create():
    data = {
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "email" : request.form['email']
    }
    User.create(data)
    return redirect('/')

@app.route('/add')
def addnew():
    return render_template('main.html')

@app.route('/show/<int:id>')
def showme(id):
    data = {
        "id" : id
    }
    return render_template('show.html', users=User.get_one(data))

@app.route('/edit/<int:id>')
def editme(id):
    data = {
        "id" : id
    }
    return render_template('edit.html', users=User.get_one(data))

@app.route('/delete/<int:id>')
def delete(id):
    data = {
        "id" : id
    }
    User.delete(data)
    return redirect('/')

@app.route('/update', methods=['POST'])
def update():
    User.updating(request.form)
    return redirect('/')

@app.route('/get_data')
def get_data():
    return jsonify(message="Hello World")