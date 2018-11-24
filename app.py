from flask import Flask, session, request
import os


app = Flask(__name__)


@app.route('/register')
def registration(userName, password):
    pass

@app.route('/ticket')
def bet(x_coordinate, y_coordinate, ticket_type):
    pass

@app.route('/prices')
def prices():
    pass



