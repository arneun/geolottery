
import sqlite3
from user import User
from bet import Bet
from price import Price


class Database:

    def setup(self):
        conn = sqlite3.connect("/home/.geolottery_storage")
        c = conn.cursor()
        c.execute('''CREATE TABLE user (number integer, name text, mail text, password text) ''')
        conn.commit()
        c.execute('''CREATE TABLE prices (size integer, price integer)''')
        conn.commit()
        
        c.execute('''CREATE TABLE prizes (lottery_time text, prize integer ) '''  )
        conn.commit()
        c.execute('''CREATE TABLE bets (id, latitude real, longtitude real, ticket_type integer, timestamp text, user_id integer) ''')
        conn.commit()
        conn.close()
    
    def authenticate(self, user_name, user_password):
        conn = sqlite3.connect('/home/.geolottery_storage')
        c = conn.cursor()
        c.execute('''SELECT name, number FROM user WHERE name=? AND mail=? ''', (user_name, user_password) )
        res = c.fetchone()
        conn.commit()
        conn.close()
                
        return res is None
        
    def get_newest_user(self):
        conn = sqlite3.connect('/home/.geolottery_storage')
        c = conn.cursor()
        c.execute('''SELECT MAX(number) FROM user''')
        res = c.fetchall()
        conn.commit()
        conn.close()
        return res[0]
    
    def get_newest_bet(self):
        conn = sqlite3.connect('/home/.geolottery_storage')
        c = conn.cursor()
        c.execute('''SELECT MAX(id) FROM bets''')
        res = c.fetchall()
        conn.commit()
        conn.close()
        return res[0]

    def add_bet(self, bet):
        conn = sqlite3.connect('/home/.geolottery_storage')
        c = conn.cursor()
        c.execute('''INSERT INTO bets (id, latitude, longitude,ticket_type,timestamp ,user_id) VALUES (?,?,?,?,?)''', (
        self.get_newest_bet() + 1, bet.latitude, bet.longitude, bet.ticket_type, bet.timestamp, bet.user))
        conn.commit()
        conn.close()

    def add_user(self, user):
        conn = sqlite3.connect('/home/.geolottery_storage')
        c = conn.cursor()
        c.execute('''INSERT INTO users (numer, name, email, password ) VALUES (?,?,?,?)''', (self.get_newest_user() + 1, user.name, user.email, user.password))
        conn.commit()
        conn.close()
        
    def get_prices(self):
        conn = sqlite3.connect('/home/.geolottery_storage')
        c = conn.cursor()
        c.execute('''SELECT (size, price) FROM prices''' )
        res = c.fetchall()
        conn.commit()
        conn.close()
        
        result = [] 
        for row in res:
            result.append(Price(row[0], row[1]) )
        return result

    def get_user_bets(self, user_id):
        conn = sqlite3.connect('/home/.geolottery_storage')
        c = conn.cursor()
        c.execute('''SELECT (id, latitude, longitude, ticket_type, timestamp) FROM bets WHERE user_id = ?''' (user_id) )
        res = c.fetchall()
        conn.commit()
        conn.close()
        
        result = [] 
        for row in res:
            result.append(Bet( row[1], row[2], row[3], row[4], user_id) )
        return result

    def get_bets(self):
        conn = sqlite3.connect('/home/.geolottery_storage')
        c = conn.cursor()
        c.execute('''SELECT (id, latitude, longitude, ticket_type, timestamp) FROM bets''')
        res = c.fetchall()
        conn.commit()
        conn.close()

        result = []
        for row in res:
            result.append(Bet(row[1], row[2], row[3], row[4]))
        return result
