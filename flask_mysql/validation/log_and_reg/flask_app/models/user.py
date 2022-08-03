from flask_app.config.mysqlconnection import connectToMySQL
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

from flask import flash


class User:
    db = "log_and_reg"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @staticmethod
    def vaildate_registration(user):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(User.db).query_db(query,user)
        if len(results) >= 1:
            flash("Email already taken!!!", "register")
            is_valid = False
        if len(user['first_name']) < 2:
            flash("Name must be at least 2 charcters.", "register")
            is_valid = False
        if len(user['last_name']) < 2:
            flash("Name must be at least 2 characters.", "register")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email address", "register")
            is_valid = False
        if len(user["password"]) < 8:
            flash("password must be at least 8 characters", "register")
            is_valid - False
        if user["password_confirm"] != user['password']:
            flash("password confirmation doesn't match", "register") 
            is_valid = False
        return is_valid


    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());"
        return connectToMySQL('log_and_reg').query_db(query,data)

    
    @classmethod
    def login(cls, data):
        query = "INSERT INTO users (email, password) VALUES (%(email)s, %(password)s);"
        return connectToMySQL('log_and_reg').query_db(query,data)

    @classmethod 
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL('log_and_reg').query_db(query,data)

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        return cls(results[0])

        if len(result) < 1:
            return False
        return cls(result[0])