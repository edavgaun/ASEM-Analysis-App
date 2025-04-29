import requests
import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Load stopwords from GitHub
def load_stopwords():
    url = "https://raw.githubusercontent.com/edavgaun/ASEM-Analysis-App/main/Data/own_stopwords.txt"
    response = requests.get(url)
    content = response.text.replace("\n", ", ").split(", ")
    content = [word.strip() for word in content if word.strip()]
    return sorted(set(content))
