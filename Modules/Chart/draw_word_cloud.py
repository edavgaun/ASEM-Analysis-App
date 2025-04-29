def draw_word_cloud(data_year, num_word=10):
  import imageio.v2 as imageio
  from io import BytesIO

  logo_url = "https://raw.githubusercontent.com/edavgaun/ASEM-Analysis-App/main/assets/asem_logo.png"
  df=get_df(data_year)
  corpus=get_corpus(df, data_year)
  tokens=get_tokens(corpus)
  bow=get_bow(tokens)
  bow_df=get_bow_df(bow)
  own_stopwords=get_dict()
  word_freq = dict(zip(bow_df[bow_df.Word.isin(own_stopwords)]['Word'],
                     bow_df[bow_df.Word.isin(own_stopwords)]['frq']))

  response = requests.get(logo_url)
  mask = imageio.imread(BytesIO(response.content))
  mask = np.where(mask > 128, 255, 0)  # Apply a threshold to get a binary mask

  wordcloud = WordCloud(width=1000, height=700, mask=mask,
                        background_color='white',contour_width=0.5, contour_color='Blue'
                        ).generate_from_frequencies(word_freq)

  # Plot the word cloud
  plt.figure(figsize=(10, 5))
  plt.imshow(wordcloud, interpolation='bilinear')
  plt.axis('off')  # Turn off axis labels
  plt.show()