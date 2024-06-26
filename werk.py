"""
Werkzeug launcher for application
Nicholas Lovera
CS2660 Final
Program taken from Catcoin Community Bank
"""

import traceback

from app import app

if __name__ == '__main__':

    # pylint: disable=W0703
    try:
        app.run(debug=app.debug, host='localhost', port=8097)
    except Exception as err:
        traceback.print_exc()

