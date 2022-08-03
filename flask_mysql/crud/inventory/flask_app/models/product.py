from flask_app.config.mysqlconnection import connectToMySQL

class Product:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.cost = data['cost']
        self.retail = data['retail']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM items;"
        results = connectToMySQL('products').query_db(query)
        
        items = []
        
        for item in results:
            items.append( cls(item) )
        return items

    @classmethod
    def new(cls, data):
        query = "INSERT INTO items (name, cost, retail, created_at, updated_at) VALUES (%(name)s, %(cost)s, %(retail)s, NOW(), NOW());"
        return connectToMySQL('products').query_db(query, data)

    @classmethod
    def show_one(cls, data):
        query = "SELECT * FROM items WHERE id = %(id)s;"
        results = connectToMySQL('products').query_db(query,data)
        return cls(results[0])

    @classmethod
    def update(cls, data):
        query = "UPDATE items SET name = %(name)s, cost = %(cost)s, retail = %(retail)s, updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL('products').query_db(query, data)

    @classmethod 
    def delete(cls, data):
        query = "DELETE FROM items WHERE id = %(id)s;"
        return connectToMySQL('products').query_db(query, data)