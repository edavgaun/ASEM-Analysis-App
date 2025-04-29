import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st
from utils.constants import YEAR_RANGE, COLOR_RED, COLOR_BLUE, TITLE_FONT_SIZE, LABEL_FONT_SIZE, GRID_STYLE

def radar_chart(year, word, topN_Words, ax, color, dfs, bow_dfs, get_topN_word_bow_df, get_word_frq, get_combinations):
    word = word.lower()
    df = dfs[year]
    bow_df = bow_dfs[year]
    KW = get_topN_word_bow_df(topN_Words, bow_df)
    word_frequencies = get_word_frq(bow_df, KW)
    df_comb = get_combinations(df, bow_df, KW)

    try:
        rank = bow_df[bow_df["Word"] == word].index.values[0]
    except IndexError:
        ax.text(0, 0, f"'{word}' not found in {year}", ha="center", va="center")
        return

    df_comb_word = df_comb[(df_comb.Word1 == word) | (df_comb.Word2 == word)]
    arr = df_comb_word.iloc[:, 1:].values
    df_comb_word.loc[:, "label"] = arr[arr != word]
    df_comb_word = df_comb_word.sort_values("label").reset_index()
    labels = df_comb_word.label.values.tolist()
    values = df_comb_word.Count.values
    norm = np.linalg.norm(values)
    norm_values = list(values / norm) + [values[0] / norm]  # close the loop

    num_vars = len(labels)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angles += angles[:1]

    ax.fill(angles, norm_values, color=color, alpha=0.25)
    ax.plot(angles, norm_values, color=color, linewidth=2)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, fontsize=LABEL_FONT_SIZE)
    ax.set_yticks([0.1, 0.2, 0.3, 0.4, 0.5])
    ax.set_yticklabels([0.1, 0.2, 0.3, 0.4, 0.5])
    ax.text(0, 0, f"{word.upper()}\n{year}\nrank {rank+1}", ha='center', va="center")

def compare_radar_streamlit(word, topN_Words, year1, year2, dfs, bow_dfs, get_topN_word_bow_df, get_word_frq, get_combinations):
    fig, ax = plt.subplots(1, 2, figsize=(14, 6), subplot_kw=dict(polar=True))
    try:
        radar_chart(year1, word, topN_Words, ax[0], COLOR_RED, dfs, bow_dfs, get_topN_word_bow_df, get_word_frq, get_combinations)
    except:
        ax[0].text(0, 0, "Missing data\nfor this topic\nthis year", ha="center", va="center")
    try:
        radar_chart(year2, word, topN_Words, ax[1], COLOR_BLUE, dfs, bow_dfs, get_topN_word_bow_df, get_word_frq, get_combinations)
    except:
        ax[1].text(0, 0, "Missing data\nfor this topic\nthis year", ha="center", va="center")

    fig.suptitle(f'Relationship between "{word.title()}" and Other Topics', fontsize=TITLE_FONT_SIZE, y=1.025)
    st.pyplot(fig)
