import sqlite3
from datetime import datetime, timedelta 
import time

from user import User
from bet import Bet
from price import Price
from prize import Prizes


class Database:

    def __init__(self):
        self.storage = 'testDB2.db'

    def setup(self):
        conn = sqlite3.connect(self.storage)
        c = conn.cursor()
        c.execute('''CREATE TABLE users (number integer, name text, mail text, password text) ''')
        conn.commit()
        c.execute('''CREATE TABLE prices (size integer, price integer)''')
        conn.commit()
        
        c.execute('''CREATE TABLE prizes (lottery_time timestamp, prize integer ) '''  )
        conn.commit()
        c.execute('''CREATE TABLE bets (id, latitude real, longitude real, ticket_type integer, timestamp timestamp, user_id integer) ''')
        conn.commit()
        conn.close()
    
    def authenticate(self, user_name, user_password):
        conn = sqlite3.connect(self.storage)
        c = conn.cursor()
        c.execute('''SELECT name, number FROM user WHERE name=? AND mail=? ''', (user_name, user_password) )
        res = c.fetchone()
        conn.commit()
        conn.close()
                
        return res is None

    def get_user_info(self, user_id):
        conn = sqlite3.connect(self.storage)
        c = conn.cursor()
        c.execute('''SELECT name, mail, password FROM users WHERE number=?''', (str(user_id)))
        res = c.fetchone()
        conn.commit()
        conn.close()

        if res is None:
            return User(0, "", "", "")

        return User(user_id, res[0], res[1], res[2]) 

    def get_newest_user(self):
        conn = sqlite3.connect(self.storage)
        c = conn.cursor()
        c.execute('''SELECT * FROM users ORDER BY number DESC''')
        res = c.fetchone()
        conn.commit()
        conn.close()
        
        if res is None:
            return 0
        else:
            return res[0]
    
    def get_newest_bet(self):
        conn = sqlite3.connect(self.storage)
        c = conn.cursor()
        c.execute('''SELECT * FROM bets ORDER BY id''')
        res = c.fetchone()
        conn.commit()
        conn.close()
        if res is None:
            return 0
        else:
            return res[0]

    def add_bet(self, bet):
        conn = sqlite3.connect(self.storage)
        c = conn.cursor()
        c.execute('''INSERT INTO bets (id, latitude, longitude,ticket_type,timestamp ,user_id) VALUES (?,?,?,?,?,?)''', (
            self.get_newest_bet() + 1, bet.latitude, bet.longitude, bet.ticket_type, bet.timestamp.isoformat()[:19], bet.user))
        conn.commit()
        conn.close()

    def add_user(self, user):
        conn = sqlite3.connect(self.storage)
        c = conn.cursor()
        user.id = (self.get_newest_user() + 1)
        print(user.id)
        c.execute('''INSERT INTO users (number, name, mail, password ) VALUES (?,?,?,?)''', (user.id, user.name, user.email, user.password))
        conn.commit()
        
        conn.close()
        return user
        
    def get_prices(self):
        conn = sqlite3.connect(self.storage)
        c = conn.cursor()
        c.execute('''SELECT size, price FROM prices''')
        res = c.fetchall()
        conn.commit()
        conn.close()
        
        result = [] 
        for row in res:
            result.append(Price(row[0], row[1]).__dict__)
        return result

    def get_user_bets(self, user_id):
        conn = sqlite3.connect(self.storage)
        c = conn.cursor()
        c.execute('''SELECT id, latitude, longitude, ticket_type, timestamp FROM bets WHERE user_id = ?''', (user_id) )
        res = c.fetchall()
        conn.commit()
        conn.close()
        
        result = [] 
        for row in res:
            result.append(Bet( row[1], row[2], row[3], row[4], user_id).__dict__ )
        return result

    def get_prizes(self):
        conn = sqlite3.connect(self.storage)
        c = conn.cursor()
        c.execute('''SELECT lottery_time, prize FROM prizes''' )
        res = c.fetchall()
        print(res)
        conn.commit()
        conn.close()
        
        result = [] 
        for row in res:
            result.append(Prizes(datetime.strptime(row[0],'%Y-%m-%dT%H:%M:%S').isoformat(), row[1]).__dict__ )
        return result

    def get_bets(self):
        conn = sqlite3.connect(self.storage)
        c = conn.cursor()
        c.execute('''SELECT id, latitude, longitude, ticket_type, timestamp, user_id FROM bets''')
        res = c.fetchall()
        conn.commit()
        conn.close()
        print(res)
        result = []
        for row in res:
            result.append(Bet(row[1], row[2], row[3], datetime.strptime(row[4],'%Y-%m-%dT%H:%M:%S').isoformat(), row[5] ))
        return result

    def reseed_database(self):
        conn = sqlite3.connect(self.storage)
        c = conn.cursor()

        c.execute('''DELETE FROM users''')
        c.execute('''DELETE FROM prices''')
        c.execute('''DELETE FROM prizes''')
        c.execute('''DELETE FROM bets''')

        c.execute('''INSERT INTO prices ( price, size ) VALUES (?,?)''', ( 2,  1 ) )
        c.execute('''INSERT INTO prices ( price, size ) VALUES (?,?)''', ( 5,  2 ) )
        c.execute('''INSERT INTO prices ( price, size ) VALUES (?,?)''', ( 10, 3 ) )

        c.execute('''INSERT INTO users (number, name, mail, password ) VALUES (?,?,?,?)''', (
1 , 'Andrzej Strzelba', 'user@example.com', 'example') )

        c.execute('''INSERT INTO bets (id, latitude, longitude,ticket_type,timestamp ,user_id) VALUES (?,?,?,?,?,?)''', ( 1, 51.4, 21.166667, 3, datetime.now().isoformat()[:19], self.get_newest_user() ) )

        c.execute('''INSERT INTO prizes ( lottery_time, prize ) VALUES (?,?)''', ( (datetime.now() + timedelta(days=1)).isoformat()[:19], 1666 ) )

        conn.commit()
        conn.close()
