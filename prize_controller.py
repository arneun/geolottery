from database import Database
from prize import Prizes
from flask import jsonify

class PrizeController:

    def __init__(self):
        self.connection = Database()

    def get_prizes(self):
        prizes = self.connection.get_prizes()
        return jsonify(prizes)
        





