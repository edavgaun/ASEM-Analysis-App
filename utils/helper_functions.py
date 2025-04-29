import numpy as np
import pandas as pd
import streamlit as st

def get_topN_word_bow_df(N, bow_df):
    """Return the top N most frequent words from a bag-of-words DataFrame."""
    return bow_df.sort_values("frq", ascending=False).head(N)["Word"].tolist()

def get_word_frq(bow_df, words):
    """Return a dictionary with word frequencies from the bag-of-words DataFrame."""
    return {word: bow_df.loc[bow_df["Word"] == word, "frq"].values[0] for word in words if word in bow_df["Word"].values}

def get_combinations(df, bow_df, words):
    """Return co-occurrence combinations between the selected words in a DataFrame."""
    from itertools import combinations
    from collections import Counter

    comb_counter = Counter()

    for row in df["Keywords"]:
        tokens = row.lower().split(",")
        tokens = [t.strip() for t in tokens if t.strip() in words]
        comb_counter.update(combinations(sorted(set(tokens)), 2))

    data = [(w1, w2, count) for (w1, w2), count in comb_counter.items()]
    return pd.DataFrame(data, columns=["Word1", "Word2", "Count"])
