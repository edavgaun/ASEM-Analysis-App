import streamlit as st
import pandas as pd
from Modules.Chart.plot_umap import plot_umap_scatter, add_centroids_to_umap
from Modules.Utils.UI import set_layout, show_header, show_umap_instructions

# Load dataset
@st.cache_data
def load_data():
    return pd.read_json("Data/ieom_full.json.gz", compression="gzip")

df = load_data()

# Layout
set_layout()

# Header
show_header("🗺️ UMAP Embedding Explorer")

# Instructions
show_umap_instructions()

# Filters
selected_years = st.multiselect(
    "Select Years", sorted(df["Year"].unique()), default=sorted(df["Year"].unique())
)

selected_conferences = st.multiselect(
    "Select Conferences", sorted(df["Conference"].unique()), default=sorted(df["Conference"].unique())
)

selected_topics = st.multiselect(
    "Select Topics", options=df["FinalTopicName"].unique(), default=df["FinalTopicName"].unique()
)

# Plot UMAP
fig, filt_df = plot_umap_scatter(
    df,
    selected_years=selected_years,
    selected_conferences=selected_conferences,
    selected_topics=selected_topics
)

fig = add_centroids_to_umap(fig, filt_df)
st.plotly_chart(fig, use_container_width=True)
