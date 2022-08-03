from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import message
from flask import flash 
import re 

class User:
    def __init__(self, data):
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = ddata['created_at']
        self.updated_at = data['updated_at']
        self.messages = []
