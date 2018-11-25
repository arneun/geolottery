from datetime import datetime
from country_checker import CountryChecker
from bet import Bet
from database import Database
from flask import jsonify


class BetController:

    def __init__(self):
        self.connection = Database()

    def add_new_bet(self, x_coordinate, y_coordinate, ticket_type, user_id):
        checker = CountryChecker()

        if checker.check_if_in_poland(x_coordinate, y_coordinate):
            new_bet = Bet(x_coordinate, y_coordinate, ticket_type, datetime.now(), user_id)
            self.connection.add_bet(new_bet)
            return jsonify(new_bet.__dict__)

        return None

    def get_user_bets(self, user_id):
        bets = self.connection.get_user_bets(user_id)
        return jsonify(bets)

    def get_bets(self):
        bets = self.connection.get_bets()
        return jsonify(bets)
