from collections import Counter

def get_word_frq(tokens):
    """
    Returns word frequency dictionary from a spaCy Doc object.
    Filters out stop words and non-alphabetic tokens.
    """
    words = [
        token.text.lower()
        for token in tokens
        if token.is_alpha and not token.is_stop
    ]
    return Counter(words)
