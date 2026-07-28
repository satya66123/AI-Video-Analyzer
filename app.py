import streamlit as st

st.set_page_config(
    page_title="AI Video Analyzer",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select Page",
    [
        "Home",
        "About"
    ]
)

st.title("🎬 AI Video Analyzer")

if page == "Home":

    st.header("🏠 Home")
    st.info("Welcome to AI Video Analyzer.")

elif page == "About":

    st.header("ℹ️ About")

    st.write("""
AI Video Analyzer is a Streamlit application that uses
Artificial Intelligence to analyze videos.

Version: v1.0.0
""")