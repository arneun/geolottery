from flask import Flask, session, request, jsonify
import os
from user_controller import UserController
from bet_controller import BetController
from database import Database
from price_controller import PriceController
from prize_controller import PrizeController
from flask_cors import CORS
from lottery import Lottery


app = Flask(__name__)
CORS(app)

@app.route('/user/register/<name>/<email>/<password>')
def registration(name, email, password):
    print(name + " " + email + " " + password)
    user_c = UserController()
    return user_c.register_user(name, email, password)


@app.route('/user/<user_id>')
def user_info(user_id):
    user_c = UserController()
    return user_c.get_user_info(user_id)


@app.route('/auth/<login>/<password>')
def auth(login, password):
    user_c = UserController()
    return user_c.authenticate(login, password)


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


@app.route('/winner')
def winner():
    lot = Lottery()
    winning = lot.generate_random_coordinates()
    win_user = lot.get_winner(winning[0], winning[1])
    if win_user is None:
        return jsonify(User(0, "", "", "").__dict__)
    return jsonify(win_user.__dict__)


@app.route('/defwinner')
def def_winner():
    bet_c = BetController()
    bet_c.add_new_bet(51.107548, 17.061917, 3, 2)
    lot = Lottery()
    win_user = lot.get_winner(51.110809, 17.064131)
    print(win_user)
    return jsonify(win_user.__dict__)
