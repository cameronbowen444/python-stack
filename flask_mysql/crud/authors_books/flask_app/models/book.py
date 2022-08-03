from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author

class Book:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.with_authors = []


    @classmethod
    def get_fav_book(cls, data):
        query = "SELECT * FROM books LEFT JOIN favorites ON favorites.book_id = books.id LEFT JOIN authors ON authors.id = favorites.author_id WHERE books.id = %(id)s;"
        results = connectToMySQL('books').query_db(query, data)

        book = cls(results[0])
        for row in results:
            author_data = {
                "id" : row['authors.id'],
                "name" : row['name'],
                "created_at" : row['created_at'],
                "updated_at" : row['updated_at']
            }
            book.with_authors.append(author.Author(author_data))
        return book


    @classmethod
    def add_favorite(cls, data):
        query = "INSERT INTO favorites (author_id, book_id) VALUES (%(author_id)s, %(book_id)s);"
        return connectToMySQL('books').query_db(query,data)


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL('books').query_db(query)

        books = []
        for book in results:
            books.append( cls(book) )
        return books


    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM books WHERE id = %(id)s;"
        results = connectToMySQL('books').query_db(query, data)

        books = []
        for book in results:
            books.append(cls(book))
        return books


    @classmethod 
    def addbook(cls, data):
        query = "INSERT INTO books (title, num_of_pages, created_at, updated_at) VALUES (%(title)s, %(num_of_pages)s, NOW(), NOW());"
        return connectToMySQL('books').query_db(query,data)