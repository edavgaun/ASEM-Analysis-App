import requests
import nltk
from nltk.corpus import stopwords

def load_nltk_stopwords():
    """
    Load default English stopwords from NLTK.
    """
    try:
        nltk.data.find("corpora/stopwords")
    except LookupError:
        nltk.download("stopwords")
    return set(stopwords.words("english"))

def load_own_stopwords(url):
    """
    Load custom stopwords from your GitHub-hosted .txt file.
    """
    response = requests.get(url)
    content = response.text
    custom_stops = content.replace("\n", ", ").split(", ")
    custom_stops = [word.strip() for word in custom_stops if word.strip()]
    return set(custom_stops)

def load_all_stopwords(own_url):
    """
    Combine NLTK and custom stopwords into one set.
    """
    nltk_stops = load_nltk_stopwords()
    own_stops = load_own_stopwords(own_url)
    combined = nltk_stops.union(own_stops)
    return sorted(combined)
