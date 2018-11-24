from flask import Flask, session, request
import os
from user_controller import UserController
from bet_controller import BetController
from database import Database

app = Flask(__name__)


@app.route('/register/<name>/<email>/<password>')
def registration(name, email, password):
    print(name + " " + email + " " + password)
    user_c = UserController()
    return user_c.register_user(name, email, password)

@app.route('/bet', methods=['POST'])
def bet(x_coordinate, y_coordinate, ticket_type, user_id):
    bet_c = BetController()
    return bet_c.add_new_bet(x_coordinate, y_coordinate, ticket_type, user_id)

@app.route('/bet', methods=['GET'])
def bets(user_id):
    bet_c = BetController()
    return bet_c.get_user_bets(user_id)

@app.route('/prices')
def prices():
    pass



