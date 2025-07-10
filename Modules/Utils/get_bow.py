from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

def get_bow(tokens):
    bow_kw = {}
    for token in tokens:
        if len(token) < 2:
            continue
        if not token.isalpha():
            continue

        lemma = lemmatizer.lemmatize(token)
        bow_kw[lemma] = bow_kw.get(lemma, 0) + 1
    return bow_kw
