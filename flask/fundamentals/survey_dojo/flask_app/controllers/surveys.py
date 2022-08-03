from flask_app import app
from flask import render_template, request, redirect, session, url_for
from flask_app.models import survey

@app.route('/')
def index():
    return render_template("survey.html")

@app.route('/users', methods=['POST'])
def users():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['lang'] = request.form['lang']
    session['comment'] = request.form['comment']

    if not survey.Survey.valid_survey(request.form):
        return redirect('/')
    else:
        survey.Survey.save(request.form)
    return redirect('/results')

@app.route('/results')
def result():
    return render_template("results.html")
