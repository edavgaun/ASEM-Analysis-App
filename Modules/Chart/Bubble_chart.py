def Bubble_chart(*top_words):
  df_long=get_long_df()
  data_full=get_wide_df()
  try:
    top_words = list(top_words)
    top_words.sort()

    df_plot = df_long[df_long.Word.isin(top_words)]

    fig, axs = plt.subplots(figsize=(10, max(2, len(top_words) * 0.9)))

    sns.scatterplot(
        data=df_plot,
        x='year', y='Word', size='frq', hue='frq',
        palette='Blues', sizes=(100, 3000),
        edgecolor='k', ax=axs,
        legend=False
    )

    # Add bubble value annotations
    for index, row in df_plot.iterrows():
        txt_color = "black"
        txt_weight = None
        if row['frq'] > int(df_plot.frq.max()*3/5):
            txt_color = "white"
            txt_weight = "bold"

        axs.text(row['year'], row['Word'], str(row['frq']),
                 ha='center', va='center', fontsize=8, alpha=0.7,
                 color=txt_color, fontweight=txt_weight)

    axs.set_ylim(-0.6, len(top_words) - 0.4)
    axs.grid(axis='both', linestyle='--', alpha=0.4)
    axs.spines['top'].set_visible(False)
    axs.spines['right'].set_visible(False)

    plt.tight_layout()
    plt.show()
  except:
    pass