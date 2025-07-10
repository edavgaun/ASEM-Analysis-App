# Modules/Utils/get_bump_data.py
import pandas as pd
import numpy as np
from Modules.Utils.get_dict import get_dict

def get_bump_chart_data(bow_dfs, k=12):
    filter_words = get_dict() + ["  ", "review"]
    table = pd.DataFrame(np.zeros((10, 1 + k)), columns=["Year"] + [f"Top W{n}" for n in range(1, k + 1)])

    for row in range(10):
        year = 2015 + row
        filtered = bow_dfs[year][~bow_dfs[year].Word.isin(filter_words)].head(k)
        topW = [f"({i}), {t}" for i, t in zip(filtered.index.tolist(), filtered.Word.values.tolist())]
        table.at[row, "Year"] = year
        for col, word in enumerate(topW):
            table.iat[row, col + 1] = word

    table["Year"] = table["Year"].astype(int)
    return table
