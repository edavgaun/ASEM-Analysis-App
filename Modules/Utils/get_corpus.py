def get_corpus(df, year):
  corpus=", ".join([t.lower() if type(t)!=float else "" for t in df.Title.values])
  if year!=2015:
    corpus+=", ".join([t.lower() if type(t)!=float else "" for t in df.KeyWords.values])
  corpus+=", ".join([t.lower() if type(t)!=float else "" for t in df.Abstract.values])
  corpus=", ".join([c.replace(" ", "-").replace(";", ",").replace(".", ",").replace("-,", "") for c in corpus.split(", ")])
  corpus=corpus.replace("4,0", "4.0").replace("5,0", "5.0")
  return corpus