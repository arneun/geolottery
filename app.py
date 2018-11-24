from flask import Flask, session, request
import os
from user_controller import UserController
from bet_controller import BetController
from database import Database
from price_controller import PriceController
from prize_controller import PrizeController

app = Flask(__name__)


@app.route('/user/register/<name>/<email>/<password>')
def registration(name, email, password):
    print(name + " " + email + " " + password)
    user_c = UserController()
    return user_c.register_user(name, email, password)


@app.route('/user/<user_id>')
def user_info(user_id):
    user_c = UserController()
    return user_c.get_user_info(user_id)


@app.route('/bet/<x_coordinate>/<y_coordinate>/<ticket_type>/<user_id>', methods=['POST'])
def bet(x_coordinate, y_coordinate, ticket_type, user_id):
    bet_c = BetController()
    return bet_c.add_new_bet(x_coordinate, y_coordinate, ticket_type, user_id)


@app.route('/bets/<user_id>', methods=['GET'])
def bets(user_id):
    bet_c = BetController()
    return bet_c.get_user_bets(user_id)


@app.route('/prices')
def prices():
    price_c = PriceController()
    return price_c.get_prices()


@app.route('/prizes')
def prizes():
    prize_c = PrizeController()
    return prize_c.get_prizes()
