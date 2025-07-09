import streamlit as st
import re

def get_tokens(corpus):
    tokens = re.findall(r'\b[a-zA-Z]{2,}\b', corpus.lower())
    st.write(f"Token sample: {tokens[:10]}")
    return tokens
