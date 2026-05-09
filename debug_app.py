"""
SECTION-2I1 - Fake News Detection
Minimal version for debugging
"""

import streamlit as st
import os
import sys

st.set_page_config(page_title="Fake News Detection - Debug", layout="wide")
st.title("Fake News Detection - Debug Mode")

with st.container():
    st.subheader("Environment Check")
    
    # Check Python version
    st.write(f"Python version: {sys.version}")
    st.write(f"Working directory: {os.getcwd()}")
    
    # List files
    st.write("Files in directory:")
    files = os.listdir('.')
    pkl_files = [f for f in files if f.endswith('.pkl')]
    st.write(f"  - Found {len(pkl_files)} pickle files: {pkl_files}")
    
    # Check imports
    st.write("Checking imports...")
    try:
        import joblib
        st.write("  ✓ joblib imported")
    except Exception as e:
        st.error(f"  ✗ joblib: {e}")
    
    try:
        import sklearn
        st.write(f"  ✓ scikit-learn {sklearn.__version__}")
    except Exception as e:
        st.error(f"  ✗ scikit-learn: {e}")
    
    try:
        import nltk
        st.write("  ✓ nltk imported")
    except Exception as e:
        st.error(f"  ✗ nltk: {e}")
    
    # Try to load models
    st.write("Attempting to load models...")
    try:
        import joblib
        m = joblib.load('fake_news_master_model.pkl')
        st.write(f"  ✓ Model loaded: {type(m)}")
    except Exception as e:
        st.error(f"  ✗ Model error: {type(e).__name__}: {str(e)[:200]}")
    
    try:
        import joblib
        v = joblib.load('tfidf_master_vectorizer.pkl')
        st.write(f"  ✓ Vectorizer loaded: {type(v)}")
    except Exception as e:
        st.error(f"  ✗ Vectorizer error: {type(e).__name__}: {str(e)[:200]}")

st.success("Debug page loaded successfully!")
