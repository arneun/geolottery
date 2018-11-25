from database import Database
from prize import Prizes
from flask import Response
import json

class PrizeController:

    def __init__(self):
        self.connection = Database()

    def get_prizes(self):
        prizes = self.connection.get_prizes()
        return Response(json.dumps(prizes),  mimetype='application/json')
        





