# Modules/Chart/bump_chart.py
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
from Modules.Utils.get_bump_data import get_bump_chart_data

def draw_bump_chart(bow_dfs):
    table = get_bump_chart_data(bow_dfs)
    years = table["Year"].tolist()

    bump_words = {
        w.split(", ")[1]: [] 
        for row in table.iloc[:, 1:].values 
        for w in row
    }

    # Fill in bump_words with ranks per year
    for i, row in table.iterrows():
        word_ranks = {
            cell.split(", ")[1]: int(cell.split(", ")[0][1:-1]) 
            for cell in row[1:] if isinstance(cell, str)
        }
        for word in bump_words:
            bump_words[word].append(word_ranks.get(word, np.nan) + 1 if word in word_ranks else np.nan)

    bump_df = pd.DataFrame(bump_words, index=years)

    # Visuals
    topics = ["sustainability", "leadership", "energy", "ai", "technology", "team"]
    fz = 12
    colors = sns.color_palette("tab10", n_colors=10)
    fig, axs = plt.subplots(figsize=(12, 6))

    # Plot bump lines
    for i, column in enumerate(bump_df.columns):
        is_topic = column in topics
        axs.plot(
            bump_df.index,
            bump_df[column],
            marker="^" if is_topic else "o",
            alpha=1 if is_topic else 0.25,
            markersize=12,
            label=column if is_topic else None,
            color=colors[topics.index(column)] if is_topic else "gray",
            mec="black"
        )

    # Annotations
    col_index = 0
    for year in years:
        if year % 2 == 1:
            serie = table.T.iloc[1:, col_index].apply(lambda x: x.split(", ")).apply(pd.Series)
            for n in range(len(serie)):
                x = 0.25 + year - 1
                y = int(serie.iloc[n, 0][1:-1]) + 1.25
                word = serie.iloc[n, 1]
                axs.annotate(word, xy=(x, y), ha="left", color="gray", fontsize=fz - 3)
                axs.quiver(x + 0.5, y - 0.4, 0.25, 0, color="gray", scale_units='xy',
                           angles='xy', scale=1.2, width=0.002)
            col_index += 2

    # Formatting
    axs.set_xticks(bump_df.index, labels=years, fontsize=fz)
    axs.set_yticks(
        range(0, int(np.nanmax(bump_df.values)) + 2, 5),
        labels=range(0, int(np.nanmax(bump_df.values)) + 2, 5),
        fontsize=fz
    )
    axs.set_ylim(0, 45)
    axs.set_xlim(2014, 2024.5)
    axs.invert_yaxis()
    axs.set_xlabel("Year", fontsize=fz + 4)
    axs.set_ylabel("Ranking", fontsize=fz + 4)
    axs.grid(which='major', linestyle='--', linewidth='0.5', color='black')
    axs.grid(which='minor', linestyle=':', linewidth='0.5', color='gray')
    plt.legend(title="Keyword", bbox_to_anchor=(1.01, 1), loc='upper left', fontsize=fz)
    plt.tight_layout()
    st.pyplot(fig)
