from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
from flask import flash
import re

class Recipe:
    db = "real_recipes"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date = data['date']
        self.under30 = data['under30']
        self.user_recipe = data['user_id']
        self.created_at = data['created_at']
        self.updated_at - data['updated_at']
        self.creator = None

    @staticmethod
    def validate_recipe(recipe):
        is_valid = True
        if len(recipe['name']) < 3:
            flash('name must be at least 3 characters')
            is_valid = False



    @classmethod
    def save_recipe(cls, data):
        query = "INSERT INTO recipes (name, description, instructions, date, under30, user_id, created_at, updated_at) VALUES (%(name)s, %(description)s, %(instructions)s, %(date)s, %(under30)s, %(user_recipe)s, NOW(), NOW());"
        return connectToMySQL(cls.db).query_db(query, data)


    @classmethod 
    def get_recipes_with_users(cls):
        query = "SELECT * FROM recipes LEFT JOIN users ON recipes.user_id = users.id;"
        results = connectToMySQL(cls.db).query_db(query)

        all_recipes = []
        for row in results:
            one_recipe = cls(row)
            user_info = {
                "id" : row['users.id'],
                "first_name": row['first_name'],
                "last_name": row['last_name'],
                "email": row['email'],
                "password": row['password'],
                "created_at": row['users.created_at'],
                "updated_at": row['users.updated_at']
            }

            user = user.User(user_info)

            one_recipe.creator = user

            all_recipes.appen(one_recipe)
        return all_recipes