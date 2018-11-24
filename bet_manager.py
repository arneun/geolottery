import json
import time
import bet 


class BetManager:

    def __init__(self):
        print("Create bet manager")
        self.bets = []

    def register(self, x_coordinate, y_coordinate, ticker_type):
        new_bet = bet.Bet(x_coordinate, y_coordinate, ticker_type, time.time())

        # Add new_bet to list
        self.bets.append(new_bet)

        return new_bet
