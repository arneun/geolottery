from database import Database
from distance_calculator import Calculator
from random import Random
from country_checker import CountryChecker


class Lottery:

    def __init__(self):
        self.connection = Database()

    def get_winner(self, winning_latitude, winning_longitude):
        bets = self.connection.get_bets()
        cal = Calculator()

        lowest_bet = None
        smallest_distance = None

        for bet in bets:
            distance = cal.calculate_distance(bet.latitude, bet.longitude, winning_latitude, winning_longitude)
            if distance < smallest_distance:
                smallest_distance = distance
                lowest_bet = bet

        if (lowest_bet.ticket_type == 1 and smallest_distance < 1) or (lowest_bet.ticket_type == 2 and smallest_distance < 2) or (smallest_distance < 3):
            return lowest_bet

        return None

    def generate_random_coordinates(self):
        minN = 49.00
        maxN = 54.50
        minE = 14.7
        maxE = 27.09
        r = Random()
        random_latitude = minN + (maxN - minN) * r.random()
        random_longitude = minE + (maxE - minE) * r.random()

        c = CountryChecker()
        if c.check_if_in_poland(random_latitude, random_longitude):
            return random_latitude, random_longitude
        return self.generate_random_coordinates()
