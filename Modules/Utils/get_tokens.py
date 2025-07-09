import spacy

nlp = spacy.load("en_core_web_sm")

def get_tokens(corpus, nlp_model=nlp):
    """
    Tokenizes the cleaned corpus using spaCy.
    """
    concepts = [
        t.replace("--", "-").replace("-", " ")
        for t in set(corpus.split(", ")) if len(t) >= 2
    ]
    doc = nlp_model(", ".join(concepts))
    return doc
