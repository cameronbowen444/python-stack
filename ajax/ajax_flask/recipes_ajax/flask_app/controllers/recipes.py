from flask_app import app 
from flask import render_template, jsonify, request, redirect, session, flash
from flask_app.models import recipe, user
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)



@app.route('/new_recipe', methods=['POST'])
def new():
    if 'user_id' not in session:
        return redirect('/logout')
    if not recipe.Recipe.validate_recipe(request.form):
        return redirect('/dashboard')
    data = {
        "name": request.form["name"],
        "description": request.form["description"],
        "instructions": request.form["instructions"],
        "under30": int(request.form["under30"]),
        "date": request.form["date"],
        "user_id": session["user_id"]
    }
    recipe.Recipe.save(data)
    return redirect('/dashboard')


@app.route('/dashboard/<int:id>')
def show_recipe(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id" : id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("show.html", user=user.User.get_id(user_data), recipe=recipe.Recipe.get_one(data))


@app.route('/update', methods=['POST'])
def updated():
    if 'user_id' not in session:
        return redirect('/logout')
    if not recipe.Recipe.validate_recipe(request.form):
        return redirect(request.referrer)
    data = {
        "name" : request.form["name"],
        "description" : request.form["description"],
        "instructions" : request.form["instructions"],
        "under30": int(request.form["under30"]),
        "date" : request.form["date"],
        "id" : request.form["id"]
    }
    recipe.Recipe.update(data)
    return redirect('/dashboard')

@app.route('/delete/<int:id>')
def destroy(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    recipe.Recipe.delete(data)
    return redirect('/dashboard')