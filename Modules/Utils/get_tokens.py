import re

def get_tokens(corpus):
    tokens = re.findall(r'\b[a-zA-Z]{2,}\b', corpus.lower())
    return tokens
