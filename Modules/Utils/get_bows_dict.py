from Modules.Utils.get_df import get_df
from Modules.Utils.get_corpus import get_corpus
from Modules.Utils.get_tokens import get_tokens
from Modules.Utils.get_bow import get_bow
from Modules.Utils.get_bow_df import get_bow_df
import streamlit as st

def get_bows_dict(start=2015, end=2024):
    dfs, corpuses, tokenses, bows, bow_dfs = {}, {}, {}, {}, {}

    for n in range(end - start + 1):
        try:
            year = start + n
            df = get_df(year)
            corpus = get_corpus(df, year)
            tokens = get_tokens(corpus)

            bow = get_bow(tokens)
            bow_df = get_bow_df(bow)

            dfs[year] = df
            corpuses[year] = corpus
            tokenses[year] = tokens
            bows[year] = bow
            bow_dfs[year] = bow_df

        except Exception as e:
            st.warning(f"❌ Failed for year {year}: {e}")
            continue

    return dfs, corpuses, tokenses, bows, bow_dfs
