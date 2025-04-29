import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from utils.preprocessing import load_data_full, load_df_long, load_bow_dfs, load_dfs
from utils.text_processing import load_stopwords, load_spacy_model
from utils.constants import YEAR_RANGE, COLOR_RED, GRID_STYLE
from Charts.bubble_chart import plot_bubble_chart
from Charts.radar_chart import compare_radar_streamlit

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
nlp = load_spacy_model()  # Only if needed
st.success(f"The custom stopword dictionary contains {len(own_stopwords)} terms.")

# Load all data
data_full = load_data_full()
df_long = load_df_long()
bow_dfs = load_bow_dfs()
dfs = load_dfs()

# Create bubble chart
top_words = st.multiselect("Select words to display:", options=sorted(data_full.index), default=[])

plot_bubble_chart(top_words, df_long, data_full)

# Create radar chart
compare_radar_streamlit(word, topN_Words, year1, year2, dfs, bow_dfs, get_topN_word_bow_df, get_word_frq, get_combinations)
