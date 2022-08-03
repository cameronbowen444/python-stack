from flask_app import app
from flask import render_template, request, redirect
from flask_app.models import income
from flask_app.models import millionaire

@app.route('/create')
def make():
    return render_template('source.html', millionaires=millionaire.Millionaire.get_all())

@app.route('/add_source', methods=['POST'])
def adding():
    income.Income.addsource(request.form)
    return redirect('/')