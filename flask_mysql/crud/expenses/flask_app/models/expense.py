from flask_app.config.mysqlconnection import connectToMySQL

class Expense:
    db = "expenses"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.cost = data['cost']
        self.date = data['date']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM expenses;"
        results = connectToMySQL(cls.db).query_db(query)

        expenses = []

        for e in results:
            expenses.append(cls(e))
        return expenses

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM expenses WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        return results[0]


    @classmethod 
    def save(cls,data):
        query = "INSERT INTO expenses (name, cost, date, created_at, updated_at) VALUES (%(name)s, %(cost)s, %(date)s, NOW(), NOW());"
        return connectToMySQL(cls.db).query_db(query, data)

    
    @classmethod 
    def update(cls, data):
        query = "UPDATE expenses SET name=%(name)s, cost=%(cost)s, date=%(date)s, updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod 
    def delete(cls, data):
        query = "DELETE FROM expenses WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)