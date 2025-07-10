import pandas as pd
import numpy as np
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords', quiet=True)
from Modules.Utils.get_dict import get_dict

def get_bump_data(bow_dfs, k=12):
    filter_words = stopwords.words("english") + get_dict() + ["  ", "review"]
    table = pd.DataFrame(np.zeros((10, 1 + k), dtype=object),
                         columns=["Year"] + [f"Top W{n}" for n in range(1, k + 1)])

    for row in range(10):
        year = 2015 + row
        df = bow_dfs[year]
        filtered = df[~df.Word.isin(filter_words)].head(k).Word
        topW = [f"({i}), {str(t)}" for i, t in zip(filtered.index.tolist(), filtered.values.tolist())]
        table.at[row, "Year"] = year
        for col, word in enumerate(topW):
            table.iat[row, col + 1] = word

    table["Year"] = table["Year"].astype(int)

    bump_words = {
        word: [] for word in
        set(w.split(", ")[1] for w in table.iloc[:, 1:].values.flatten() if pd.notna(w))
    }

    for _, row in table.iterrows():
        words_present = {}
        for cell in row[1:]:
            if pd.notna(cell):
                rank_str, word = cell.split(", ")
                rank = int(rank_str.strip("()"))
                words_present[word] = rank
        for word in bump_words:
            bump_words[word].append(words_present.get(word, np.nan))

    years = list(range(2015, 2025))
    bump_df = pd.DataFrame(bump_words, index=years)

    return table, bump_df
