import time
from country_checker import CountryChecker
from bet import Bet
from database import Database
import json


class BetController:

    def __init__(self, bet_manager):
        self.bet_manager = bet_manager
        self.connection = Database()

    def add_new_bet(self, x_coordinate, y_coordinate, ticket_type, user_id):
        checker = CountryChecker()

        if checker.check_if_in_poland(x_coordinate, y_coordinate):
            new_bet = Bet(x_coordinate, y_coordinate, ticket_type, time.time(), user_id)
            self.connection.add_bet(new_bet)
            return new_bet

        return None

    def get_bets(self, user_id):
        bets = self.connection.get_bets(user_id)
        return json.dump(bets)
