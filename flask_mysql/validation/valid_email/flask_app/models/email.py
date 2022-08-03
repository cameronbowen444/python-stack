from flask_app.config.mysqlconnection import connectToMySQL 
from flask import flash 
import re 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 


class User:
    db = "valid_email"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod 
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, age, email, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(email)s, NOW(), NOW());"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_last(cls):
        query = "SELECT * FROM users ORDER BY id DESC LIMIT 1;"
        results = connectToMySQL(cls.db).query_db(query)

        users = []
        for user in results:
            users.append(cls(user))
        return users


    @staticmethod
    def validate_user(user):
        is_valid = True
        if len(user['first_name']) < 3:
            flash('Name must be at least 3 characters!')
            is_valid = False
        if len(user['last_name']) < 3:
            flash('Last name must be at least 3 characters!')
            is_valid = False
        if user['age'] == "":
            flash('Age must be inserted!')
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invaild Email Address")
            is_valid = False
        return is_valid