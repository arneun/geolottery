from price import Price
from database import Database
from flask import jsonify

class PriceController:

    def __init__(self):
        self.connection = Database()

    def get_prices(self):
        prices = self.connection.get_prices()
        return jsonify(prices.__dict__)
