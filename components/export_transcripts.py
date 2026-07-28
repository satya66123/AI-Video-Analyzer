import io
import zipfile

import streamlit as st

from utils.transcript_utils import TranscriptUtils


def show_export_transcripts():

    transcripts = TranscriptUtils.list_transcripts()

    if not transcripts:
        return

    zip_buffer = io.BytesIO()

    with zipfile.ZipFile(
        zip_buffer,
        "w",
        zipfile.ZIP_DEFLATED
    ) as zip_file:

        for transcript in transcripts:

            text = TranscriptUtils.read_transcript(
                transcript
            )

            zip_file.writestr(
                transcript,
                text
            )

    st.download_button(
        label="📦 Download All Transcripts",
        data=zip_buffer.getvalue(),
        file_name="transcripts.zip",
        mime="application/zip",
        use_container_width=True
    )