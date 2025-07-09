import matplotlib.pyplot as plt
import numpy as np
import requests
from io import BytesIO
from PIL import Image
from wordcloud import WordCloud
import streamlit as st
from Modules.Utils.get_dict import get_dict

def draw_word_cloud(bows):
    """
    Uses a fixed word list (get_dict), accumulates word frequencies from all years (2015–2024),
    and generates a WordCloud shaped by the ASEM logo.
    Displays it using Streamlit.
    """
    # Load your stopword dictionary
    own_stopwords = get_dict()
    word_freq = {}

    for word in own_stopwords:
        if len(word) > 2:
            for y in range(2015, 2025):
                try:
                    word_freq[word] += bows[y][word]
                except:
                    try:
                        word_freq[word] = bows[y][word]
                    except:
                        continue

    # Load and process mask image
    logo_url = "https://raw.githubusercontent.com/edavgaun/ASEM-Analysis-App/main/assets/asem_logo.png"
    try:
        response = requests.get(logo_url)
        image = Image.open(BytesIO(response.content)).convert("L")  # grayscale
        mask = np.array(image)
        mask = np.where(mask > 128, 255, 0)  # threshold to binary mask
    except Exception as e:
        st.warning("⚠️ Failed to load mask image. Using blank mask.")
        mask = None

    # Generate word cloud
    wordcloud = WordCloud(
        width=1000,
        height=700,
        mask=mask,
        background_color='white',
        contour_width=0.5,
        contour_color='Blue'
    ).generate_from_frequencies(word_freq)

    # Plot
    fig, ax = plt.subplots(figsize=(5, 2.5))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')

    # Show in Streamlit
    st.pyplot(fig)
