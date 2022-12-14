from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash 
import re 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    db = "user_log_reg"
    def __init__(self, data):
        self.id = data['id'] 
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod 
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, age, email, password, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(email)s, %(password)s, NOW(), NOW());"
        return connectToMySQL(cls.db).query_db(query, data)


    @classmethod 
    def get_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        
        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod 
    def get_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result[0]

    @staticmethod
    def validate_user(user):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(User.db).query_db(query, user)
        if len(result) >= 1:
            flash("email is already in use!", 'register')
            is_valid = False
        if len(user['first_name']) < 2:
            flash("First name must be at least 2 characters!", 'register')
            is_valid = False
        if len(user['last_name']) < 2:
            flash("Last name must be at least 2 characters!", 'register')
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email format!", 'register')
            is_valid = False
        if len(user['password']) < 8:
            flash("Password must be at least 8 characters!", 'register')
            is_valid = False
        if user['confirm'] != user['password']:
            flash("Passwords do not match!", 'register')
            is_valid = False
        return is_valid