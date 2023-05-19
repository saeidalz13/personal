import pandas as pd
from pathlib import Path

DATABASE = Path("database", "TD_Hours.xlsx")


def read_file(database=DATABASE):
    df = pd.read_excel(database, sheet_name="TD")

    all_hours = df.loc[:, "Hours"].sum()
    beg_date = df.iloc[0, 0]

    return all_hours, beg_date


def main():
    ALL_HOURS, BEG_DATE = read_file()
    print(f"Since {BEG_DATE}, {ALL_HOURS} hours of TD have been charged\n")


if __name__ == "__main__":
    main()
