def get_tokens(corpus, nlp=nlp):
  concepts=[t.replace("--", "-").replace("-", " ") for t in set(corpus.split(", ")) if len(t)>=2]
  doc = nlp(", ".join(concepts))
  return doc