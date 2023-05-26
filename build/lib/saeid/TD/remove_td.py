import re
import sqlite3

from datetime import datetime
from pathlib import *

path_database = Path(__file__).parent
DATABASE = Path(path_database, 'td_hours.db')

def get_command_args():

    date = ""
    while not date:
        date = input("Date you want to be removed ('%Y-%m-%d'):\n")
        if date == "":
            print("Oops! No value entered")

    return date

def remove_td(
    date: str,
    database=DATABASE,
) -> bool:
    
    correct_date = datetime.strptime(date, '%Y-%m-%d').strftime("%Y/%m/%d") 
    try:
        connect = sqlite3.connect(database)

        c = connect.cursor()
    
        with connect:
            c.execute("DELETE FROM td_hours WHERE :date", 
                    {
                        "date": correct_date,
                    })
        return True
    except Exception as e:
        return False



def run() -> bool:
    DATE = get_command_args()
    return remove_td(date = DATE)


def main():
    if run():
        print("Requested date was removed from the database")
    else:
        print("Something went wrong with updating the database!")


if __name__ == "__main__":
    main()

