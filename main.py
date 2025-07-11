# Libraries
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

@st.cache_resource
def load_nltk_data():
    import nltk
    nltk.download('wordnet')
    nltk.download('omw-1.4')

load_nltk_data()

# Utils imports
from Modules.Utils.get_df import get_df
from Modules.Utils.get_word_frq import get_word_frq
from Modules.Utils.get_tokens import get_tokens
from Modules.Utils.get_bows_dict import get_bows_dict
from Modules.Utils.get_dict import get_dict
own_stopwords = set(get_dict())

# Charts imports
from Modules.Chart.draw_word_cloud import draw_word_cloud
from Modules.Chart.draw_Network import draw_Network
from Modules.Chart.radar_chart import radar_chart
from Modules.Chart.bump_chart import draw_bump_chart



# Variable set up
dfs, corpuses, tokenses, bows, bow_dfs = get_bows_dict()

# Main App
st.set_page_config(layout="wide")

# 🔧 Remove top whitespace and adjust layout
st.markdown("""
    <style>
        /* Remove default padding */
        .block-container {
            padding-top: 0rem;
            padding-bottom: 1rem;
            padding-left: 2rem;
            padding-right: 2rem;
        }
        /* Optional: tweak header spacing */
        .css-18e3th9 {
            padding-top: 0rem !important;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("ASEM Dashboard Explorer, 2015-2024")
st.caption("📘 Based on: Edgar Avalos-Gauna; (2025), *10 Years of ASEM Proceedings*")
st.caption('Avalos-Gauna, E. (2025). ASEM uncovered: A decade of insights through natural language processing data analysis. In Proceedings of the ASEM 2025 International Annual Conference, Boise, ID, USA.')

# Row 1
with st.container():
    col1, col_rest = st.columns([1, 5])


    # --- Column 1: Inputs ---
    with col1:
        year = st.selectbox("Select Year", list(range(2015, 2025)))
        df = get_df(year)
        max_rows = len(df)
        row_range = st.slider(
            "Select row range",
            min_value=0,
            max_value=max_rows - 1,
            value=(0, min(10, max_rows - 1))
        )
        df_slice = df.iloc[row_range[0]:row_range[1] + 1]

    # --- Columns 2–4: Output Tables ---
    with col_rest:
        st.subheader("Conference Papers Overview")
        st.dataframe(df_slice[["Title", "KeyWords", "Abstract", "Paper"]], use_container_width=True)



# Row 2
with st.container():
    col1, col2 = st.columns([2, 3])
    with col1:
        st.subheader("StopWords Cloud, ASEM")
        st.write("Total different words used across all years in bows:", sum(len(b) for b in bows.values()))
        # Count total matching stopwords in bows
        stopword_hits = sum(
            sum(1 for word in bows[year] if word in own_stopwords)
            for year in bows)
        # Optionally, total unique stopwords found:
        unique_stopwords_found = set(
            word for year in bows for word in bows[year] if word in own_stopwords)

        st.write(f"✨ Unique stopwords matched: {len(unique_stopwords_found)}")
        draw_word_cloud(bows)
    
    with col2:
        st.subheader("Keyword Frequency Bubble Chart")
    
        from Modules.Utils.get_wide_df import get_wide_df
        from Modules.Chart.Bubble_chart import Bubble_chart
    
        data_full = get_wide_df()
    
        selected_words = st.multiselect(
            "Select keywords to visualize:",
            options=data_full["Word"].tolist(),
            default=data_full["Word"].head(5).tolist()
        )
    
        if selected_words:
            Bubble_chart(selected_words)
        else:
            st.info("Please select at least one word to display the chart.")


# Row 3
with st.container():
    col1, col_rest = st.columns([1, 5])
    with col1:
        st.subheader("Network Parameters")
        year = st.selectbox("Select Year", list(range(2015, 2025)), key="network_year")
        num_words = st.slider("Top N Words", 5, 100, 20, step=5, key="network_topn")
        seed = st.slider("Random Seed", 0, 100, 42, step=1, key="seed")

    with col_rest:
        st.subheader("Keyword Co-occurrence Network")
        try:
            fig_net = draw_Network(data_year=year, num_word=num_words, random_loc=seed)
            st.pyplot(fig_net, use_container_width=True)
        except Exception as e:
            st.error(f"❌ Failed to render network: {e}")

# Row 4 – Radar Charts
with st.container():
    # First declare the inputs (RIGHT SIDE — col3)
    col1, col2, col3 = st.columns([2, 2, 1.5])

    with col3:
        st.subheader("Radar Settings")
        radar_word = st.text_input("Keyword", value="Leadership", key="radar_word_input")
        topN_words = st.slider("Top N Words", min_value=5, max_value=100, step=5, value=15, key="topN_slider")
        year1 = st.selectbox("Select Year 1", list(range(2015, 2025)), index=2, key="radar_year1")
        year2 = st.selectbox("Select Year 2", list(range(2015, 2025)), index=3, key="radar_year2")

    # Now that inputs exist, safely draw charts
    with col1:
        st.subheader(f"Radar Chart – {year1}")
        fig1, ax1 = plt.subplots(figsize=(6, 5), subplot_kw=dict(polar=True))
        radar_chart(dfs, bow_dfs, year1, radar_word.lower(), topN_words, ax1, color="blue")
        st.pyplot(fig1)

    with col2:
        st.subheader(f"Radar Chart – {year2}")
        fig2, ax2 = plt.subplots(figsize=(6, 5), subplot_kw=dict(polar=True))
        radar_chart(dfs, bow_dfs, year2, radar_word.lower(), topN_words, ax2, color="green")
        st.pyplot(fig2)

# Row 5 – Bump Chart
with st.container():
    col1, col_rest = st.columns([1, 5])

    with col1:
        st.subheader("Bump Chart")
        st.caption("Top ranked words across the years\n– keywords in color were preselected")

    with col_rest:
        #draw_bump_chart(bow_dfs)


