def get_bow(tokens):
    bow_kw = {}
    for token in tokens:
        # Filter out tokens with digits, punctuation, or length < 2
        if len(token) < 2:
            continue
        if not token.isalpha():
            continue
        bow_kw[token] = bow_kw.get(token, 0) + 1
    return bow_kw
