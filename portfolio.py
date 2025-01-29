import streamlit as st
from streamlit_lottie import st_lottie
import requests

# Page configuration
st.set_page_config(
    page_title="Arshia Aamena - Portfolio",
    page_icon="👩‍💻",
    layout="wide"
)

# Custom CSS with animations
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

.stApp {
    font-family: 'Poppins', sans-serif;
}

.big-font {
    font-size:60px !important;
    font-weight: bold;
    background: linear-gradient(120deg, #155799, #159957);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 20px;
}

.subtitle {
    font-size: 24px !important;
    color: #666;
    margin-bottom: 30px;
}

.section-title {
    font-size: 36px !important;
    font-weight: bold;
    margin: 40px 0 20px 0;
    background: linear-gradient(120deg, #155799, #159957);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.highlight {
    background: white;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    margin: 15px 0;
    transition: transform 0.3s ease;
}

.highlight:hover {
    transform: translateY(-5px);
}

.skill-box {
    padding: 10px 20px;
    background: linear-gradient(120deg, #155799, #159957);
    color: white;
    border-radius: 25px;
    margin: 5px;
    display: inline-block;
    font-size: 14px;
    transition: transform 0.2s ease;
}

.skill-box:hover {
    transform: scale(1.05);
}

.contact-info {
    font-size: 18px;
    margin: 20px 0;
}

.divider {
    height: 3px;
    background: linear-gradient(120deg, #155799, #159957);
    margin: 40px 0;
    border-radius: 2px;
}

.project-title {
    font-size: 24px !important;
    font-weight: bold;
    color: #155799;
}

hr {
    height: 3px !important;
    background: linear-gradient(120deg, #155799, #159957) !important;
    border: none !important;
    margin: 40px 0 !important;
}
</style>
""", unsafe_allow_html=True)

# Load Lottie animations
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load animations
hero_animation = load_lottie_url("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
project_animation = load_lottie_url("https://assets4.lottiefiles.com/private_files/lf30_wqypnpu5.json")
skills_animation = load_lottie_url("https://assets9.lottiefiles.com/packages/lf20_69HH48.json")

# Hero Section
col1, col2 = st.columns([2, 1])
with col1:
    st.markdown('<p class="big-font">Arshia Aamena</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">🎓 Final Year CSE Student | 💻 MERN Stack Developer | 🤖 AI Enthusiast</p>', unsafe_allow_html=True)
    st.markdown("""
    <div class="contact-info">
        📍 Machilipatnam<br>
        📧 arshiaa245@gmail.com<br>
       
        <a href="https://linkedin.com/in/arshia-aamena" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
        <a href="https://github.com/arshia1234567" target="_blank"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"/></a>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st_lottie(hero_animation, height=300)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Experience Section
st.markdown('<p class="section-title">💼 Experience</p>', unsafe_allow_html=True)
with st.container():
    st.markdown('<div class="highlight">', unsafe_allow_html=True)
    st.markdown("### MERN Stack Intern | SmartInternz")
    st.markdown("*April 2024 - June 2024*")
    st.markdown("""
    - 🚀 Developed dynamic frontends with React, built RESTful APIs with Node.js and Express, and managed MongoDB databases
    - 💪 Specialized in designing and implementing advanced features for a fitness tracker website
    - 🔐 Implemented authentication, authorization, and real-time tracking features
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# Education Section
st.markdown('<p class="section-title">🎓 Education</p>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="highlight">', unsafe_allow_html=True)
    st.markdown("### B.Tech in CSE")
    st.markdown("Seshadri Rao Gudlavalleru Engineering College")
    st.markdown("2021 - Present")
    st.markdown("**CGPA: 9.12/10.00**")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="highlight">', unsafe_allow_html=True)
    st.markdown("### Intermediate")
    st.markdown("Sri Chaitanya Junior College")
    st.markdown("2019 - 2021")
    st.markdown("**Percentage: 97%**")
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="highlight">', unsafe_allow_html=True)
    st.markdown("### SSC")
    st.markdown("Bhashyam")
    st.markdown("2019")
    st.markdown("**GPA: 9.8/10**")
    st.markdown('</div>', unsafe_allow_html=True)

# Skills Section
st.markdown('<p class="section-title">🛠️ Skills</p>', unsafe_allow_html=True)

col1, col2 = st.columns([3, 1])
with col1:
    categories = {
        "Programming Languages": ["Python", "Java", "C", "JavaScript"],
        "Web Technologies": ["HTML5", "CSS3", "PHP", "RESTful APIs"],
        "Frameworks & Libraries": ["React.js", "Node.js", "Django", "LangChain", "Pandas", "Scikit-learn"],
        "Databases & Tools": ["MongoDB", "MySQL", "GitHub", "VS Code", "PowerBI", "Azure"]
    }
    
    for category, skills in categories.items():
        st.markdown(f"### {category}")
        st.markdown('<div class="highlight">', unsafe_allow_html=True)
        for skill in skills:
            st.markdown(f'<span class="skill-box">{skill}</span>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
with col2:
    st_lottie(skills_animation, height=400)

# Projects Section
st.markdown('<p class="section-title">🚀 Projects</p>', unsafe_allow_html=True)

# Project 1
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown('<div class="highlight">', unsafe_allow_html=True)
    st.markdown('<p class="project-title">GenAI-ASKDOC using Gemma</p>', unsafe_allow_html=True)
    st.markdown("**Technologies:** Python, Faiss, Streamlit, Groq API")
    st.markdown("""
    - 🤖 Developed a RAG application for document querying with context-aware responses
    - 🔧 Integrated Groq API with Gemma model and Google embeddings
    - 💻 Created interactive frontend using Streamlit
    """)
    st.markdown('</div>', unsafe_allow_html=True)
with col2:
    st_lottie(project_animation, height=200)

# Project 2
st.markdown('<div class="highlight">', unsafe_allow_html=True)
st.markdown('<p class="project-title">Unravelling Smoking Trends</p>', unsafe_allow_html=True)
st.markdown("**Technologies:** Data Mining, Association Rules, ETL, Orange")
st.markdown("""
- 📊 Implemented ETL pipeline for large staff dataset analysis
- 🔍 Applied association rule mining for pattern discovery
- 📈 Utilized Orange tool for data preprocessing and visualization
""")
st.markdown('</div>', unsafe_allow_html=True)

# Certifications Section
st.markdown('<p class="section-title">🏆 Certifications</p>', unsafe_allow_html=True)
cert_col1, cert_col2, cert_col3 = st.columns(3)

with cert_col1:
    st.markdown('<div class="highlight">', unsafe_allow_html=True)
    st.markdown("### CISCO")
    st.markdown("- Python Essentials")
    st.markdown("- Introduction to Cyber Security")
    st.markdown('</div>', unsafe_allow_html=True)

with cert_col2:
    st.markdown('<div class="highlight">', unsafe_allow_html=True)
    st.markdown("### Microsoft")
    st.markdown("- Azure Data Fundamentals")
    st.markdown('</div>', unsafe_allow_html=True)

with cert_col3:
    st.markdown('<div class="highlight">', unsafe_allow_html=True)
    st.markdown("### GUVI")
    st.markdown("- Generative AI")
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown("""
<div style='text-align: center; color: #666;'>
    Built with ❤️ using Streamlit | 
    <a href='https://linkedin.com/in/arshia-aamena'>LinkedIn</a> | 
    <a href='https://github.com/arshia1234567'>GitHub</a>
</div>
""", unsafe_allow_html=True)