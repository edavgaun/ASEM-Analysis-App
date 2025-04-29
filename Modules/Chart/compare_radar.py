def compare_radar(word, topN_Words, year1, year2):

  fig, ax = plt.subplots(1,2, figsize=(14, 6), subplot_kw=dict(polar=True))
  try:
    radar_chart(year1, word, topN_Words, ax[0], "red")
  except:
    ax[0].text(0,0,"Missing data\nfor this topic\nthis year", ha="center", va="center")
  try:
    radar_chart(year2, word, topN_Words, ax[1], "blue")
  except:
    ax[1].text(0,0,"Missing data\nfor this topic\nthis year", ha="center", va="center")
  plt.suptitle('Relationship between "{}" and Other Topics'.format(
                                                        word.title() ),
                                                        fontsize=20,
                                                        y=1.025)
  plt.show()