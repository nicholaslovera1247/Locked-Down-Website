'''
Nicholas Lovera
Database module
CS2660 Final Project
'''

import os
import sqlite3
import sys

from passwordsettings import hash_pw

DATABASE = 'user.db'

def delete(username):
    try:
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        c.executemany("DELETE FROM user WHERE username = ?", [(username,),])
        conn.commit()
    except sqlite3.DatabaseError:
        print("Error. Could not retrieve data.")
    finally:
        if c is not None:
            c.close()
        if conn is not None:
            conn.close()


def create_db():
    try:
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        c.execute('''CREATE TABLE user
                 (
                  username text,
                  password text,
                  access_level INTEGER DEFAULT 1,
                  failed_attempts INTEGER DEFAULT 0
                  )''')
        conn.commit()
        return True
    except BaseException:
        return False
    finally:
        if c is not None:
            c.close()
        if conn is not None:
            conn.close()

def add_user(username, password, access_level=1, failed_attempts=0):
    password = hash_pw(password)
    data_to_insert = [(username, password, access_level, failed_attempts)]
    try:
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        c.executemany("INSERT INTO user VALUES (?, ?, ?,?)", data_to_insert)
        conn.commit()
    except sqlite3.IntegrityError:
        print("Error. Tried to add duplicate record!")
    finally:
        if c is not None:
            c.close()
        if conn is not None:
            conn.close()

def query_db(): #query_db function from SQLLite example
    try:
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        for row in c.execute("SELECT * FROM user"):
            print(row)
    except sqlite3.DatabaseError:
        print("Error. Could not retrieve data.")
    finally:
        if c is not None:
            c.close()
        if conn is not None:
            conn.close()
if __name__ == '__main__':
    query_db()


