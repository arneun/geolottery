from price import Price
from database import Database
from flask import jsonify

class PriceController:
 
    def get_prices(self):
        prices = self.connection.get_prices()
        return jsonify(prices)
