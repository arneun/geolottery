from database import Database
from user import User
from flask import jsonify


class UserController:
    
    def __init__(self):
        self.connection = Database()

    def register_user(self, name, email, password):
        user = User(0, name, email, password)
        user = self.connection.add_user(user)
        return jsonify(user.__dict__)

    def authenticate(self, username, password):
        return jsonify(self.connection.authenticate(username, password))

    def get_user_info(self, user_id):
        return jsonify(self.connection.get_user_info(user_id).__dict__)
