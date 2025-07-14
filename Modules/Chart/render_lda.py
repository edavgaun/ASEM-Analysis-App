import streamlit as st
import streamlit.components.v1 as components
import requests

def render_lda(lda_url):
    try:
        response = requests.get(lda_url)
        response.raise_for_status()
        html_content = response.text
        components.html(html_content, height=800, scrolling=True)
    except requests.exceptions.RequestException as e:
        st.error(f"❌ Could not load LDA visualization from URL.\n\nError: {e}")
