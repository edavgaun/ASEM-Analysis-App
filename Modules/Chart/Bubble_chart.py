import requests
from PIL import Image
from io import BytesIO
from wordcloud import WordCloud
from Modules.Utils.get_dict import get_dict

def draw_word_cloud(bows):
    logo_url = "https://raw.githubusercontent.com/edavgaun/ASEM-Analysis-App/main/assets/asem_logo.png"
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

    # Load and process the mask image
    try:
        response = requests.get(logo_url)
        image = Image.open(BytesIO(response.content)).convert("L")  # grayscale
        mask = np.array(image)
        mask = np.where(mask > 128, 255, 0)  # binary mask
    except Exception:
        st.warning("⚠️ Failed to load ASEM logo mask. Using blank mask.")
        mask = None

    wordcloud = WordCloud(
        width=1000,
        height=700,
        mask=mask,
        background_color='white',
        contour_width=0.5,
        contour_color='Blue'
    ).generate_from_frequencies(word_freq)

    # Plot and show in Streamlit
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    st.pyplot(plt.gcf())
