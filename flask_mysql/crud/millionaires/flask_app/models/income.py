from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import millionaire

class Income:
    db = "millionaires"
    def __init__(self, data):
        self.id = data['id']
        self.yearly = data['yearly']
        self.type = data['type']
        self.company = data['company']
        self.millionares_id = data['millionaires_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod 
    def addsource(cls, data):
        query = "INSERT INTO income (yearly, type, company, millionaires_id, created_at, updated_at) VALUES (%(yearly)s, %(type)s, %(company)s, %(millionaires_id)s, NOW(), NOW());"
        return connectToMySQL(cls.db).query_db(query, data)