def get_tokens(corpus, nlp_model):
    """
    Tokenizes the cleaned corpus using a provided spaCy language model.
    """
    concepts = [
        t.replace("--", "-").replace("-", " ")
        for t in set(corpus.split(", ")) if len(t) >= 2
    ]
    doc = nlp_model(", ".join(concepts))
    return doc
