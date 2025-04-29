def scatterplot3D():
  data_full=get_wide_df().set_index("Word")
  df_long=get_long_df()
  X = data_full.values
  X_embedded = TSNE(n_components=3, learning_rate='auto',
                    init='random', perplexity=3).fit_transform(X)
  df = px.data.iris()
  fig = px.scatter_3d(x=X_embedded[:,0], y=X_embedded[:,1], z=X_embedded[:,2],
                color=data_full.Cluster, size=df_long.groupby("Word")["frq"].sum())
  fig.show()