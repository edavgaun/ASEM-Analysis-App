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


def show_new_section_instructions():
    st.markdown("""
    ### 🧭 Choose a Visualization Tool

    This tab will include links to new sections that are being developed as future contributions to this work.

    - 🧭 **UMAP Embedding Explorer** (Added Sept 2025) 
      Explore papers in a 2D space based on semantic similarity.  
      👉 [Open UMAP Explorer](https://asem-2025-umap.streamlit.app/)

    - 🔍 **BOW TF - IDF Analysis**  (Added Sept-Oct 2025)
      View the most frequent and Distinctive words given a particular Conference and Year.  
      👉 [Open BOW Explorer](https://asem-2025-tf-idf.streamlit.app/)
      
    """, unsafe_allow_html=True)
    
    st.markdown("---")


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
