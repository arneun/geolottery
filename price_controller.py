import json
# get this object
from flask import Response

from database import Database


class PriceController:

    def __init__(self):
        self.connection = Database()

    def get_prices(self):
        prices = self.connection.get_prices()
        return Response(json.dumps(prices),  mimetype='application/json')
