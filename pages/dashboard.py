import streamlit as st
from pathlib import Path


def show_dashboard(provider_name, selected_model):

    st.header("📊 Dashboard")

    ########################################################################
    # Folder Statistics
    ########################################################################

    upload_folder = Path("uploads")
    audio_folder = Path("audio")
    transcript_folder = Path("transcripts")
    analysis_folder = Path("analysis")
    chat_folder = Path("chat_history")
    export_folder = Path("exports")

    videos = list(upload_folder.glob("*.*"))
    audio = list(audio_folder.glob("*.*"))
    transcripts = list(transcript_folder.glob("*.txt"))
    analysis = list(analysis_folder.glob("*.md"))
    chats = list(chat_folder.glob("*.json"))
    exports = list(export_folder.glob("*.*"))

    ########################################################################
    # Total Storage
    ########################################################################

    folders = [
        upload_folder,
        audio_folder,
        transcript_folder,
        analysis_folder,
        chat_folder,
        export_folder,
    ]

    total_size = 0

    for folder in folders:

        if folder.exists():

            for file in folder.glob("*.*"):
                total_size += file.stat().st_size

    total_size_mb = total_size / (1024 * 1024)

    st.subheader("📊 Project Statistics")

    row1_col1, row1_col2, row1_col3, row1_col4 = st.columns(4)

    with row1_col1:
        st.metric("📹 Videos", len(videos))

    with row1_col2:
        st.metric("🎵 Audio", len(audio))

    with row1_col3:
        st.metric("📝 Transcripts", len(transcripts))

    with row1_col4:
        st.metric("🤖 Analysis", len(analysis))

    row2_col1, row2_col2, row2_col3, row2_col4 = st.columns(4)

    with row2_col1:
        st.metric("💬 Chats", len(chats))

    with row2_col2:
        st.metric("📤 Exports", len(exports))

    with row2_col3:
        st.metric("💾 Storage", f"{total_size_mb:.2f} MB")

    with row2_col4:
        st.metric("🧠 Model", selected_model)


    st.divider()
    st.divider()

    col1, col2 = st.columns(2)



    ####################################################################
    # Videos
    ####################################################################

    with col1:

        st.subheader("📹 Videos")

        videos = sorted(
            Path("uploads").glob("*.*"),
            reverse=True
        )[:5]

        if videos:

            for file in videos:
                st.write(file.name+"\n")

        else:
            st.caption("No videos")

    ####################################################################
    # Audio
    ####################################################################

    with col2:

        st.subheader("🎵 Audio")

        audios = sorted(
            Path("audio").glob("*.*"),
            reverse=True
        )[:5]

        if audios:

            for file in audios:
                st.write(file.name+"\n")

        else:
            st.caption("No audio")

    st.divider()

    col3, col4 = st.columns(2)


    ####################################################################
    # Transcript
    ####################################################################

    with col3:

        st.subheader("📝 Transcript")

        transcripts = sorted(
            Path("transcripts").glob("*.txt"),
            reverse=True
        )[:5]

        if transcripts:

            for file in transcripts:
                st.write(file.name+"\n")

        else:
            st.caption("No transcripts")

    st.divider()
    col5, col6 = st.columns(2)

    ####################################################################
    # Analysis
    ####################################################################

    with col4:

        st.subheader("🤖 Analysis")

        analysis = sorted(
            Path("analysis").glob("*.md"),
            reverse=True
        )[:5]

        if analysis:

            for file in analysis:
                st.write(file.name+"\n")

        else:
            st.caption("No analysis")

    ####################################################################
    # Chats
    ####################################################################

    with col5:

        st.subheader("💬 Chats")

        chats = sorted(
            Path("chat_history").glob("*.json"),
            reverse=True
        )[:5]

        if chats:

            for file in chats:
                st.write(file.name+"\n")


        else:
            st.caption("No chats")

    ####################################################################
    # Exports
    ####################################################################

    with col6:

        st.subheader("📤 Exports")

        exports = sorted(
            Path("exports").glob("*.*"),
            reverse=True
        )[:5]

        if exports:

            for file in exports:
                st.write(file.name+"\n")


        else:
            st.caption("No exports")

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

        progress = 80

        st.progress(progress)

        st.write(f"Project Completion: **{progress}%**")

        roadmap = [
            "✅ General Setup",
            "✅ Provider Management",
            "✅ Video Upload & Management",
            "✅ Audio Processing",
            "✅ Speech-to-Text",
            "✅ AI Video Analysis",
            "✅ AI Chat",
            "✅ Export & Reports",
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
- Audio extraction done.
- Speech-to-Text done.
- AI-powered video analysis done.
- Chat with your videos will be available in **Phase 6**.
""")