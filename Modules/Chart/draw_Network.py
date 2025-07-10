import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as mcolors
import networkx as nx
from collections import Counter
from Modules.Utils.get_topN_word_bow_df import get_topN_word_bow_df
from Modules.Utils.get_word_frq import get_word_frq
from Modules.Utils.get_combinations import get_combinations
from Modules.Utils.get_bows_dict import get_bows_dict

# Load global dicts
dfs, corpuses, tokenses, bows, bow_dfs = get_bows_dict()

def draw_Network(data_year, num_word=10, random_loc=0):
    df = dfs[data_year]
    corpus = corpuses[data_year]
    tokens = tokenses[data_year]
    bow = bows[data_year]
    bow_df = bow_dfs[data_year]

    KW = get_topN_word_bow_df(num_word, bow_df)
    word_frequencies = get_word_frq(bow_df, KW)
    df_comb = get_combinations(df, bow_df, KW)

    G = nx.Graph()
    for _, row in df_comb.iterrows():
        if row["Count"] > 0:
            G.add_edge(row["Word1"], row["Word2"], weight=row["Count"] / num_word)

    node_degrees = dict(G.degree())
    nx.set_node_attributes(G, node_degrees, "degree")

    max_degree = max(node_degrees.values()) if node_degrees else 1
    node_colors = [node_degrees[n] / max_degree for n in G.nodes]

    cmap = cm.plasma
    norm = mcolors.Normalize(vmin=0, vmax=50)
    pos = nx.spring_layout(G, seed=int(random_loc), k=0.7)
    node_sizes = [word_frequencies.get(n, 1) * 5 for n in G.nodes]

    fig, ax = plt.subplots(figsize=(12, 9))
    edge_weights = [d["weight"] * 7 for _, _, d in G.edges(data=True)]
    nx.draw_networkx_edges(G, pos, alpha=0.6, width=edge_weights, edge_color="gray")
    nx.draw_networkx_nodes(
        G, pos, node_size=node_sizes, node_color=node_colors, cmap=cmap, edgecolors="black", alpha=0.9
    )
    nx.draw_networkx_labels(G, pos, font_size=10, font_weight="bold", verticalalignment="top")

    sm = cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])
    cbar = plt.colorbar(sm, ax=ax, fraction=0.02, pad=0.04)
    cbar.set_label("Degree Centrality", fontsize=12)

    plt.title(f"Word Co-occurrence Network, {data_year} (Semantic Clustering)", fontsize=14)
    plt.axis("off")
    return fig
