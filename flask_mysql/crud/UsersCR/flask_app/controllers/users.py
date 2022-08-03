from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.user import User


@app.route('/')
def index():
    users = User.get_users()
    print(users)
    return render_template('read.html',users=users)


@app.route('/create_user', methods=["POST"])
def create():
    data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    User.add_users(data)
    return redirect('/')


@app.route('/create')
def read():
    users = User.get_users()
    print(users)
    return render_template('create.html', users=users)


@app.route('/show/<int:id>')
def show(id):
    data = {
        "id" : id
    }
    users = User.show_user(data)
    print(users)
    return render_template('show.html',users=users)


@app.route('/edit/<int:id>')
def edit(id):
    data = {
        "id" : id
    }
    users = User.show_user(data)
    print(users)
    return render_template('edit.html',users=users)

@app.route('/update_user', methods=['POST'])
def updating():
    User.update(request.form)
    return redirect('/')


@app.route('/delete/<int:id>')
def delete_(id):
    data = {
        "id" : id
    }
    User.delete_user(data)
    return redirect('/')

