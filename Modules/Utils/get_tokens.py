import re

def get_tokens(corpus):
    """
    Tokenizes the corpus into lowercase words using regex.
    Removes punctuation and non-alphabetic tokens.
    """
    # Split on non-alphabetic chars, keep words only
    tokens = re.findall(r'\\b[a-zA-Z]{2,}\\b', corpus.lower())
    return tokens
