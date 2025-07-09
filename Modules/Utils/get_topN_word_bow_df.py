from Modules.Utils.get_dict import get_dict

def get_topN_word_bow_df(num_word, bow_df, own_stopwords=None):
    if own_stopwords is None:
        own_stopwords = get_dict()
    return bow_df[~bow_df["Word"].isin(own_stopwords)].head(num_word)["Word"].values
