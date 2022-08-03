from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Survey:
    db = "survey"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod 
    def get_last(cls):
        query = "SELECT * FROM survey ORDER BY id DESC LIMIT 1;"
        result = connectToMySQL(cls.db).query_db(query)
        
        info = []

        for i in result:
            info.append(cls(i))
        return info

    @classmethod 
    def save(cls, data):
        query = "INSERT INTO survey (name, location, language, comment, created_at, updated_at) VALUES (%(name)s, %(location)s, %(language)s, %(comment)s, NOW(), NOW());"
        return connectToMySQL(cls.db).query_db(query, data)

    @staticmethod 
    def validate_form(survey):
        is_valid = True
        if len(survey['name']) < 3:
            flash("name must be at least 2 characters")
            is_valid = False
        if survey['location'] == "Select a Location...":
            flash("Must select a location")
            is_valid = False
        if survey['language'] == "Select a Language...":
            flash("Must choose a language")
            is_valid = False
        if len(survey['comment']) < 5:
            flash("Comment must be at least 5 characters")
            is_valid = False
        return is_valid
