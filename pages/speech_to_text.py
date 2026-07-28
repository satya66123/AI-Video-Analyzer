import streamlit as st


def show_speech_to_text():

    st.header("📝 Speech-to-Text")

    st.write("""
Convert extracted audio into text.

Features:
- Whisper Transcription
- Timestamp Generation
- Subtitle Generation
- Transcript Download
""")

    st.divider()

    st.info("🚧 This module will be implemented in Phase 4.")