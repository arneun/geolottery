from database import Database
from user import User


class UserController:
    
    def __init__(self):
        self.connection = Database()

    def register_user(self, name, email, password):
        user = User(name, email, password)
        self.connection.add_user(user)
        return user

    def authenticate(self, username, password):
        return self.connection.authenticate(username, password)

