
import sqlite3
from user import User
from bet import Bet

class Database:

    def setup(self):
        conn = sqlite3.connect('/home/.geolottery_storage')
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
        res = c.fetchall()
        conn.commit()
        conn.close()

        return User(res[0], res[1], res[2])
        
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
        c.execute('''INSERT INTO bets (id, latitude, longitude,ticket_type,timestamp ,user_id) VALUES (?,?,?,?,?)''', (get_newest_bet()+1, bet.latitude, bet.longitude, bet.ticket_type, bet.timestamp, bet.user))
        conn.commit()
        conn.close()
    

    def add_user(self, user):
        conn = sqlite3.connect('/home/.geolottery_storage')
        c = conn.cursor()
        c.execute('''INSERT INTO users (numer, name, email, password ) VALUES (?,?,?,?)''', (get_newest_user() +1, user.name, user.email, user.password))
        conn.commit()
        conn.close()
    


