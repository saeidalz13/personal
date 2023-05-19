import pandas as pd

FILE = r"C:\Air Quality - Local\01 Career\0000 Personal\saeid\TD\TD_Hours.xlsx"


def read_file(file=FILE):
    df = pd.read_excel(file, sheet_name="TD")

    all_hours = df.loc[:, "Hours"].sum()
    beg_date = df.iloc[0, 0]

    return all_hours, beg_date


def main():
    ALL_HOURS, BEG_DATE = read_file()
    print(f"Since {BEG_DATE}, {ALL_HOURS} hours of TD have been charged\n")


if __name__ == "__main__":
    main()
