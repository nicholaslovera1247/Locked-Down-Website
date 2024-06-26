import hashlib
import os
import random
import array

MIN_PASSWORD_LENGTH = 8
MAX_PASSWORD_LENGTH = 25

DIGITS = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' ]
LOWER_CASE_CHARS = [ 'a', 'b', 'c', 'd', 'e', 'f',
                    'g', 'h', 'i', 'j', 'k', 'l', 'm',
                    'o', 'p', 'q', 'r', 's', 't', 'u',
                    'v', 'w', 'x', 'y', 'z' ]
UPPER_CASE_CHARS = [ 'A', 'B', 'C', 'D', 'E', 'F',
                    'G', 'H', 'I', 'J', 'K', 'L', 'M',
                    'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                    'V', 'W', 'X', 'Y', 'Z' ]
SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<']




def hash_pw(plain_text, salt='') -> str: #hash_pw function from lab 6

    salt = os.urandom(20).hex()
    hashable = salt + plain_text
    hashable = hashable.encode('utf-8')
    this_hash = hashlib.sha1(hashable).hexdigest()
    return salt + this_hash

def strong_pw(): #strong password function uses concepts from a GeeksForGeeks lesson at: https://www.geeksforgeeks.org/generating-strong-password-using-python/#
    rand_digit = random.choice(DIGITS)
    rand_upper = random.choice(UPPER_CASE_CHARS)
    rand_lower = random.choice(LOWER_CASE_CHARS)
    rand_symbol = random.choice(SYMBOLS)
    temp_password = rand_digit + rand_upper + rand_lower + rand_symbol
    combined_array = DIGITS + LOWER_CASE_CHARS + UPPER_CASE_CHARS + SYMBOLS
    for x in range (MIN_PASSWORD_LENGTH, MAX_PASSWORD_LENGTH - 4):
        temp_password = temp_password + random.choice(combined_array)
        temp_list = array.array('u', temp_password)
        random.shuffle(temp_list)
    password = ""
    for x in temp_list:
        password += x
    return password

def authenticate_password(test_password):  # Password strength function from Lab 2
    if test_password.isalnum() or test_password.isalpha():
        return False
    if len(test_password) < MIN_PASSWORD_LENGTH:
        return False
    if len(test_password) > MAX_PASSWORD_LENGTH:
        return False
    special_char_check = False
    has_upper = False
    has_lower = False
    has_digit = False
    for ch in test_password:
        if ch in SYMBOLS:
            special_char_check = True
        if ch.isupper():
            has_upper = True
        if ch.islower():
            has_lower = True
        if ch.isdigit():
            has_digit = True
    if not special_char_check or \
            not has_upper or \
            not has_lower or \
            not has_digit:
        return False
    else:
        return True
