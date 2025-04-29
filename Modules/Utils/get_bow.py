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