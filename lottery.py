from database import Database
from distance_calculator import Calculator
from random import Random
from country_checker import CountryChecker
from user import User

class Lottery:

    def __init__(self):
        self.connection = Database()

    def get_winner(self, winning_latitude, winning_longitude):
        bets = self.connection.get_bets()
        cal = Calculator()

        lowest_bet = None
        smallest_distance = 500.0

        for bet in bets:
            distance = cal.calculate_distance(bet.latitude, bet.longitude, winning_latitude, winning_longitude)
            if distance < smallest_distance:
                smallest_distance = distance
                lowest_bet = bet

        print(lowest_bet.__class__)
        print(smallest_distance.__class__)

        if (lowest_bet.ticket_type == 1 and smallest_distance < 1) or (lowest_bet.ticket_type == 2 and smallest_distance < 2) or (smallest_distance < 3):
            print(lowest_bet.user)
            var = self.connection.get_user_info(lowest_bet.user)
            print(var.__class__)
            return var

        return User(0,"","","")

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
