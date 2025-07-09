import re

def get_bow(tokens):
    bow_kw = {}
    for token in tokens:
        # Filter out tokens with digits, punctuation, or length < 2
        if len(token) < 2:
            continue
        if re.search(r"\d", token):
            continue
        if re.search(r"[\W_]", token):  # non-word characters or underscore
            continue
        bow_kw[token] = bow_kw.get(token, 0) + 1
    return bow_kw
