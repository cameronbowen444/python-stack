from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Message:
    db = "private_wall"
    def __init__(self, data):
        self.id = data['id']
        self.content = data['content']
        self.location = data['location']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.creator = None


    @classmethod
    def save(cls, data):
        query = "INSERT INTO messages (content, user_id, created_at, updated_at) VALUES (%(content)s, %(user_id)s, NOW(), NOW());"
        return connectToMySQL(User.db).query_db(query, data)


    @classmethod 
    def get_messages(cls):
        query = "SELECT * FROM messages JOIN users ON messages.user_id = users.id;"
        results = connectToMySQL(User.db).query_db(cls)
        all_messages = []

        for row in results:
            one_message = cls(row)
        
            user_info = {
                "id" : row['users.id'],
                "first_name" : row['first_name'],
                "last_name" : row['last_name'],
                "email" : row['email'],
                "password" : row['password'],
                "created_at" : row['users.created_at'],
                "updated_at" : row['users.updated_at']
            }
            
            user = user.User(user_info)

            one_message.creator = creator
            all_messages.append(one_message)
        return all_messages

