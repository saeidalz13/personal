import pandas as pd
import re
from pathlib import Path
from datetime import datetime


PATH_DATABASE = Path(__file__)
DATABASE = Path(PATH_DATABASE.parent, "TD_Hours.xlsx")


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
    df = pd.read_excel(database)
    new_df = pd.DataFrame()
    new_df["Date"] = [pd.to_datetime(datetime.today()).strftime("%Y/%m/%d")]
    new_df["Hours"] = [hours]
    new_df["Task Done"] = [task_done]

    try:
        df = pd.concat([df, new_df], axis="rows", ignore_index=True)
        df.drop_duplicates("Date", keep="last", inplace=True)
        df.to_excel(database, sheet_name="TD", index=False, header=True)
        return True
    except Exception as e:
        print(f"Error occurred! {e}")
        return False


def run() -> bool:
    HOURS, TASK_DONE = get_command_args()
    return add_td(hours=HOURS, task_done=TASK_DONE)


def main():
    if run():
        print("TD hours CSV was succesfully updated!")
    else:
        print("Something went wrong with updating the CSV file")


if __name__ == "__main__":
    main()
