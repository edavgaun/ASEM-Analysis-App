def get_word_frq(bow_df, Top_KW):
  return bow_df[bow_df.Word.isin(Top_KW)].set_index("Word").to_dict()["frq"]