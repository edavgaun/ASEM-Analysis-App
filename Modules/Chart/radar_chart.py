def radar_chart(year, word, topN_Words, ax, color):
  word=word.lower()
  df=dfs[year]
  bow_df=bow_dfs[year]
  KW=get_topN_word_bow_df(topN_Words, bow_df)
  word_frequencies = get_word_frq(bow_df, KW)
  df_comb=get_combinations(df, bow_df, KW)
  rank=bow_df[bow_df["Word"]==word].index.values[0]
  df_comb_word=df_comb[(df_comb.Word1==word) | (df_comb.Word2==word)]
  arr=df_comb_word.iloc[:,1:].values
  df_comb_word.loc[:, "label"]=arr[arr != word]
  df_comb_word=df_comb_word.sort_values("label").reset_index()
  labels = df_comb_word.label.values.tolist()
  values = df_comb_word.Count.values
  norm = np.linalg.norm(values)
  norm_values=list(values/norm)

  # Convert to radians for the radar chart
  num_vars = len(labels)
  angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

  # Close the radar chart (connect last point to first)
  norm_values += norm_values[:1]
  angles += angles[:1]

  # Plot the data
  ax.fill(angles, norm_values, color=color, alpha=0.25)  # Fill area
  ax.plot(angles, norm_values, color=color, linewidth=2)  # Line plot

  # Add category labels
  ax.set_xticks(angles[:-1])
  ax.set_xticklabels(labels, fontsize=10)
  ax.set_yticks([0.1, 0.2, 0.3, 0.4, 0.5])
  ax.set_yticklabels([0.1, 0.2, 0.3, 0.4, 0.5])

  # Display the chart
  ax.text(0,0,"{}\n{}\nrank{}".format(word.upper(), year,rank+1), ha='center', va="center")