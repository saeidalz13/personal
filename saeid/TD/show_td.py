import re
import sqlite3

from datetime import datetime
from pathlib import *

path_database = Path(__file__).parent
DATABASE = Path(path_database, "td_hours.db")


def show_td(database=DATABASE):
    try:
        connect = sqlite3.connect(database)

        c = connect.cursor()

        with connect:
            result = c.execute(
                "SELECT SUM(hours) AS total_hours, MIN(date) AS beg_date FROM td_hours"
            ).fetchone()

        return result
    except Exception as e:
        return False


def main():
    RESULT = show_td()
    print(f"Since {RESULT[1]}, {RESULT[0]} hours have been charged.")


if __name__ == "__main__":
    main()
