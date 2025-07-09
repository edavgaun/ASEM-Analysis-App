def get_bow(tokens):
    bow_kw = {}
    for token in tokens:
        if (
            not token.is_stop
            and not token.is_punct
            and not token.is_digit
            and len(token) >= 2
        ):
            lemma = token.lemma_
            if lemma in bow_kw:
                bow_kw[lemma] += 1
            else:
                bow_kw[lemma] = 1
    return bow_kw
