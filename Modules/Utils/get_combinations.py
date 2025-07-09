import pandas as pd
from collections import Counter
from itertools import combinations

def get_combinations(df, bow_df, KW_values):
    # Initialize co-occurrence counter
    pair_counter = Counter()

    # Process each paper efficiently
    for paper in df["Paper"].dropna():
        words_in_paper = set(paper.split())
        for w1, w2 in combinations(KW_values, 2):
            if w1 in words_in_paper and w2 in words_in_paper:
                pair_counter[(w1, w2)] += 1

    # Convert the Counter dictionary to a DataFrame
    df_comb = pd.DataFrame(pair_counter.items(), columns=["Word_Pair", "Count"])
    df_comb[["Word1", "Word2"]] = pd.DataFrame(df_comb["Word_Pair"].tolist(), index=df_comb.index)
    df_comb.drop(columns=["Word_Pair"], inplace=True)

    return df_comb
