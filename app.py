from groq import Groq
import os
import pandas as pd
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import fitz
import json


client = Groq(api_key=os.getenv("GROQ_API_KEY"))



if 'page' not in st.session_state:
    st.session_state.page = 'welcome'

if st.session_state.page == 'welcome':
    st.title("🤖 AI Resume Analyzer")
    st.subheader("Get instant AI feedback on your resume!")
    st.write("Upload your resume PDF and get:")
    st.write("✅ Overall Score")
    st.write("✅ Problems & Solutions")  
    st.write("✅ Improvement Tips")
    
    if st.button("Get Started →"):
        st.session_state.page = 'home'
        st.rerun()
elif st.session_state.page == 'home':
    st.title("📄 Upload Your Resume")
    
    uploaded_file = st.file_uploader("Choose your resume PDF", type="pdf")
    
    if uploaded_file is not None:
        if 'analysis_data' not in st.session_state:
            with st.spinner("Analyzing your resume..."):
                doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
                text = ""
                for page in doc:
                    text += page.get_text()

                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {"role": "system", "content": """You are an expert resume analyzer.
    analyze the resume step by step and provide the best solution
    Reply in JSON format only:
    {
        "overall_score": "",
        "issues": [{"problem": "", "solution": ""}],
        "improvements": []
    }"""},
                        {"role": "user", "content": f"Analyze this resume:\n{text}"}
                    ]
                )

                content = response.choices[0].message.content
                content = content.replace("```json", "").replace("```", "").strip()
                st.session_state.analysis_data = json.loads(content)

        # Results dikhao — session state se
        data = st.session_state.analysis_data
        st.success("✅ Analysis Complete!")
        st.metric("Overall Score", f"{data['overall_score']}")
        
        st.subheader("Issues Found")
        table_data = [{"Problem": i['problem'], "Solution": i['solution']} for i in data['issues']]
        st.table(pd.DataFrame(table_data))
        
        st.subheader("Improvements")
        for i, imp in enumerate(data['improvements'], 1):
            st.info(f"{i}. {imp}")
