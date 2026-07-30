# 🎥 AI Video Analyzer

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)
![OpenAI Whisper](https://img.shields.io/badge/OpenAI-Whisper-412991?logo=openai)
![FFmpeg](https://img.shields.io/badge/FFmpeg-Media_Processing-007808?logo=ffmpeg)
![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-black)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT-412991?logo=openai)
![Anthropic](https://img.shields.io/badge/Anthropic-Claude-D97706)
![Pytest](https://img.shields.io/badge/Pytest-Tested-0A9EDC?logo=pytest)
![GitHub Actions](https://img.shields.io/badge/CI-GitHub_Actions-2088FF?logo=githubactions)
![Git](https://img.shields.io/badge/Git-Version_Control-F05032?logo=git)
![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?logo=github)
![License](https://img.shields.io/badge/License-MIT-yellow)

![Repo Size](https://img.shields.io/github/repo-size/satya66123/AI-Video-Analyzer)
![Code Size](https://img.shields.io/github/languages/code-size/satya66123/AI-Video-Analyzer)
![Last Commit](https://img.shields.io/github/last-commit/satya66123/AI-Video-Analyzer)
![Release](https://img.shields.io/github/v/release/satya66123/AI-Video-Analyzer)
![Issues](https://img.shields.io/github/issues/satya66123/AI-Video-Analyzer)
![Pull Requests](https://img.shields.io/github/issues-pr/satya66123/AI-Video-Analyzer)
![Stars](https://img.shields.io/github/stars/satya66123/AI-Video-Analyzer?style=social)
![Forks](https://img.shields.io/github/forks/satya66123/AI-Video-Analyzer?style=social)
[![GitHub Actions](https://github.com/satya66123/AI-Video-Analyzer/actions/workflows/python-app.yml/badge.svg)](https://github.com/satya66123/AI-Video-Analyzer/actions/workflows/python-app.yml)
![Project Status](https://img.shields.io/badge/Project%20Status-Production%20Ready-brightgreen?style=for-the-badge&logo=github)
![Version](https://img.shields.io/badge/Version-v1.0.0-blue?style=for-the-badge&logo=semantic-release)
![Release](https://img.shields.io/badge/Release-Completed-success?style=for-the-badge&logo=checkmarx)
![Build](https://img.shields.io/badge/Build-Stable-success?style=for-the-badge)
![Tests](https://img.shields.io/badge/Tests-Passing-brightgreen?style=for-the-badge&logo=pytest)
![Documentation](https://img.shields.io/badge/Documentation-100%25-success?style=for-the-badge&logo=readthedocs)

# AI-Powered Video Analysis using Whisper & Multiple LLM Providers

*A modular Python application that converts videos into intelligent insights using speech recognition and Large Language Models.*

</div>

---

# 📑 Table of Contents

- Overview
- Features
- Technology Stack
- Architecture
- Project Structure
- Installation
- Usage
- Workflow
- Screenshots
- Testing
- Documentation
- Future Enhancements
- Contributing
- License
- Author

---

# 📌 Overview

AI Video Analyzer is a modular AI-powered application developed using **Python** and **Streamlit**. The application extracts audio from uploaded videos, generates transcripts using **OpenAI Whisper**, analyzes the transcript using multiple AI providers, and exports detailed reports in multiple formats.

The project demonstrates modern software engineering practices including layered architecture, design patterns, automated testing, continuous integration, and comprehensive documentation.

---

# 🚀 Features

- 🎥 Video Upload & Validation
- 🎵 Audio Extraction using FFmpeg
- 🎤 Speech-to-Text using Whisper
- 🤖 AI-Powered Transcript Analysis
- 📝 AI Summary Generation
- 📌 Key Points Extraction
- ✅ Action Items Generation
- 🧠 Multi-Provider AI Support
- 📄 Export Reports (TXT, HTML, Markdown, PDF)
- 📊 Progress Tracking
- 📜 Transcript Management
- ⚠️ Error Handling
- 📋 Structured Logging
- 🧪 Unit Testing
- 🔄 Continuous Integration

---

# 🛠️ Technology Stack

| Category | Technologies |
|-----------|--------------|
| Language | Python |
| Frontend | Streamlit |
| AI Models | Ollama, OpenAI, Anthropic |
| Speech Recognition | Whisper |
| Multimedia | FFmpeg |
| Testing | Pytest, unittest.mock |
| CI/CD | GitHub Actions |
| Version Control | Git & GitHub |

---

# 🏗️ Architecture

```text
                User
                  │
                  ▼
            Streamlit UI
                  │
                  ▼
          Application Layer
                  │
                  ▼
           Service Layer
 ┌──────────┬──────────┬──────────┐
 │          │          │          │
 ▼          ▼          ▼          ▼
Video    Audio    Speech    AIAnalysis
Service  Service  Service    Service
                  │
                  ▼
           Provider Factory
        ┌────────┼────────┐
        ▼        ▼        ▼
     Ollama   OpenAI  Anthropic
```

---

# 📂 Project Structure

```text
AI-Video-Analyzer/
│
├── app.py
├── requirements.txt
├── requirements_test.txt
├── config/
├── providers/
├── services/
├── utils/
├── components/
├── tests/
├── exports/
├── uploads/
├── transcripts/
├── docs/
└── assets/
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/satya66123/AI-Video-Analyzer.git

cd AI-Video-Analyzer
```

## Create Virtual Environment

```bash
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
streamlit run app.py
```

---

# 💻 Usage

1. Launch the Streamlit application.
2. Upload a supported video.
3. Video is validated.
4. Audio is extracted using FFmpeg.
5. Whisper generates a transcript.
6. Select an AI Provider.
7. Generate AI analysis.
8. View summary and insights.
9. Export the report.

---

# 🔄 Workflow

```text
Upload Video
      │
      ▼
Video Validation
      │
      ▼
Audio Extraction
      │
      ▼
Whisper Transcription
      │
      ▼
Prompt Builder
      │
      ▼
Provider Factory
      │
      ▼
AI Analysis
      │
      ▼
Summary & Insights
      │
      ▼
Export Reports
```

---

---

# 📸 Application Screenshots

<div align="center">

![UI](https://img.shields.io/badge/UI-Modern_Streamlit-red?logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)
![Whisper](https://img.shields.io/badge/OpenAI-Whisper-412991?logo=openai&logoColor=white)
![AI](https://img.shields.io/badge/AI-Multi_Provider-success)
![FFmpeg](https://img.shields.io/badge/FFmpeg-Audio_Processing-green?logo=ffmpeg&logoColor=white)
![Screenshots](https://img.shields.io/badge/Screenshots-12-blue)
![Version](https://img.shields.io/badge/v1.0.0-Latest-success)
![Status](https://img.shields.io/badge/Status-Production_Ready-brightgreen)

</div>

These screenshots provide a complete walkthrough of the **AI Video Analyzer** application, demonstrating the workflow from uploading a video to generating AI-powered insights and exporting reports.

---

## 🏠 Home Dashboard

![Home Dashboard](docs/screenshots/home-dashboard.png)

**Highlights**

- Modern Streamlit dashboard
- Navigation sidebar
- Feature overview
- Quick access to all modules

---

## 📤 Video Upload

![Video Upload](docs/screenshots/video-upload.png)

**Highlights**

- Upload MP4, AVI, MOV, MKV, WEBM
- File validation
- Progress indicator

---

## 🎬 Video to Audio

![Video to Audio](docs/screenshots/video-to-audio.png)

**Highlights**

- FFmpeg integration
- Audio extraction
- Processing pipeline

---

## 🎤 Speech-to-Text

<p align="center">
<img src="docs/screenshots/speechtotext1.png" width="48%">
<img src="docs/screenshots/speechtotext2.png" width="48%">
</p>

**Highlights**

- OpenAI Whisper transcription
- Transcript generation
- Language detection

---

## 🔊 Audio Processing

![Audio Processing](docs/screenshots/audio-processing.png)

**Highlights**

- Audio preprocessing
- Metadata extraction
- Audio validation

---

## 🤖 AI Analysis

![AI Analysis](docs/screenshots/analysis.png)
![AI Analysis Hitsory](docs/screenshots/analysishistory.png)


**Highlights**

- AI Summary
- Key Points
- Action Items
- Recommendations
- Multi-Provider AI

---

## 💬 AI Chat

![AI Chat](docs/screenshots/aichat.png)

**Highlights**

- Interactive conversation
- Context-aware responses
- Multiple AI providers

---

## 📄 Reports

![Reports](docs/screenshots/reports.png)

**Highlights**

- Generated reports
- Summary
- Analysis
- Transcript

---

## 📤 Export Center

![Export Center](docs/screenshots/export-center.png)

**Highlights**

- Export to TXT
- Export to Markdown
- Export to HTML
- Export to PDF

---

## ℹ️ About

![About](docs/screenshots/about.png)

**Highlights**

- Project information
- Technologies used
- Version details

---

## ✅ All Tests Passed

![All Tests Passed](docs/screenshots/all-tests-passed.png)

**Highlights**

- Pytest success
- CI-ready project
- Stable codebase

---

## 📷 Complete Screenshot Gallery

For detailed descriptions of every screenshot and the complete application walkthrough, see:

➡️ **[📸 SCREENSHOTS.md](docs/SCREENSHOTS.md)**

---

---

# 🧪 Testing

Run all tests:

```bash
pytest
```

Generate coverage:

```bash
pytest --cov
```

Continuous Integration is configured using GitHub Actions.

---

# 📚 Documentation

Comprehensive documentation is available inside the **docs/** folder.

- INSTALLATION.md
- FEATURES.md
- PROJECT_STRUCTURE.md
- ARCHITECTURE.md
- SYSTEM_DESIGN.md
- USER_GUIDE.md
- API_DOCUMENTATION.md
- PROVIDER_GUIDE.md
- VIDEO_PROCESSING.md
- AUDIO_PROCESSING.md
- AI_ANALYSIS.md
- EXPORT_GUIDE.md
- CONFIGURATION.md
- SECURITY.md
- FAQ.md
- TROUBLESHOOTING.md
- TESTING.md
- WORKFLOW.md
- CHANGELOG.md
- RELEASE_NOTES.md
- CONTRIBUTING.md
- CODE_OF_CONDUCT.md
- IMPLEMENTATION_STEPS.md
- PROJECT_PLANNER.md
- INTERVIEW_QUESTIONS.md
- INTERVIEW_ANSWERS.md
- RESUME_BULLETS.md
- DOCUMENTATION.md
- PROJECT_NOTES.md

---

# 📈 Skills Demonstrated

- Python
- Streamlit
- Whisper
- FFmpeg
- AI Integration
- REST APIs
- Software Architecture
- Factory Pattern
- SOLID Principles
- Dependency Injection
- Object-Oriented Programming
- Clean Code
- Unit Testing
- GitHub Actions
- CI/CD
- Technical Documentation

---

# 🔮 Future Enhancements

- User Authentication
- Database Integration
- Docker Support
- Cloud Deployment
- OCR Integration
- Speaker Diarization
- Batch Processing
- Real-Time Analysis
- Analytics Dashboard
- Kubernetes Deployment

---

# 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push to your branch.
5. Open a Pull Request.

---

# 📄 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Author

**Nekkanti Satya Srinath**

GitHub: https://github.com/satya66123

---

<div align="center">

## ⭐ If you found this project useful, please consider giving it a Star!

**Thank you for visiting the AI Video Analyzer repository!**

</div>