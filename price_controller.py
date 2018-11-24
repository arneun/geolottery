from price import Price
from database import Database

class PriceController:

    def __init__(self, price_manager):
        self.price_manager = price_manager
        self.connection = Database()

    def price(self):
        return self.price
   
   def size(self):
        return self.size

