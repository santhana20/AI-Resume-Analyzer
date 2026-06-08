import streamlit as st
import PyPDF2

st.title("AI Resume Analyzer")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

if uploaded_file is not None:
    pdf_reader = PyPDF2.PdfReader(uploaded_file)

    resume_text = ""
    for page in pdf_reader.pages:
        text = page.extract_text()
        if text:
            resume_text += text

    skills = [
        "Python", "Java", "HTML", "CSS", "JavaScript",
        "SQL", "Data Analytics", "MS Office",
        "Excel", "Web Development"
    ]

    found_skills = []

    for skill in skills:
        if skill.lower() in resume_text.lower():
            found_skills.append(skill)

    missing_skills = [
        skill for skill in skills
        if skill not in found_skills
    ]

    st.subheader("Skills Found")
    if found_skills:
        st.write(found_skills)
    else:
        st.write("No skills found")

    st.subheader("Missing Skills")
    st.write(missing_skills)

    score = int((len(found_skills) / len(skills)) * 100)

    st.subheader("Resume Score")
    st.progress(score)
    st.write(f"Score: {score}%")
