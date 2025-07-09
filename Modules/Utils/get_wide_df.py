import pandas as pd
import streamlit as st

@st.cache_data
def get_wide_df():
    url = "https://raw.githubusercontent.com/edavgaun/ASEM-Analysis-App/main/Data/data_full.csv"
    df = pd.read_csv(url)
    return df
