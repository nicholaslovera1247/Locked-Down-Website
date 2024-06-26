import sqlite3
import database
import hashlib

DATABASE = 'user.db'
MAX_ATTEMPTS = 3



def get_access_level(username):
    try:
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        c.execute('SELECT access_level FROM user WHERE username = ?', (username,))
        access_level = c.fetchone()
        if access_level:
            return access_level[0]
        return None
    except sqlite3.Error as e:
        print(e)
        return None
    finally:
        if c is not None:
            c.close()
        if conn is not None:
            conn.close()
def reset_lock(username):
    try:
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        c.execute('UPDATE user SET failed_attempts = 0 WHERE username = ?', (username,))
        conn.commit()
    except sqlite3.Error as e:
        print(e)
    finally:
        if c is not None:
            c.close()
        if conn is not None:
            conn.close()
def add_lock(username):
    try:
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        c.execute('UPDATE user SET failed_attempts = failed_attempts + 1 WHERE username = ?', (username,))
        conn.commit()
    except sqlite3.Error as e:
        print(e)
    finally:
        if c is not None:
            c.close()
        if conn is not None:
            conn.close()
def check_locked(username) -> bool:
    try:
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        c.execute('SELECT failed_attempts FROM user WHERE username = ?', (username,))
        locked = c.fetchone()
        stored_lock = locked[0]
        return stored_lock >= 3
    except sqlite3.Error as e:
        print(e)
    finally:
        if c is not None:
            c.close()
        if conn is not None:
            conn.close()
def check_username(username)-> bool:
    try:
        conn  = sqlite3.connect(DATABASE)
        c = conn.cursor()

        c.execute('SELECT * FROM user WHERE username = ?', (username,))
        row = c.fetchone()
        return row is not None
    except sqlite3.Error as e:
        print(e)
        return False
    finally:
        if c is not None:
            c.close()
        if conn is not None:
            conn.close()


def check_password(username, plain_text, salt_length=40) -> bool: # takes code from authenticate function from Lab 6
    try:
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()

        c.execute('SELECT password FROM user WHERE username = ?', (username,))
        stored_password = c.fetchone()
        stored = stored_password[0]
    except sqlite3.Error as e:
        print(e)
    finally:
        if c is not None:
            c.close()
        if conn is not None:
            conn.close()
    salt = stored[:salt_length]
    stored_hash = stored[salt_length:]
    hashable = salt + plain_text
    hashable = hashable.encode('utf-8')
    this_hash = hashlib.sha1(hashable).hexdigest()
    return this_hash == stored_hash
