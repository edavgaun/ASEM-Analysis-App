import streamlit as st
import pandas as pd
import requests

# Page configuration
st.set_page_config(page_title="ASEM Analysis App", layout="wide")

# Title
st.title("ASEM Conference Data Analysis (2015–2024)")

# Load stopwords from GitHub
@st.cache_data
def load_stopwords():
    url = "https://raw.githubusercontent.com/edavgaun/ASEM-Analysis-App/main/Data/own_stopwords.txt"
    response = requests.get(url)
    stopwords = response.text.replace("\n", ", ").split(", ")
    stopwords.sort()
    return stopwords

own_stopwords = load_stopwords()
st.success(f"{len(own_stopwords)} stopwords loaded successfully.")

# Load a sample data file from GitHub
@st.cache_data
def load_sample_data(year):
    url = f"https://raw.githubusercontent.com/edavgaun/ASEM-Analysis-App/main/Data/CP_{year}.csv"
    df = pd.read_csv(url, index_col=0)
    return df

# Year selector
year = st.selectbox("Select year", list(range(2015, 2025)))

# Show preview
try:
    df = load_sample_data(year)
    st.subheader(f"Dataset for {year}")
    st.dataframe(df.head())
except Exception as e:
    st.error(f"Failed to load data for {year}: {e}")

