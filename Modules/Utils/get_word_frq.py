def get_word_frq(bow_df, Top_KW):
    filtered_df = bow_df[bow_df["Word"].isin(Top_KW)]
    return filtered_df.set_index("Word")["frq"].to_dict()
