from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Email:
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validated_email(email):
        is_valid = True
        if not EMAIL_REGEX.match(email['email']):
            flash("Email is NOT valid!", 'error')
            is_valid = False
        if EMAIL_REGEX.match(email['email']):
            flash("Email is Valid, Here is everything below", 'success')
            is_valid = True
        return is_valid

    @classmethod
    def save(cls, data):
        query = "INSERT INTO email (email, created_at, updated_at) VALUES (%(email)s, NOW(), NOW());"
        return connectToMySQL('email').query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM email;"
        results = connectToMySQL('email').query_db(query)

        email = []
        for e in results:
            email.append( cls(e) )
        return email

