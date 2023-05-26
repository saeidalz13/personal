import re
import sqlite3

from datetime import datetime
from pathlib import *

path_database = Path(__file__).parent
DATABASE = Path(path_database, 'td_hours.db')


def get_command_args():
    hours = ""
    while not hours or re.findall(r"[,*\-_]", hours):
        hours = input("How many hours of TD:\n")

        if hours == "":
            print("Oops! No value entered for the hours")
        elif re.findall(r"[,*\-_]", hours):
            print("Invalid characters found in entry [* , - _]")

    hours = round(float(hours), 2)
    task_done = ""
    while not task_done:
        task_done = input("Describe the task:\n")
        if task_done == "":
            print("Oops! No value entered")

    return hours, task_done


def add_td(
    hours: float,
    task_done: str,
    database=DATABASE,
) -> bool:
    
    try:
        connect = sqlite3.connect(database)

        c = connect.cursor()
    
        with connect:
            c.execute("INSERT INTO td_hours VALUES (:date, :hours, :desc)", 
                    {
                        "date": datetime.today().strftime("%Y/%m/%d"),
                        "hours": hours,
                        "desc": task_done
                    })
        return True
    except Exception as e:
        return False



def run() -> bool:
    HOURS, TASK_DONE = get_command_args()
    return add_td(hours=HOURS, task_done=TASK_DONE)


def main():
    if run():
        print("Database was sucessfully updated!")
    else:
        print("Something went wrong with updating the database!")


if __name__ == "__main__":
    main()


