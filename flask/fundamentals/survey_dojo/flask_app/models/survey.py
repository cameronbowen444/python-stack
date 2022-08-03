from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Survey:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.lang = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @staticmethod 
    def valid_survey(survey):
        is_valid = True
        if survey['name'] < str(3):
            flash("Name must be included and at least 3 characters long to be valid.")
            is_valid = False
        if survey['location'] == "--Select A Location--":
            flash("Must select a location to be valid")
            is_valid = False
        if survey['lang'] == "--Select A Language--":
            flash("Must select a language to be valid")
            is_valid = False
        if survey['comment'] < str(5):
            flash("Comment must be at least 5 characters long to be valid.")
            is_valid - False
        return is_valid

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name, location, language, comment, created_at, updated_at) VALUES (%(name)s, %(location)s, %(lang)s, %(comment)s, NOW(), NOW());"
        return connectToMySQL('dojo_survey').query_db(query,data)