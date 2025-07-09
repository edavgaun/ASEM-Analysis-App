from wordcloud import WordCloud
import matplotlib.pyplot as plt

def draw_word_cloud(freq_dict, width=900, height=400, max_words=100, background_color='white'):
    """
    Draws and returns a WordCloud matplotlib figure from a frequency dictionary.
    """
    wc = WordCloud(
        width=width,
        height=height,
        background_color=background_color,
        max_words=max_words
    ).generate_from_frequencies(freq_dict)

    fig, ax = plt.subplots(figsize=(width/100, height/100))
    ax.imshow(wc, interpolation="bilinear")
    ax.axis("off")
    return fig
