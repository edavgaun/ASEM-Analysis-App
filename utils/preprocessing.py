import pandas as pd
import os

def load_data_full():
    url = "Data/data_full.csv"
    return pd.read_csv(url, index_col=0)

def load_df_long():
    url = "Data/df_long.csv"
    return pd.read_csv(url)

def load_dfs():
    dfs = {}
    for year in range(2015, 2025):
        url = f"Data/CP_{year}.csv"
        dfs[year] = pd.read_csv(url)
    return dfs
