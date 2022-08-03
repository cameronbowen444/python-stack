from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []


    @classmethod
    def newdojos(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
        return connectToMySQL('dojos_ninjas').query_db(query,data)

    @classmethod
    def getdojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_ninjas').query_db(query)
        
        all_dojos = []

        for dojos in results:
            all_dojos.append( cls(dojos) )
        return all_dojos

    @classmethod
    def showdojo(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojos_id = dojos.id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_ninjas').query_db(query, data)

        all_dojos = cls( results[0] )
        for row in results:

            ninja_data = {
                "id" : row['ninjas.id'],
                "first_name" : row['first_name'],
                "last_name" : row['last_name'],
                "age" : row['age'],
                "created_at" : row['created_at'],
                "updated_at" : row['updated_at']
            }
            all_dojos.ninjas.append( ninja.Ninja( ninja_data ))
        return all_dojos
