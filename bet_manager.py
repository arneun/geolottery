import json
import time
import bet 
from database import Database

class BetManager:

    def __init__(self):
        print("Create bet manager")
        self.connection = Database()

    def register(self, x_coordinate, y_coordinate, ticker_type):
        new_bet = bet.Bet(x_coordinate, y_coordinate, ticker_type, time.time())

        # Add new_bet to list
        self.connection.add_bet(new_bet)

        return new_bet
