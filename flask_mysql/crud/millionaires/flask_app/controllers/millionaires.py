from flask_app import app
from flask import render_template, request, redirect
from flask_app.models import millionaire
from flask_app.models import income

@app.route('/')
def index():
    return redirect('/millionaires')

@app.route('/millionaires')
def millionaires():
    return render_template('main.html', millionaires=millionaire.Millionaire.get_all())

@app.route('/add_new', methods=['POST'])
def create():
    millionaire.Millionaire.create(request.form)
    return redirect('/')

@app.route('/show/<int:id>')
def showme(id):
    data = {
        "id" : id
    }
    return render_template('show.html',millionaires=millionaire.Millionaire.millionaires_with_income(data))
