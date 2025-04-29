import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

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

@st.cache_data
def load_bubble_data():
    url_long = "https://raw.githubusercontent.com/edavgaun/ASEM-Analysis-App/main/Data/df_long.csv"
    url_full = "https://raw.githubusercontent.com/edavgaun/ASEM-Analysis-App/main/Data/data_full.csv"
    df_long = pd.read_csv(url_long)
    data_full = pd.read_csv(url_full, index_col=0)
    return df_long, data_full

df_long, data_full = load_bubble_data()

st.header("📈 Bubble Chart: Word Frequency Over Time")

# Select words
top_words = st.multiselect("Select words to display:", options=sorted(data_full.index), default=[])

if top_words:
    fig, ax = plt.subplots(figsize=(10, len(top_words)))

    sns.scatterplot(
        data=df_long[df_long["Word"].isin(top_words)],
        x="year", y="Word", size="frq", hue="frq",
        palette='Blues', sizes=(100, 3000),
        edgecolor='k', ax=ax, legend=None
    )

    # Add text labels
    for word in top_words:
        for year in range(2015, 2025):
            col_name = f"frq_{year}"
            if col_name in data_full.columns:
                val = data_full.loc[word, col_name]
                if not pd.isna(val):
                    txt_color = "white" if val > 315 else "black"
                    weight = "bold" if val > 315 else "normal"
                    plt.text(year, word, str(int(val)),
                             ha='center', va='center',
                             fontsize=8, color=txt_color, fontweight=weight, alpha=0.8)

    ax.set_ylim(-0.5, len(top_words) - 0.25)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.grid(axis='both', linestyle='--', alpha=0.4)
    plt.tight_layout()
    st.pyplot(fig)
else:
    st.info("Please select one or more words to display the bubble chart.")

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

