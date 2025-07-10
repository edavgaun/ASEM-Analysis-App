@st.cache_data
def get_radar_data(year, topN_words):
    df = dfs[year]
    bow_df = bow_dfs[year]
    KW = get_topN_word_bow_df(topN_words, bow_df)
    word_frequencies = get_word_frq(bow_df, KW)
    df_comb = get_combinations(df, bow_df, KW)
    return df, bow_df, KW, word_frequencies, df_comb
