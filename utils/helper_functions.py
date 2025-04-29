import numpy as np
import pandas as pd
import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')
    
def get_corpus(df, year):
  corpus=", ".join([t.lower() if type(t)!=float else "" for t in df.Title.values])
  if year!=2015:
    corpus+=", ".join([t.lower() if type(t)!=float else "" for t in df.KeyWords.values])
  corpus+=", ".join([t.lower() if type(t)!=float else "" for t in df.Abstract.values])
  corpus=", ".join([c.replace(" ", "-").replace(";", ",").replace(".", ",").replace("-,", "") for c in corpus.split(", ")])
  corpus=corpus.replace("4,0", "4.0").replace("5,0", "5.0")
  return corpus

def get_tokens(corpus):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(corpus.lower())
    tokens = [word for word in words if word.isalpha() and word not in stop_words]
    return tokens

def get_bow(tokens):
  bow_kw={}
  for token in tokens:
    if (not token.is_stop) and (not token.is_punct) and (not token.is_digit) \
        and (len(token)>=2):
      try:
        bow_kw[token.lemma_]+=1
      except:
        bow_kw[token.lemma_]=1
  return bow_kw

def get_bow_df(bow):
  df_kw=pd.DataFrame({"Word":bow.keys(), "frq":bow.values()}).sort_values("frq", ascending=False
                                                                                ).reset_index(drop=True)
  return df_kw

def get_topN_word_bow_df(N, bow_df):
    """Return the top N most frequent words from a bag-of-words DataFrame."""
    return bow_df.sort_values("frq", ascending=False).head(N)["Word"].tolist()

def get_word_frq(bow_df, words):
    """Return a dictionary with word frequencies from the bag-of-words DataFrame."""
    return {word: bow_df.loc[bow_df["Word"] == word, "frq"].values[0] for word in words if word in bow_df["Word"].values}

def get_combinations(df, bow_df, words):
    """Return co-occurrence combinations between the selected words in a DataFrame."""
    from itertools import combinations
    from collections import Counter

    comb_counter = Counter()

    for row in df["Keywords"]:
        tokens = row.lower().split(",")
        tokens = [t.strip() for t in tokens if t.strip() in words]
        comb_counter.update(combinations(sorted(set(tokens)), 2))

    data = [(w1, w2, count) for (w1, w2), count in comb_counter.items()]
    return pd.DataFrame(data, columns=["Word1", "Word2", "Count"])
