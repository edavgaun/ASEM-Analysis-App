from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

def get_bow(tokens):
    bow_kw = {}
    for token in tokens:
        token = token.lower()
        if len(token) < 2 or not token.isalpha():
            continue
        stemmed = stemmer.stem(token)
        bow_kw[stemmed] = bow_kw.get(stemmed, 0) + 1
    return bow_kw
