from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

def get_dict():
    """
    Returns a sorted list of standard English stopwords
    including the user-defined ones from GitHub.
    """
    import requests

    # GitHub-hosted custom stopwords
    url = "https://raw.githubusercontent.com/edavgaun/ASEM-Analysis-App/main/Data/own_stopwords.txt"
    try:
        response = requests.get(url)
        custom = response.text.strip().replace("\n", ", ").split(", ")
    except Exception as e:
        custom = []

    # Merge and deduplicate with sklearn stopwords
    combined = set(ENGLISH_STOP_WORDS).union(set(custom))
    return sorted([w.strip().lower() for w in combined if w.strip()])
