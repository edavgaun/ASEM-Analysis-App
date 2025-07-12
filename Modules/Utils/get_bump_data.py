import pandas as pd
import numpy as np
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords', quiet=True)
from Modules.Utils.get_dict import get_dict
import streamlit as st

def get_bump_data(bow_dfs, k=12, custom_stopwords=None):
    if custom_stopwords is None:
        custom_stopwords = []
    else:
        custom_stopwords=get_dict()

    filter_words = ["  ", "review"] + custom_stopwords
    streamlit_words = ['based', 'data', 'ha', 'keywords', 'used', 'wa']
    filter_words += streamlit_words

    if 'system' in filter_words:
        filter_words.remove('system')
    
    table = pd.DataFrame(np.zeros((10, 1 + k), dtype=object),
                         columns=["Year"] + [f"Top W{n}" for n in range(1, k + 1)])

    for row in range(10):
        year = 2015 + row
        df = bow_dfs[year]
        filtered = df[~df.Word.isin(stopwords.words("english"))].Word.reset_index()
        st.write(filtered.Word)
        filtered = filtered[~filtered.Word.isin(filter_words)].head(k).Word
        topW = [f"({i}), {str(t)}" for i, t in zip(filtered.index.tolist(), filtered.values.tolist())]
        table.loc[row, "Year"] = year
        for col, word in enumerate(topW):
            table.iloc[row, col + 1] = word

    table["Year"] = table["Year"].astype(int)

    bump_words={z:[] for z in set([w.split(", ")[1] for y in table.iloc[:, 1:].values for w in y])}
    for _, row in table.iterrows():
        words_present = {}
        for cell in row[1:]:  # skip Year column
                rank_str, word = cell.split(", ")
                rank = int(rank_str.strip("()"))
                words_present[word] = rank
        
        # For each keyword in bump_words, append rank or np.nan for this year
        for word in bump_words:
            if word in words_present:
                bump_words[word].append(words_present[word]+1)
            else:
                bump_words[word].append(np.nan)

    years = list(range(2015, 2025))
    bump_df = pd.DataFrame(bump_words, index=years)

    return table, bump_df
