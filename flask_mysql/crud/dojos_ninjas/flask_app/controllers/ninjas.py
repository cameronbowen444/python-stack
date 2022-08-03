from flask import render_template,redirect,request
from flask_app import app
from flask_app.models import dojo, ninja

@app.route('/ninjas')
def ninjas():

    return render_template('ninjas.html', all_dojos=dojo.Dojo.getdojos())


@app.route('/newninja', methods=["POST"])
def addnew():
    ninja.Ninja.save(request.form)
    return redirect('/')