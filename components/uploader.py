import streamlit as st

from services.video_service import VideoService
from utils.file_validator import FileValidator
from utils.video_metadata import VideoMetadata

from components.metadata import show_metadata


def show_uploader():

    uploaded_video = st.file_uploader(

        "Upload Video",

        type=[
            "mp4",
            "avi",
            "mov",
            "mkv",
            "webm"
        ]
    )

    if not uploaded_video:

        return

    valid, message = FileValidator.validate(
        uploaded_video
    )

    if not valid:

        st.error(message)

        return

    progress = st.progress(0)

    filepath = VideoService.save_video(
        uploaded_video,
        progress
    )

    st.success("Video Uploaded Successfully")

    st.video(filepath)

    metadata = VideoMetadata.get_metadata(
        filepath
    )

    if metadata:

        show_metadata(metadata)