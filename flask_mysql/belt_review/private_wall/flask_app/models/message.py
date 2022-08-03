from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
from flask import flash 
import re 

class Message:
    def __init__(self, data):
        self.id = data['id']
        self.content = data['content']
        self.user_id = data['user_id']
        self.friend_id = data['friend_id']
        self.created_at = ddata['created_at']
        self.updated_at = data['updated_at']
        self.creator = None

    
