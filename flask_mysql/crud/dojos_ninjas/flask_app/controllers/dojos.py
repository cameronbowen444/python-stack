from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route('/')
def indexredirect():
    return redirect('/dojos')


@app.route('/newdojo', methods=['POST'])
def createnew():
    Dojo.newdojos(request.form)
    return redirect('/')


@app.route('/dojos')
def index():
    return render_template('dojos.html', dojos=Dojo.getdojos())


@app.route('/show/<int:id>')
def show(id):
    data = {
        "id" : id
    }
    return render_template('show.html', dojos=Dojo.showdojo(data))