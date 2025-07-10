import pandas as pd
import numpy as np
from Modules.Utils.get_dict import get_dict

def get_bump_chart_data(bow_dfs, k=12):
    filter_words = get_dict() + ["  ", "review"]
    table = pd.DataFrame(np.zeros((10, 1 + k)), columns=["Year"] + ["Top W" + str(n) for n in range(1, 1 + k)])
    for row in range(10):
        year = 2015 + row
        temp = bow_dfs[year][~bow_dfs[year].Word.isin(filter_words)].head(k).Word
        topW = [f"({i}), {str(t)}" for i, t in zip(temp.index.tolist(), temp.values.tolist())]
        table.loc[row, "Year"] = year
        for col, word in enumerate(topW):
            table.iloc[row, col + 1] = word
    table["Year"] = table["Year"].astype(int)
    return table
