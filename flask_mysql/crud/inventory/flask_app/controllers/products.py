from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.product import Product

@app.route('/')
def index():
    items = Product.get_all()
    print(items)
    return render_template('index.html', all_items=items)


@app.route('/new')
def addnew():
    return render_template('new.html')


@app.route('/create', methods=['POST'])
def add():
    data = {
        "name" : request.form['name'],
        "cost" : request.form['cost'],
        "retail" : request.form['retail']
    }
    Product.new(data)
    return redirect('/')


@app.route('/edit/<int:id>')
def edititem(id):
    data = {
        "id" : id
    }
    return render_template('edit.html',item=Product.show_one(data))


@app.route('/update', methods=['POST', 'GET'])
def updateitem():
    Product.update(request.form)
    return redirect('/')


@app.route('/show/<int:id>')
def showitem(id):
    data = {
        "id" : id
    }
    return render_template('show.html',item=Product.show_one(data))

@app.route('/delete/<int:id>')
def deleteitem(id):
    data = {
        "id" : id
    }
    Product.delete(data)
    return redirect('/')