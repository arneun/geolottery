import time
from country_checker import CountryChecker
from bet import Bet
from database import Database


class BetController:

    def __init__(self, bet_manager):
        self.bet_manager = bet_manager
        self.connection = Database()

    def add_new_bet(self, x_coordinate, y_coordinate, ticket_type):
        checker = CountryChecker()

        if checker.check_if_in_poland(x_coordinate, y_coordinate):
            new_bet = Bet(x_coordinate, y_coordinate, ticket_type, time.time())
            self.connection.add_bet(new_bet)
            return new_bet

        return None
