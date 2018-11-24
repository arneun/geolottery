import country_checker as country_checker
from bet_manager import BetManager
from flask import abort


class BetController:

    def __init__(self, bet_manager):
        self.bet_manager = bet_manager

    def add_new_bet(self, x_coordinate, y_coordinate, ticket_type):
        checker = country_checker.CountryChecker()

        if checker.check_if_in_poland(x_coordinate, y_coordinate):
            # Here u should register bet here
            return self.bet_manager.register(x_coordinate, y_coordinate, ticket_type)
        return None
