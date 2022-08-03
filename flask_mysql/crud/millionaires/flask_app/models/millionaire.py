from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import income

class Millionaire:
    db = "millionaires"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.income = []
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM millionaires;"
        results = connectToMySQL(cls.db).query_db(query)

        millionaires = []

        for millionaire in results:
            millionaires.append(cls(millionaire))
        return millionaires
    
    @classmethod 
    def millionaires_with_income(cls, data):
        query = "SELECT * FROM millionaires LEFT JOIN income ON millionaires.id = income.millionaires_id WHERE millionaires.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)

        millionaires = cls(results[0])

        for row in results:
            income_data = {
                "id" : row['income.id'],
                "yearly" : row['yearly'],
                "type" : row['type'],
                "company" : row['company'], 
                "millionaires_id" : row['millionaires_id'],
                "created_at" : row['created_at'],
                "updated_at" : row['updated_at']
            }

            millionaires.income.append(income.Income(income_data))
        return millionaires

    @classmethod 
    def create(cls, data):
        query = "INSERT INTO millionaires (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
        return connectToMySQL(cls.db).query_db(query, data)

