import requests

def get_dict():
  url="https://raw.githubusercontent.com/edavgaun/ASEM-Analysis-App/main/Data/own_stopwords.txt"
  response = requests.get(url)
  content = response.text
  content = content.strip().replace("\n", ", ").split(", ")
  content.sort()
  return content
