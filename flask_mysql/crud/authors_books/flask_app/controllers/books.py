from flask import render_template, redirect, request
from flask_app import app
from flask_app.models import author, book


@app.route('/books')
def books():
    books = book.Book.get_all()
    return render_template('books.html',books=books)


@app.route('/addbook', methods=['POST'])
def add_book():
    book.Book.addbook(request.form)
    return redirect('/books')


@app.route('/book/<int:id>')
def showbook(id):
    data = {
        "id" : id
    }
    return render_template('bookshow.html',books=book.Book.get_fav_book(data), authors=author.Author.get_authors())


@app.route('/addauthor', methods=['POST'])
def add_author():
    data = {
        "author_id" : request.form['author_id'],
        "book_id" : request.form['book_id']
    }
    author.Author.add_favorite(data)
    return redirect(f"/book/{request.form['book_id']}")