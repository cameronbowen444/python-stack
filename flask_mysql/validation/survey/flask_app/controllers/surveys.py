from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import survey

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add', methods=['POST'])
def addcomment():
    if not survey.Survey.validate_form(request.form):
        return redirect('/')
    survey.Survey.save(request.form)
    return redirect('/result')


@app.route('/result')
def result():
    return render_template('result.html', info=survey.Survey.get_last())