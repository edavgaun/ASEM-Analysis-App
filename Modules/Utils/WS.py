def WS():
  data_full=get_wide_df()
  word_selector = widgets.SelectMultiple(
      options=data_full.Word,
      description='Words to choose:',
      rows=5,  # number of rows shown
      style={'description_width': 'initial'},
      layout=widgets.Layout(width='50%')
  )
  return word_selector