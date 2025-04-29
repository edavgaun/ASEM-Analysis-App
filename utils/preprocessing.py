import pandas as pd
import os

def load_data_full():
    url = "https://raw.githubusercontent.com/edavgaun/ASEM-Analysis-App/main/Data/data_full.csv"
    return pd.read_csv(url, index_col=0)

def load_df_long():
    url = "https://raw.githubusercontent.com/edavgaun/ASEM-Analysis-App/main/Data/df_long.csv"
    return pd.read_csv(url)

def load_bow_dfs():
    bow_dfs = {}
    for year in range(2015, 2025):
        url = f"https://raw.githubusercontent.com/edavgaun/ASEM-Analysis-App/main/Data/bow_df_{year}.csv"
        bow_dfs[year] = pd.read_csv(url)
    return bow_dfs

def load_dfs():
    dfs = {}
    for year in range(2015, 2025):
        url = f"https://raw.githubusercontent.com/edavgaun/ASEM-Analysis-App/main/Data/df_{year}.csv"
        dfs[year] = pd.read_csv(url)
    return dfs
