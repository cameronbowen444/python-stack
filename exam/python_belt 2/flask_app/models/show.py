from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user, show
from flask import flash 
import re 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Show:
    db = "belt_exam"
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.network = data['network']
        self.date = data['date']
        self.description = data['description']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.creator = None


    @staticmethod
    def validate_show(show):
        is_valid = True 
        if len(show['title']) < 3:
            flash("Title must be at least 3 characters!", 'show')
            is_valid = False
        if len(show['network']) < 3:
            flash("Network must be at least 3 characters!", 'show')
            is_valid = False
        if len(show['description']) < 3:
            flash("Description must be at least 3 characters!", 'show')
            is_valid = False
        if show['date'] == "":
            flash("Please enter a date!", 'show')
            is_valid = False
        return is_valid


    @classmethod 
    def get_shows_with_user(cls):
        query = "SELECT * FROM shows LEFT JOIN users ON shows.user_id = users.id;"
        results = connectToMySQL(cls.db).query_db(query)
        all_shows = []

        for row in results:
            one_show = cls(row)
            one_show_author_info = {
                "id" : row['users.id'],
                "first_name" : row['first_name'],
                "last_name" : row['last_name'],
                "email" : row['email'],
                "password" : row['password'],
                "created_at" : row['created_at'],
                "updated_at" : row['updated_at']
            }
            
            author = user.User(one_show_author_info)

            one_show.creator = author

            all_shows.append(one_show)
        return all_shows
        

    @classmethod 
    def save_show(cls, data):
        query = "INSERT INTO shows (title, network, date, description, user_id, created_at, updated_at) VALUES (%(title)s, %(network)s, %(date)s, %(description)s, %(user_id)s, NOW(), NOW());"
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def get_show(cls, data):
        query = "SELECT * FROM shows WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        return cls(results[0])


    @classmethod 
    def update(cls, data):
        query = "UPDATE shows SET title=%(title)s, network=%(network)s, date=%(date)s, description=%(description)s, updated_at=NOW() WHERE id=%(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM shows WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)