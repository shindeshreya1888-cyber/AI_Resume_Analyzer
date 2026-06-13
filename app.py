import streamlit as st
import matplotlib.pyplot as plt

# Page Settings
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# Sidebar
st.sidebar.title("📋 Navigation")

st.sidebar.info("""
AI Resume Analyzer

Built Using:
• Python
• Streamlit
• NLP
• Gemini AI
""")

# Main Title
st.title("📄 AI Resume Analyzer")
st.write("Upload your resume and get ATS analysis.")

# Upload Resume
uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

# Sample Dashboard Cards
if uploaded_file:

    st.success("Resume uploaded successfully!")

    # Sample data
    found_skills = 15
    missing_skills = 10
    total_skills = found_skills + missing_skills

    # Job Match Percentage
    job_match = (found_skills / total_skills) * 100

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="ATS Score",
            value="78%"
        )

    with col2:
        st.metric(
            label="Skills Found",
            value=found_skills
        )

    with col3:
        st.metric(
            label="Job Match %",
            value=f"{job_match:.2f}%"
        )

    # Progress Bar
    st.subheader("📊 Job Match Progress")
    st.progress(int(job_match))

    st.write(f"Your resume matches **{job_match:.2f}%** with the job description.")

    # Pie Chart
    st.subheader("📊 Skills Distribution")

    labels = ['Skills Found', 'Missing Skills']
    sizes = [found_skills, missing_skills]

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%')
    ax.axis('equal')  # perfect circle

    st.pyplot(fig)