from flask import render_template, redirect, request
from flask_app import app
from flask_app.models import author, book

@app.route('/')
def index():
    return redirect('/authors')

@app.route('/authors')
def authors():
    return render_template('authors.html', all_authors=author.Author.get_authors())


@app.route('/author/<int:id>')
def showauthor(id):
    data = {
        "id" : id
    }
    return render_template('authorshow.html',authors=author.Author.favorites(data), books=book.Book.get_all())


@app.route('/add', methods=['POST'])
def addbook():
    data = {
        "author_id" : request.form['author_id'],
        "book_id" : request.form['book_id']
    }
    author.Author.add_favorite(data)
    return redirect(f"/author/{request.form['author_id']}")



@app.route('/newauthor', methods=['POST'])
def savethis():
    author.Author.save(request.form)
    return redirect('/')

