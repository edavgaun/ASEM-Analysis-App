import requests
import spacy

# Load stopwords from GitHub
def load_stopwords():
    url = "https://raw.githubusercontent.com/edavgaun/ASEM-Analysis-App/main/Data/own_stopwords.txt"
    response = requests.get(url)
    content = response.text.replace("\n", ", ").split(", ")
    content = [word.strip() for word in content if word.strip()]
    return sorted(set(content))

# Load spaCy model (call this only if needed)
def load_spacy_model():
    try:
        return spacy.load("en_core_web_sm")
    except OSError:
        # Optional: handle installation dynamically
        raise RuntimeError("spaCy model 'en_core_web_sm' is not installed. Please install it before running the app.")
