import streamlit as st


def show_reports():

    st.header("📄 Reports")

    st.write("""
Generate reports from AI analysis.

Features:
- PDF Report
- DOCX Report
- Markdown Export
- JSON Export
- Analysis History
""")

    st.divider()

    st.info("🚧 This module will be implemented in Phase 7.")