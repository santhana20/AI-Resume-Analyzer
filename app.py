import streamlit as st

st.set_page_config(page_title="AI Resume Analyzer")

st.title("AI Resume Analyzer")

uploaded_file = st.file_uploader("Upload Resume (TXT file)", type=["txt"])

required_skills = [
    "Python",
    "Java",
    "HTML",
    "CSS",
    "SQL",
    "Data Analytics",
    "MS Office"
]

if uploaded_file is not None:
    resume_text = uploaded_file.read().decode("utf-8")

    st.subheader("Resume Content")
    st.text(resume_text)

    found_skills = []
    missing_skills = []

    for skill in required_skills:
        if skill.lower() in resume_text.lower():
            found_skills.append(skill)
        else:
            missing_skills.append(skill)

    st.subheader("Skills Found")
    if found_skills:
        st.success(", ".join(found_skills))
    else:
        st.warning("No matching skills found")

    st.subheader("Missing Skills")
    if missing_skills:
        st.error(", ".join(missing_skills))
    else:
        st.success("All skills found!")

    score = int((len(found_skills) / len(required_skills)) * 100)

    st.subheader("Resume Score")
    st.progress(score)
    st.write(f"Score: {score}/100")