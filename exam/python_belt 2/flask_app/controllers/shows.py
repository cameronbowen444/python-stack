from flask_app import app 
from flask import render_template, request, redirect, session, flash
from flask_app.models import show
from flask_app.models import user
from flask_bcrypt import Bcrypt 
bcrypt = Bcrypt(app) 


@app.route('/add/<int:id>')
def newshow(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id" : session['user_id']
    }
    return render_template('new.html',user = user.User.get_id(data))


@app.route('/add_show', methods=['POST'])
def addme():
    if 'user_id' not in session:
        return redirect('/logout')

    if not show.Show.validate_show(request.form):
        return redirect("/dashboard")

    data = {
        "title" : request.form['title'],
        "network" : request.form['network'],
        "date" : request.form['date'],
        "description" : request.form['description'],
        "user_id" : session['user_id'],
    } 
    show.Show.save_show(data)
    return redirect('/dashboard')



@app.route('/show/<int:id>')
def showme(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id" : id
    }
    user_data = {
        "id" : session['user_id']
    }
    return render_template('show.html', show=show.Show.get_show(data), user=user.User.get_id(user_data))


@app.route('/edit/<int:id>')
def editme(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id" : id
    }
    user_data = {
        "id" : session['user_id']
    }
    return render_template('edit.html', show=show.Show.get_show(data), user=user.User.get_id(user_data))


@app.route('/update', methods=['POST'])
def updateme():
    if 'user_id' not in session:
        return redirect('/logout')
    
    data_id = {
        "id" : id
    }
    if not show.Show.validate_show(request.form):
        return redirect("/dashboard")
    
    data = {
        "title" : request.form['title'],
        "network" : request.form['network'],
        "date" : request.form['date'],
        "description" : request.form['description'],
        "id" : request.form['id']
    } 
    show.Show.update(data)
    return redirect('/dashboard')

@app.route('/delete/<int:id>')
def deleteme(id):
    data = {
        "id" : id
    }
    show.Show.delete(data)
    return redirect('/dashboard')