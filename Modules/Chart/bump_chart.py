import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import numpy as np
from Modules.Utils.get_bump_data import get_bump_data

def draw_bump_chart(bow_dfs):
    table, bump_df = get_bump_data(bow_dfs)
    years = list(range(2015, 2025))
    fz = 12
    topics = ["sustainability", "leadership", "energy", "ai", "technology", "team"]
    colors = sns.color_palette("tab10", n_colors=10)

    # If all values are NaN, stop and show error
    if np.isnan(bump_df.values).all():
        st.error("No data to plot — all keywords were filtered out. Check your stopwords or data.")
        st.dataframe(bump_df)
        st.stop()

    fig, axs = plt.subplots(figsize=(12, 6))
    k = 0
    for column in bump_df.columns:
        color = "Gray"
        alpha = 0.25
        marker = "o"
        if column in topics:
            color = colors[k]
            k += 1
            alpha = 1
            marker = "^"
            axs.plot(bump_df.index, bump_df[column], marker=marker, alpha=alpha,
                     markersize=12, label=column, color=color, mec="Black")
        else:
            axs.plot(bump_df.index, bump_df[column], marker=marker, alpha=alpha,
                     markersize=12, color=color, mec="Black")

    for year in years:
        if year % 2 == 1:
            try:
                serie = table.T.iloc[1:, year - 2015].apply(
                    lambda x: x.split(", ") if isinstance(x, str) else ["(0)", ""]
                ).apply(pd.Series)
                for n in range(len(serie)):
                    x = 0.25 + year - 1
                    y = int(serie.iloc[n, 0][1:-1]) + 1.25
                    text = serie.iloc[n, 1]
                    axs.annotate(text, xy=(x, y), ha="left", color="Gray", fontsize=fz - 3)
                    axs.quiver(x + 0.5, y - 0.4, 0.25, 0, color="gray", scale_units='xy',
                               angles='xy', scale=1.2, width=0.002)
            except Exception as e:
                st.warning(f"Annotation error for year {year}: {e}")
                continue

    max_rank = int(np.nanmax(bump_df.values)) + 2
    axs.set_yticks(range(0, max_rank, 5),
                   labels=range(0, max_rank, 5),
                   fontsize=fz)
    axs.set_xticks(bump_df.index, labels=years, fontsize=fz)
    axs.set_ylim(0, 45)
    axs.set_xlim(2014, 2024.5)
    axs.invert_yaxis()
    axs.set_xlabel("Year", fontsize=fz + 4)
    axs.set_ylabel("Ranking", fontsize=fz + 4)
    axs.grid(which='major', linestyle='--', linewidth='0.5', color='Black')
    axs.grid(which='minor', linestyle=':', linewidth='0.5', color='Gray')
    plt.legend(title="Keyword", bbox_to_anchor=(1.01, 1), loc='upper left', fontsize=fz)
    plt.tight_layout()
    st.pyplot(fig)
