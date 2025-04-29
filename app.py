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
st.success(f"The custom stopword dictionary contains {len(own_stopwords)} terms.")

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
    freq_cols = [f"frq_{y}" for y in range(2015, 2025)]
    max_val = data_full.loc[top_words, freq_cols].max().max()
    threshold = max_val * 0.6
    
    for word in top_words:
        for year in range(2015, 2025):
            col_name = f"frq_{year}"
            if col_name in data_full.columns:
                val = data_full.loc[word, col_name]
                if not pd.isna(val):
                    txt_color = "white" if val >= threshold else "black"
                    weight = "bold" if val >= threshold else "normal"
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

st.header("📡 Radar Chart: Frequency Pattern of a Word")

# Single word selector
selected_word = st.selectbox("Select a word to view its 10-year frequency pattern:", sorted(data_full.index))

if selected_word:
    # Extract frequency data
    freq_cols = [f"frq_{y}" for y in range(2015, 2025)]
    values = data_full.loc[selected_word, freq_cols].values.tolist()
    
    # Normalize values if needed
    values = [v if not np.isnan(v) else 0 for v in values]

    # Setup labels and angles
    labels = [str(y) for y in range(2015, 2025)]
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
    values += values[:1]  # close the loop
    angles += angles[:1]

    # Plot
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.plot(angles, values, color='teal', linewidth=2)
    ax.fill(angles, values, color='teal', alpha=0.25)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)
    ax.set_title(f"'{selected_word}' Frequency Trend", size=14, weight='bold')
    ax.grid(True, linestyle='--', alpha=0.5)

    st.pyplot(fig)

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

