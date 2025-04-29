import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import streamlit as st
from utils.constants import GRID_STYLE

def plot_bubble_chart(top_words, df_long, data_full):
    if not top_words:
        st.info("Please select one or more words to display the bubble chart.")
        return

    fig, ax = plt.subplots(figsize=(10, len(top_words)))

    sns.scatterplot(
        data=df_long[df_long["Word"].isin(top_words)],
        x="year", y="Word", size="frq", hue="frq",
        palette='Blues', sizes=(100, 3000),
        edgecolor='k', ax=ax, legend=False
    )

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
    plt.grid(**GRID_STYLE)
    plt.tight_layout()
    st.pyplot(fig)
