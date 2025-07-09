# Libraries
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Utils imports
from Modules.Utils.get_df import get_df
from Modules.Utils.get_word_frq import get_word_frq
from Modules.Utils.get_tokens import get_tokens
from Modules.Utils.get_bows_dict import get_bows_dict

# Charts imports
from Modules.Chart.draw_word_cloud import draw_word_cloud

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
st.title("ASEM 2025 Dashboard Explorer")

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
    col1, col2 = st.columns(2)
    with col1:
    with col1:
        st.subheader("StopWords Cloud, ASEM")
        draw_word_cloud(bows)
    
    with col2:
        st.subheader("Plot 4 or Input 4")

# Row 3
with st.container():
    col1, col2 = st.columns([1, 5])
    with col1:
        st.subheader("Plot 5 or Input 5")
    with col2:
        st.subheader("Plot 6 or Input 6")

# Row 4
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Plot 7 or Input 7")
    with col2:
        st.subheader("Plot 8 or Input 8")
