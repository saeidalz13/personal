import re
import sqlite3

from datetime import datetime
from pathlib import *

path_database = Path(__file__).parent
DATABASE = Path(path_database, 'td_hours.db')


def main(database=DATABASE):
    try:
        connect = sqlite3.connect(database)

        c = connect.cursor()
    
        with connect:
            c.execute("SELECT SUM(hours) FROM td_hours")
            print(c.fetchone()[0])
        return True
    except Exception as e:
        return False


if __name__ == "__main__":
    main()
