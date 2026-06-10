## 🌐 Live Demo
[Try it here!](https://ai-resume-anaalyze.streamlit.app/)

# AI Resume Analyzer 🤖

AI-powered resume analyzer using Groq LLM API.

## Features
- 📄 PDF text extraction using PyMuPDF
- 🤖 Analysis using Groq LLM (Llama 3.3 70B)
- 📊 Overall Score
- 📋 Problems & Solutions Table
- 💡 Improvement Tips
- 🌐 Streamlit Web Interface

## Setup
1. Clone the repo
2. Install dependencies:
pip install groq pymupdf python-dotenv streamlit pandas
3. Create `.env` file:
GROQ_API_KEY=your_key_here
4. Run:
python -m streamlit run app.py

## Tech Stack
- Python
- Groq LLM API (Llama 3.3 70B)
- Streamlit
- PyMuPDF
- Pandas
