import nltk
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')
try:
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('wordnet')
try:
    nltk.data.find('corpora/omw-1.4')
except LookupError:
    nltk.download('omw-1.4')
import streamlit as st
from utils.preprocessing import load_data_full, load_df_long, load_dfs
from utils.helper_functions import *
from utils.constants import YEAR_RANGE
from utils.text_processing import load_all_stopwords
from Charts.bubble_chart import plot_bubble_chart
from Charts.radar_chart import compare_radar_streamlit

stopwords_url = "https://raw.githubusercontent.com/edavgaun/ASEM-Analysis-App/main/Data/own_stopwords.txt"
combined_stopwords = load_all_stopwords(stopwords_url)

# Load your datasets
data_full = load_data_full()
df_long = load_df_long()
dfs = load_dfs()

# Build Bag of Words for each year
bow_dfs = {}

for year, df in dfs.items():
    corpus = get_corpus(df, year)
    tokens = get_tokens(corpus)  # NLTK version
    bow = get_bow(tokens)         # fixed for NLTK
    bow_df = get_bow_df(bow)       # your existing clean function
    bow_dfs[year] = bow_df

st.title("ASEM Conference Analysis App")

# BUBBLE CHART SECTION
st.header("Bubble Chart: Word Frequencies Across Years")
top_words = st.multiselect("Select words to display:", options=sorted(data_full.index), default=[])

if top_words:
    plot_bubble_chart(top_words, df_long, data_full)
else:
    st.info("Please select one or more words to display the bubble chart.")

# RADAR CHART SECTION
st.header("Radar Chart Comparison")
word = st.text_input("Word to compare (case insensitive):")
topN_Words = st.slider("Top N words for comparison", min_value=10, max_value=200, step=10, value=50)
year1 = st.selectbox("First year", YEAR_RANGE)
year2 = st.selectbox("Second year", YEAR_RANGE)

if word:
    compare_radar_streamlit(word, topN_Words, year1, year2, dfs, bow_dfs, get_topN_word_bow_df, get_word_frq, get_combinations)
