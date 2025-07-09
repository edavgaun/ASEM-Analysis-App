import streamlit as st
#from eda_dashboard import render_eda
#from lda_viewer import render_lda
#from load_data import get_html_file_map
#from city_map import render_city_map

st.set_page_config(layout="wide")

# 🔧 Remove top whitespace and adjust layout
st.markdown("""
    <style>
        /* Remove default padding */
        .block-container {
            padding-top: 0rem;
            padding-bottom: 1rem;
            padding-left: 2rem;
            padding-right: 2rem;
        }
        /* Optional: tweak header spacing */
        .css-18e3th9 {
            padding-top: 0rem !important;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("ASEM 2025 Dashboard Explorer")

with st.container():
    # Create 4 columns: col1 is narrow (e.g. for controls), col2–col4 are wider (e.g. for plots)
    col1, col2, col3, col4 = st.columns([1, 2, 2, 2])

    with col1:
        st.subheader("Inputs")
        st.selectbox("Choose cluster method", ["KMeans", "DBSCAN", "Agglomerative"])
        st.slider("Top N Words", 5, 50, 20)
        st.text_input("Keyword")

    with col2:
        st.subheader("Plot A")
        # st.plotly_chart(fig1, use_container_width=True)

    with col3:
        st.subheader("Plot B)


# Row 2
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Plot 3 or Input 3")
    with col2:
        st.subheader("Plot 4 or Input 4")

# Row 3
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Plot 5 or Input 5")
    with col2:
        st.subheader("Plot 6 or Input 6")

# Row 4
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Plot 7 or Input 7")
    with col2:
        st.subheader("Plot 8 or Input 8")
