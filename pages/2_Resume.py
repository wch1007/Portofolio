import streamlit as st
from PIL import Image
import os
import requests

# Page configuration
st.set_page_config(
    page_title="Resume | Chenghao Wang - Portfolio",
    page_icon="📄",
    layout="wide",
)

# Custom CSS
def local_css():
    st.markdown("""
    <style>
        .main {
            padding: 2rem 2rem;
        }
        h1, h2, h3 {
            font-family: 'Helvetica', sans-serif;
        }
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        .section-header {
            color: #1E3A8A;
            border-bottom: 2px solid #1E3A8A;
            padding-bottom: 0.5rem;
            margin-top: 2rem;
            margin-bottom: 1rem;
        }
        .resume-section {
            margin-bottom: 2rem;
        }
        .resume-item {
            margin-bottom: 1.5rem;
        }
        .resume-title {
            font-weight: bold;
            font-size: 1.1rem;
            margin-bottom: 0.2rem;
        }
        .resume-subtitle {
            font-style: italic;
            color: #4B5563;
            margin-bottom: 0.5rem;
        }
        .resume-date {
            color: #6B7280;
            font-size: 0.9rem;
        }
        .resume-description {
            margin-top: 0.5rem;
        }
        .skill-tag {
            background-color: #E2E8F0;
            padding: 5px 10px;
            border-radius: 15px;
            font-size: 0.9rem;
            color: #1E3A8A;
            display: inline-block;
            margin-right: 5px;
            margin-bottom: 5px;
        }
        .skills-container {
            margin-top: 15px;
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
        }
        .download-button {
            margin-top: 2rem;
            margin-bottom: 2rem;
        }
        .pdf-container {
            display: flex;
            justify-content: center;
            margin-top: 2rem;
            margin-bottom: 2rem;
        }
        .timeline-item {
            border-left: 2px solid #1E3A8A;
            padding-left: 20px;
            padding-bottom: 20px;
            position: relative;
        }
        .timeline-item:before {
            content: '';
            position: absolute;
            left: -10px;
            top: 0;
            width: 18px;
            height: 18px;
            border-radius: 50%;
            background-color: #1E3A8A;
        }
    </style>
    """, unsafe_allow_html=True)

local_css()

# Page header
st.markdown('<h1 class="section-header">Resume</h1>', unsafe_allow_html=True)
st.write("My professional experience, education, and skills at a glance.")

# Download buttons
st.markdown('<div class="download-button">', unsafe_allow_html=True)

# Define functions to download CV files from GitHub
def get_pdf_from_github(github_url):
    # Convert GitHub HTML URL to raw URL
    raw_url = github_url.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")
    response = requests.get(raw_url)
    return response.content

# English CV download button
english_cv_github_url = "https://github.com/wch1007/Portofolio/blob/master/assets/Resume/English%20CV.pdf"
english_cv_data = get_pdf_from_github(english_cv_github_url)

st.download_button(
    label="📄 Download English Resume",
    data=english_cv_data,
    file_name="Chenghao_Wang_Resume_English.pdf",
    mime="application/pdf",
    key="english_cv"
)

# Chinese CV download button
chinese_cv_github_url = "https://github.com/wch1007/Portofolio/blob/master/assets/Resume/Chinese%20CV.pdf"
chinese_cv_data = get_pdf_from_github(chinese_cv_github_url)

st.download_button(
    label="📄 下载中文简历",
    data=chinese_cv_data,
    file_name="王城昊简历.pdf",
    mime="application/pdf",
    key="chinese_cv"
)

st.markdown('</div>', unsafe_allow_html=True)

# Layout into two columns
col1, col2 = st.columns([2, 1])

with col1:
    # Education section
    st.markdown('<h2 class="section-header">Education</h2>', unsafe_allow_html=True)
    
    st.markdown('<div class="timeline-item">', unsafe_allow_html=True)
    st.markdown('<div class="resume-item">', unsafe_allow_html=True)
    st.markdown('<div class="resume-title">University of Washington</div>', unsafe_allow_html=True)
    st.markdown('<div class="resume-subtitle">M.S.T.I (Master of Science and Technology Innovation) in Robotics</div>', unsafe_allow_html=True)
    st.markdown('<div class="resume-date">September 2024 - March 2026 (Expected)</div>', unsafe_allow_html=True)
    st.markdown('<div class="resume-description">', unsafe_allow_html=True)
    st.markdown("""
    **Courses:**
    - Machine Learning & Signal Processing
    - Robotics Lab
    - Fabrication and Physical Prototyping
    - Sensors and circuits
    - User Research
    - Design Thinking
    - Technology Business Strategy
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="timeline-item">', unsafe_allow_html=True)
    st.markdown('<div class="resume-item">', unsafe_allow_html=True)
    st.markdown('<div class="resume-title">Tsinghua University</div>', unsafe_allow_html=True)
    st.markdown('<div class="resume-subtitle">M.Sc in Data Science | GPA: 3.97/4.0 (Top 10%)</div>', unsafe_allow_html=True)
    st.markdown('<div class="resume-date">September 2023 - June 2024</div>', unsafe_allow_html=True)
    st.markdown('<div class="resume-description">', unsafe_allow_html=True)
    st.markdown("""
    **Achievements:**
    - Pervasive HCI Lab researcher
    - First author of an LBR paper at HRI'2024 conference
    - GIX Academy 1st Place Scholarship
    
    **Courses:**
    - Statistical Machine Learning
    - New Venture Creation
    - Computational Intelligence and Robotics
    - HCI Technology
    - Innovation Entrepreneurship Practice
    - Strategy and Management of Design
    - Pervasive Computing
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="timeline-item">', unsafe_allow_html=True)
    st.markdown('<div class="resume-item">', unsafe_allow_html=True)
    st.markdown('<div class="resume-title">Tsinghua University</div>', unsafe_allow_html=True)
    st.markdown('<div class="resume-subtitle">B.E. in Architecture | GPA: 3.76/4.0 (Top 30%)</div>', unsafe_allow_html=True)
    st.markdown('<div class="resume-date">September 2019 - June 2023</div>', unsafe_allow_html=True)
    st.markdown('<div class="resume-description">', unsafe_allow_html=True)
    st.markdown("""
    **Achievements:**
    - Data Mindset and Practice Certificate
    - Liberal Arts and Science General Education Excellence Certificate
    - College Special Contribution Award
    - Vice Chairman of the Student Union
    - Graduation Speech Representative
    
    **Courses:**
    - Introduction to Data Science
    - Statistical Inference
    - Probability Theory
    - Calculus
    - Programming (C++)
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Professional Experience
    st.markdown('<h2 class="section-header">Professional Experience</h2>', unsafe_allow_html=True)
    
    st.markdown('<div class="timeline-item">', unsafe_allow_html=True)
    st.markdown('<div class="resume-item">', unsafe_allow_html=True)
    st.markdown('<div class="resume-title">Tangwen Zhixin (Beijing) Technology Co., Ltd.</div>', unsafe_allow_html=True)
    st.markdown('<div class="resume-subtitle">Product Director</div>', unsafe_allow_html=True)
    st.markdown('<div class="resume-date">September 2023 - Present</div>', unsafe_allow_html=True)
    st.markdown('<div class="resume-description">', unsafe_allow_html=True)
    st.markdown("""
    - Led the desktop robotics project from scratch as a core founding team member
    - Secured $300,000 seed funding from MiraclePlus
    - Showcased prototype at the China International High-tech Expo (CHITEC)
    - Created PRD, IP character profiles, HCI documentation, and robot motion libraries
    - Completed the technical roadmap for desktop robotics
    - Won multiple top-tier national innovation and entrepreneurship competitions:
      - Silver Award at the 14th Challenge Cup National Competition (Top 1%)
      - Silver Award at 2024 China International Student Innovation Entrepreneurship Competition (Top 1%)
      - 2nd Prize in the 3rd Beijing University Student Innovation Entrepreneurship Competition (Top 1%)
      - Top Ten in Youth Creative Innovation at the 7th "Entrepreneurship Beijing" Competition (Top 1%)
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Publications
    st.markdown('<h2 class="section-header">Publications & Research</h2>', unsafe_allow_html=True)
    st.markdown("""
    - First author of a Late-Breaking Report at HRI'2024 conference on human-robot interaction patterns
    - Research focused on developing natural interaction models for social robots at Tsinghua University's Pervasive HCI Lab
    """)

with col2:
    # Skills section
    st.markdown('<h2 class="section-header">Technical Skills</h2>', unsafe_allow_html=True)
    
    st.markdown("**Coding**")
    st.markdown('<div class="skills-container">', unsafe_allow_html=True)
    for skill in ["Python", "C++", "R"]:
        st.markdown(f'<span class="skill-tag">{skill}</span>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("**Software**")
    st.markdown('<div class="skills-container">', unsafe_allow_html=True)
    for skill in ["MS Office", "Photoshop", "Premiere", "InDesign", "Figma", "Arduino", "Rhino", "Fusion 360", "AutoCAD", "Flutter", "Overleaf"]:
        st.markdown(f'<span class="skill-tag">{skill}</span>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("**Systems & Tools**")
    st.markdown('<div class="skills-container">', unsafe_allow_html=True)
    for skill in ["Ubuntu", "Windows", "Linux", "Cloud Servers", "Command-line scripting", "ROS2"]:
        st.markdown(f'<span class="skill-tag">{skill}</span>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("**Product Development**")
    st.markdown('<div class="skills-container">', unsafe_allow_html=True)
    for skill in ["PRD", "Project Planning", "PMF Analysis"]:
        st.markdown(f'<span class="skill-tag">{skill}</span>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Awards section
    st.markdown('<h2 class="section-header">Awards & Achievements</h2>', unsafe_allow_html=True)
    st.markdown("""
    - Silver Award at the 14th Challenge Cup National Competition
    - Silver Award at 2024 China International Student Innovation Entrepreneurship Competition
    - 2nd Prize in the 3rd Beijing University Student Innovation Entrepreneurship Competition
    - Top Ten in Youth Creative Innovation at the 7th "Entrepreneurship Beijing" Competition
    - GIX Academy 1st Place Scholarship
    - College Special Contribution Award
    - Vice Chairman of the Student Union
    - Graduation Speech Representative
    """)
    
    # Languages section
    st.markdown('<h2 class="section-header">Languages</h2>', unsafe_allow_html=True)
    st.markdown("""
    - Mandarin (Native)
    - English (TOEFL: 111, GRE: 326)
    """)
    
    # Athletic Achievements
    st.markdown('<h2 class="section-header">Athletic Achievements</h2>', unsafe_allow_html=True)
    st.markdown("""
    - **Marathon**: 1st in 2023 Beijing Railway Half Marathon; 4 half marathons, 2 full marathons
    - **Triathlon**: 4th in age group at 2024 Changshu Shanghu Lake International Triatholon Olympic Distance
    - **Cycling**: Beijing to Zhangjiakou (400km) in 2020, around Hainan island (1080km) in 2024
    """)
    
    # Interests
    st.markdown('<h2 class="section-header">Interests</h2>', unsafe_allow_html=True)
    st.markdown('<div class="skills-container">', unsafe_allow_html=True)
    for interest in ["Product Research", "Ultimate Frisbee", "Tennis", "Basketball", "Table Tennis", "Swimming", "Fitness", "Strategic Board Games", "Puzzles"]:
        st.markdown(f'<span class="skill-tag">{interest}</span>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)