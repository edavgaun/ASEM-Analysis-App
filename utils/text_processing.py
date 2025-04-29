import requests

# Load stopwords from GitHub
def load_stopwords():
    url = "https://raw.githubusercontent.com/edavgaun/ASEM-Analysis-App/main/Data/own_stopwords.txt"
    response = requests.get(url)
    content = response.text.replace("\n", ", ").split(", ")
    content = [word.strip() for word in content if word.strip()]
    return sorted(set(content))

# Load spaCy model (call this only if needed)
def load_spacy_model():
    import spacy
    try:
        nlp = spacy.load("en_core_web_sm")
    except OSError:
        from spacy.cli import download
        download("en_core_web_sm")
        nlp = spacy.load("en_core_web_sm")
    return nlp
