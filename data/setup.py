
import sqlite3
from user.user import User


class Database:

    def setup(self):
        conn = sqlite3.connect('/home/.geolottery_storage')
        c = conn.cursor()
        c.execute('''CREATE TABLE user (name text, mail text, password text) ''')
        conn.commit()
        c.execute('''CREATE TABLE prices (size integer, price integer)''')
        conn.commit()
        
        c.execute('''CREATE TABLE prizes (lottery_time text, prize integer ) '''  )
        conn.commit()

        conn.close()
    
    def authenticate(self, user_name, user_password):
        conn = sqlite3.connect('/home/.geolottery_storage')
        c = conn.cursor()
        c.execute('''SELECT name, FROM user WHERE name=? AND mail=? ''', (user_name, user_password) )
        res = c.fetchall()
        conn.commit()
        conn.close()

        return User(res[0], res[1], res[2])
        


