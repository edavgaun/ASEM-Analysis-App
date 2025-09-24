import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

@st.cache_data
def filter_df(df, selected_years, selected_conferences, selected_topics):
    return df[
        df["Year"].isin(selected_years) &
        df["Conference"].isin(selected_conferences) &
        df["FinalTopicName"].isin(selected_topics)
    ]

def split_label(text, words_per_line=2):
    words = text.split()
    lines = [' '.join(words[i:i + words_per_line]) for i in range(0, len(words), words_per_line)]
    return "<br>".join(lines)

def plot_umap_scatter(df, selected_years=None, selected_conferences=None, selected_topics=None):
    df = filter_df(df, selected_years, selected_conferences, selected_topics)
    df["Year"] = df["Year"].astype(str)

    # Get list of visible topics after filtering
    visible_topics = df["FinalTopicName"].unique()

    # Define full color map
    full_color_map = {
        "Outliers / Uncategorized": "#d3d3d3",
        "Maintenance & Reliability Engineering": "#2ca02c",
        "Sustainability & Green Supply Chains": "#ff7f0e",
        "Industry 4.0 & Smart Manufacturing": "#2ca02c",
        "Project & Construction Management": "#9467bd",
        "Innovation & Entrepreneurship": "#8c564b",
        "Machine Learning Methods": "#e377c2",
        "Employee Behavior & Job Performance": "#17becf",
        "3D Printing & Surface Engineering": "#7f7f7f",
        "Renewable Energy & Power Systems": "#bcbd22",
        "Vehicle Routing & Optimization Problems": "#4b0082",
        "Ergonomics & Worker Safety": "#ff1493",
        "TQM, ISO & Quality Management": "#17becf",
        "Inventory Control & Demand Forecasting": "#ffcc00",
        "Public Policy & Government Programs": "#009e73",
        "Learning, Students & Education": "#e41a1c",
        "Lean Six Sigma & DMAIC": "#377eb8",
        "Customer Experience & Brand Perception": "#f781bf",
        "Supply Chain & Risk Assessment": "#a65628",
        "Financial Markets & Corporate Finance": "#984ea3"
    }

    # Restrict color map to visible topics
    filtered_color_map = {topic: full_color_map.get(topic, "#888888") for topic in visible_topics}

    fig = px.scatter(
        df,
        x="x",
        y="y",
        color="FinalTopicName",
        color_discrete_map=filtered_color_map,
        hover_data={"Title": True, "Year": True, "x": False, "y":False, 'Conference':True},
        opacity=0.6
    )

    fig.update_layout(
        height=800,
        title=(
            "UMAP Projection of IEOM Papers by Thematic Clusters"
            "<br><span style='font-size:14px; font-weight:normal'>"
            "(Use the toolbar at the top-right corner to zoom, pan, and explore → )"
            "</span>"
        ),
        legend_title="Topic",
        showlegend=False,
        xaxis_title=None,
        yaxis_title=None,
        xaxis=dict(showgrid=False, showticklabels=False, zeroline=False),
        yaxis=dict(showgrid=False, showticklabels=False, zeroline=False),
        plot_bgcolor="white"
    )

    for topic in filtered_color_map:
        if "Outlier" in topic:
            continue
        cluster_df = df[df["FinalTopicName"] == topic]
        x_mean = cluster_df["x"].mean()
        y_mean = cluster_df["y"].mean()
        label = split_label(topic)
        delta=0.75
        if y_mean<0:
            delta=-0.75
        fig.add_annotation(
            x=x_mean,
            y=y_mean+delta,
            text=label,
            showarrow=False,
            font=dict(size=12, color="black"),
            bgcolor="rgba(255,255,255,0.7)",
            bordercolor="black",
            borderwidth=1
        )

    return fig, df


def add_centroids_to_umap(
    fig,
    df,
    x_col="x",
    y_col="y",
    year_col="Year",
    padding=0.5,
    line_color="#cccccc",
    line_style="dot",
    line_width=1,
    text_color="#999999"
):
    """
    Add vertical dashed lines at centroid x-positions and label them with vertical year annotations.

    Parameters
    ----------
    fig : plotly.graph_objects.Figure
        The existing figure to be updated.
    df : pd.DataFrame
        DataFrame used for the UMAP plot.
    x_col : str
        Column name for the x-axis UMAP coordinate.
    y_col : str
        Column name for the y-axis UMAP coordinate.
    year_col : str
        Column name for the year grouping.
    padding : float
        Vertical space above the plot used to place the year labels.
    line_color : str
        Hex code for the vertical line color (e.g. "#cccccc").
    line_style : str
        Dash style for the line (e.g. "dot", "dash", "solid").
    line_width : int
        Line thickness.
    text_color : str
        Color for the year label text.

    Returns
    -------
    plotly.graph_objects.Figure
        Updated figure with vertical lines and year annotations.
    """
    # Determine Y-axis range (used for vertical lines and label placement)
    y_range = fig.layout.yaxis.range or [df[y_col].min(), df[y_col].max()]
    y_min, y_max = y_range[0], y_range[1]
    label_y = y_max + padding

    # Iterate through unique years and plot vertical dashed lines + labels
    for year in sorted(df[year_col].unique()):
        sub_df = df[df[year_col] == year]
        if sub_df.empty:
            continue

        centroid_x = sub_df[x_col].mean()

        # Add vertical dashed line
        fig.add_shape(
            type="line",
            x0=centroid_x,
            x1=centroid_x,
            y0=y_min,
            y1=y_max,
            line=dict(color=line_color, width=line_width, dash=line_style),
            layer="below"
        )

        # Add vertical rotated label
        fig.add_annotation(
            x=centroid_x,
            y=label_y,
            text=str(year),
            showarrow=False,
            textangle=90,
            font=dict(color=text_color, size=11),
            xanchor="center",
            yanchor="bottom"
        )
        fig.add_annotation(
        xref="paper",
        yref="paper",
        x=1,
        y=1.01,
        text=(
        "Dashed lines show the average position of <br>"
        " ← papers per year(semantic centroid),<br>" 
        "illustrating how topics shift over time."
        ),
        showarrow=False,
        font=dict(size=12, color="black"),
        align="center"
        )

    return fig
