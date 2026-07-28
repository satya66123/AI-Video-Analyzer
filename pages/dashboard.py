import os
import streamlit as st

from services.video_service import VideoService


def show_dashboard(provider_name, selected_model):

    st.header("📊 Dashboard")

    videos = VideoService.list_videos()

    total_size = 0

    for video in videos:

        filepath = os.path.join(
            VideoService.UPLOAD_FOLDER,
            video
        )

        if os.path.exists(filepath):
            total_size += os.path.getsize(filepath)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "📹 Videos",
            len(videos)
        )

    with col2:
        st.metric(
            "💾 Storage",
            f"{total_size / (1024 * 1024):.2f} MB"
        )

    with col3:
        st.metric(
            "🤖 Provider",
            provider_name
        )

    with col4:
        st.metric(
            "🧠 Model",
            selected_model
        )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("📁 Recent Videos")

        if videos:

            recent_videos = sorted(videos, reverse=True)[:5]

            for video in recent_videos:
                st.write(f"🎬 {video}")

        else:
            st.info("No videos uploaded yet.")

    with col2:

        st.subheader("🚀 Project Progress")

        progress = 30

        st.progress(progress)

        st.write(f"Project Completion: **{progress}%**")

        roadmap = [
            "✅ General Setup",
            "✅ Provider Management",
            "✅ Video Upload & Management",
            "⬜ Audio Processing",
            "⬜ Speech-to-Text",
            "⬜ AI Video Analysis",
            "⬜ AI Chat",
            "⬜ Export & Reports",
            "⬜ Testing",
            "⬜ Documentation"
        ]

        for item in roadmap:
            st.write(item)

    st.divider()

    st.subheader("⚙ Current AI Configuration")

    config_col1, config_col2 = st.columns(2)

    with config_col1:
        st.success(f"Provider: {provider_name}")

    with config_col2:
        st.success(f"Model: {selected_model}")

    st.divider()

    st.subheader("📌 Quick Tips")

    st.info("""
- Upload videos from the **Video Upload** page.
- Audio extraction will be available in **Phase 3**.
- Speech-to-Text will be added in **Phase 4**.
- AI-powered video analysis will be available in **Phase 5**.
- Chat with your videos will be available in **Phase 6**.
""")