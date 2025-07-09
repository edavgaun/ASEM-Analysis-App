import pandas as pd

def get_df(file_year):
    """
    Loads a CSV for the given year from GitHub and builds a 'Paper' column.
    """
    url = f"https://raw.githubusercontent.com/edavgaun/ASEM-Analysis-App/main/Data/CP_{file_year}.csv"
    df = pd.read_csv(url, index_col="Unnamed: 0")

    if file_year != 2015:
        df["Paper"] = (
            df["Title"].str.lower().fillna("") + ", " +
            df["KeyWords"].str.lower().fillna("") + ", " +
            df["Abstract"].str.lower().fillna("")
        )
    else:
        df["Paper"] = (
            df["Title"].str.lower().fillna("") + ", " +
            df["Abstract"].str.lower().fillna("")
        )

    return df
