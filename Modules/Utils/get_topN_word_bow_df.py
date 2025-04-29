def get_topN_word_bow_df(num_word, bow_df, own_stopwords=own_stopwords):
  return bow_df[~bow_df.Word.isin(own_stopwords)].head(num_word).Word.values