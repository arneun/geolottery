from database import Database
from distance_calculator import Calculator


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
