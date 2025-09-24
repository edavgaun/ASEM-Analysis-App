import streamlit as st

def set_layout():
    st.set_page_config(layout="wide")
    st.markdown("""
        <style>
            .block-container {
                padding-top: 1.5rem;
                padding-bottom: 1rem;
                padding-left: 2rem;
                padding-right: 2rem;
            }
            .css-18e3th9 {
                padding-top: 0rem !important;
            }
        </style>
    """, unsafe_allow_html=True)


def show_header(text_title):
    st.title(text_title)
    st.caption("📘 Based on: Edgar Avalos-Gauna (2025), *ASEM Uncovered: A Decade of Insights Through Natural Language Processing Data Analysis*")
    st.caption("American Society for Engineering Management (ASEM) 2025 International Annual Conference and 46th Annual Meeting, 24 - 27 September 2025")


def show_umap_instructions():
    st.markdown("""
    ### 🧭 How to Use This App

    This tool lets you explore over 10 years of ASEM conference papers in a 2D space generated using UMAP and LLM-based embeddings.

    - **Filter** by year and topic to narrow down the dataset.
    - Each dot represents a paper. Similar papers appear closer together.
    - **Year Centroids** are shown to help you visualize semantic drift (vertical dashed lines).
    - Hover over points (in Plotly) to see details and explore relationships between topics and years.

    This interface supports meta-analysis, comparative research, and exploration of thematic trends in Engineering Management discussions.
    """)
