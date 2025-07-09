from collections import Counter

def get_word_frq(tokens):
    """
    Returns word frequency dictionary from a list of tokens.
    """
    return Counter(tokens)
