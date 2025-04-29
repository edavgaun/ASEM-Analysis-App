def draw_Network(data_year, num_word=10, random_loc=0):
  df=dfs[data_year]
  corpus=corpuses[data_year]
  tokens=tokenses[data_year]
  bow=bows[data_year]
  bow_df=bow_dfs[data_year]
  KW=get_topN_word_bow_df(num_word, bow_df)
  word_frequencies = get_word_frq(bow_df, KW)
  df_comb = get_combinations(df, bow_df, KW)

  # Efficient word co-occurrence counting using Counter
  pair_counter = Counter()

  # Create the network graph
  G = nx.Graph()

  # Add edges (word pairs) with weight as count
  for _, row in df_comb.iterrows():
      if row["Count"] > 0:
          G.add_edge(row["Word1"], row["Word2"], weight=row["Count"] / num_word)

  # Compute node degrees
  node_degrees = dict(G.degree())
  nx.set_node_attributes(G, node_degrees, "degree")

  # Normalize node degrees for color mapping
  max_degree = max(node_degrees.values()) if node_degrees else 1
  node_colors = [node_degrees[node] / max_degree for node in G.nodes]

  # Choose a colormap
  cmap = cm.plasma
  norm = mcolors.Normalize(vmin=0, vmax=50)

  # Generate positions using spring layout
  pos = nx.spring_layout(G, seed=int(random_loc), k=0.7)

  # Scale node sizes based on frequency
  node_sizes = [word_frequencies.get(word, 1) * 5 for word in G.nodes()]  # Default size if missing

  # Create figure
  fig, ax = plt.subplots(figsize=(12, 9))

  # Draw edges
  edge_weights = [data["weight"] * 7 for _, _, data in G.edges(data=True)]
  nx.draw_networkx_edges(G, pos, alpha=0.6, width=edge_weights, edge_color="gray")

  # Draw nodes with color mapping (no 'norm' in draw_networkx_nodes)
  nodes = nx.draw_networkx_nodes(
      G, pos, node_size=node_sizes, node_color=node_colors, cmap=cmap, edgecolors="black", alpha=0.9
  )

  # Draw labels
  nx.draw_networkx_labels(G, pos, font_size=10, font_weight="bold", verticalalignment="top")

  # Add colorbar
  sm = cm.ScalarMappable(cmap=cmap, norm=norm)
  sm.set_array([])  # Empty array for colorbar to work
  cbar = plt.colorbar(sm, ax=ax, fraction=0.02, pad=0.04,)
  cbar.set_label("Degree Centrality", fontsize=12)

  # Final adjustments
  plt.title("Word Co-occurrence Network, {} (Semantic Clustering)".format(data_year), fontsize=14)
  plt.axis("off")
  plt.show()