import numpy as np
from Modules.Utils.get_topN_word_bow_df import get_topN_word_bow_df
from Modules.Utils.get_word_frq import get_word_frq
from Modules.Utils.get_combinations import get_combinations


def radar_chart(dfs, bow_dfs, year, word, topN_Words, ax, color):
    word = word.lower()
    df = dfs[year]
    bow_df = bow_dfs[year]
    KW = get_topN_word_bow_df(topN_Words, bow_df)
    word_frequencies = get_word_frq(bow_df, KW)
    df_comb = get_combinations(df, bow_df, KW)

    if word not in bow_df.Word.values:
        ax.set_title(f"'{word}' not found in top {topN_Words}", fontsize=10)
        return

    rank = bow_df[bow_df["Word"] == word].index.values[0]
    df_comb_word = df_comb[(df_comb.Word1 == word) | (df_comb.Word2 == word)]

    if df_comb_word.empty:
        ax.set_title(f"No co-occurrence data for '{word}'", fontsize=10)
        return

    arr = df_comb_word.iloc[:, 1:].values
    df_comb_word.loc[:, "label"] = arr[arr != word]
    df_comb_word = df_comb_word.sort_values("label").reset_index()

    labels = df_comb_word.label.values.tolist()
    values = df_comb_word.Count.values
    norm = np.linalg.norm(values)
    norm_values = list(values / norm) if norm > 0 else [0] * len(values)

    # Convert to radians for the radar chart
    num_vars = len(labels)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

    # Close the radar chart (connect last point to first)
    norm_values += norm_values[:1]
    angles += angles[:1]

    # Plot the data
    ax.fill(angles, norm_values, color=color, alpha=0.25)  # Fill area
    ax.plot(angles, norm_values, color=color, linewidth=2)  # Line plot

    # Add category labels
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, fontsize=10)
    ax.set_yticks([0.1, 0.2, 0.3, 0.4, 0.5])
    ax.set_yticklabels([0.1, 0.2, 0.3, 0.4, 0.5])

    # Display the chart with annotation
    ax.text(0, 0, f"{word.upper()}\n{year}\nRank {rank + 1}", ha='center', va="center", fontsize=10, fontweight='bold')
