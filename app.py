import streamlit as st

from providers.provider_factory import ProviderFactory
from providers.model_manager import ModelManager
from config.settings import Settings
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

st.sidebar.title("⚙ AI Settings")

provider_name = st.sidebar.selectbox(

    "Provider",

    [

        "Ollama",

        "OpenAI",

        "Anthropic"

    ],

    index=0

)

provider = ProviderFactory.get_provider(
    provider_name
)

models = ModelManager.get_models(
    provider_name
)

selected_model = st.sidebar.selectbox(

    "Model",

    models

)

if provider.health_check():

    st.sidebar.success(
        "Provider Connected"
    )

else:

    st.sidebar.error(
        "Provider Not Available"
    )



st.title("🎬 AI Video Analyzer")

if page == "Home":

    st.header("🏠 Home")
    st.info("Welcome to AI Video Analyzer.")

    st.write("---")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Provider",
            provider_name
        )

    with col2:

        st.metric(
            "Model",
            selected_model
        )

elif page == "About":

    st.header("ℹ️ About")

    st.write("""
AI Video Analyzer is a Streamlit application that uses
Artificial Intelligence to analyze videos.

Version: v1.0.0
""")