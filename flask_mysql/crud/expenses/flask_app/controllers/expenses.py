from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.expense import Expense 

@app.route('/')
def main():
    return render_template('main.html',expenses=Expense.get_all())

@app.route('/create')
def create():
    return render_template('add.html')

@app.route('/new', methods=['POST'])
def adding():
    Expense.save(request.form)
    return redirect('/')

@app.route('/show/<int:id>')
def show(id):
    data = {
        "id" : id
    }
    return render_template('show.html', expense=Expense.get_one(data))

@app.route('/edit/<int:id>')
def edit(id):
    data = {
        "id" : id
    }
    return render_template('edit.html', expense=Expense.get_one(data))

@app.route('/update', methods=['POST'])
def updating():
    Expense.update(request.form)
    return redirect('/')

@app.route('/delete/<int:id>')
def deleting(id):
    data = {
        "id" : id
    }
    Expense.delete(data)
    return redirect('/')