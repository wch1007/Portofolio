import streamlit as st
from PIL import Image
import base64
import os

# Page configuration
st.set_page_config(
    page_title="Chenghao Wang - Portfolio",
    page_icon="🎓",
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
        .stTabs [data-baseweb="tab-list"] {
            gap: 2rem;
        }
        .stTabs [data-baseweb="tab"] {
            height: 4rem;
            white-space: pre-wrap;
            font-size: 1rem;
            font-weight: 600;
            color: #1E3A8A;
        }
        .card {
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 20px;
            background-color: #f8f9fa;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        .profile-img {
            border-radius: 50%;
            width: 200px;
            height: 200px;
            object-fit: cover;
            margin: 0 auto;
            display: block;
            border: 4px solid #1E3A8A;
        }
        .name-header {
            text-align: center;
            color: #1E3A8A;
            font-size: 2.5rem;
            font-weight: bold;
            margin-top: 1rem;
        }
        .subtitle {
            text-align: center;
            color: #4B5563;
            font-size: 1.2rem;
            margin-bottom: 1.5rem;
        }
        .contact-info {
            text-align: center;
            margin-bottom: 2rem;
        }
        .section-header {
            color: #1E3A8A;
            border-bottom: 2px solid #1E3A8A;
            padding-bottom: 0.5rem;
            margin-top: 2rem;
            margin-bottom: 1rem;
        }
        .skills-container {
            display: flex;
            flex-wrap: wrap;
            gap: 4px;
            margin-top: 8px;
            margin-bottom: 15px;
            max-width: 100%;
        }
        .skill-tag {
            background-color: #E2E8F0;
            padding: 4px 8px;
            border-radius: 15px;
            font-size: 0.85rem;
            color: #1E3A8A;
            display: inline-flex;
            margin-right: 4px;
            margin-bottom: 4px;
            white-space: nowrap;
        }
        .project-card {
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 20px;
            background-color: white;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
        }
        .project-card:hover {
            transform: translateY(-5px);
        }
        .social-links {
            text-align: center;
            margin-top: 1rem;
        }
        .social-icon {
            margin: 0 10px;
            color: #1E3A8A;
            font-size: 1.5rem;
        }
    </style>
    """, unsafe_allow_html=True)

local_css()

# Create directories for assets if they don't exist
os.makedirs("assets", exist_ok=True)
os.makedirs("pages", exist_ok=True)

# Home page content
def main():
    # Header section
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown('<div class="profile-container">', unsafe_allow_html=True)
        # Using a placeholder image
        st.markdown('<img src="https://raw.githubusercontent.com/wch1007/Portofolio/master/assets/Images/portrait.jpg" class="profile-img">', unsafe_allow_html=True)
        st.markdown('<h1 class="name-header">Chenghao Wang (Caelan)</h1>', unsafe_allow_html=True)
        st.markdown('<p class="subtitle">Product Enthusiast from Tsinghua University & University of Washington</p>', unsafe_allow_html=True)
        st.markdown('<p class="contact-info">📍 Bellevue, WA; Beijing, China | 📞 (+1) 425-436-4595, (+86) 185-0128-4401 | ✉️ wch1007@uw.edu, wangch23@mails.tsinghua.edu.cn</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # About me section
    st.markdown('<h2 class="section-header">About Me</h2>', unsafe_allow_html=True)
    st.markdown("""
        I am a passionate technologist and innovator pursuing a Master's degree in Science and Technology Innovation 
        with a focus on Robotics at the University of Washington. With a background in Data Science from Tsinghua University 
        and entrepreneurial experience as a Product Director at Tangwen Zhixin Technology, I combine technical expertise 
        with product development skills.
        
        My interests lie at the intersection of robotics, human-computer interaction, and product innovation combining AI and human-centered design. 
        I believe in creating technology that enhances human capabilities and improves quality of life.
    """)
    
    # Education section
    st.markdown('<h2 class="section-header">Education</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("**University of Washington**")
        st.markdown("*M.S.T.I in Robotics (Expected)*")
        st.markdown("September 2024 - March 2026")
        st.markdown("**Courses:** Machine Learning & Signal Processing, Robotics Lab, Fabrication and Physical Prototyping, Sensors and circuits, User Research, Design Thinking, Technology Business Strategy")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("**Tsinghua University**")
        st.markdown("*M.Sc in Data Science* | GPA: 3.97/4.0 (Top 10%)")
        st.markdown("September 2023 - June 2024")
        st.markdown("**Achievements:** Pervasive HCI Lab; first author of an LBR paper at HRI'2024 conference; GIX Academy 1st Place Scholarship")
        st.markdown("**Courses:** Statistical Machine Learning, New Venture Creation, Computational Intelligence and Robotics, HCI Technology, Innovation Entrepreneurship Practice, Strategy and Management of Design, Pervasive Computing")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("**Tsinghua University**")
        st.markdown("*B.E. in Architecture* | GPA: 3.76/4.0 (Top 30%)")
        st.markdown("September 2019 - June 2023")
        st.markdown("**Achievements:** Data Mindset and Practice Certificate, Liberal Arts and Science General Education Excellence Certificate, College Special Contribution Award, Vice Chairman of the Student Union, Graduation Speech Representative")
        st.markdown("**Courses:** Introduction to Data Science, Statistical Inference, Probability Theory, Calculus, Programming(C++)")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Skills section
    st.markdown('<h2 class="section-header">Technical Skills</h2>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("**Coding**")
        st.markdown('<div class="skills-container" style="display: flex; flex-wrap: wrap; gap: 4px; max-width: 100%;">', unsafe_allow_html=True)
        for skill in ["Python", "C++", "R"]:
            st.markdown(f'<span class="skill-tag" style="display: inline-block; white-space: nowrap; background-color: #E2E8F0; padding: 4px 8px; border-radius: 15px; font-size: 0.85rem; color: #1E3A8A; margin-right: 4px; margin-bottom: 4px;">{skill}</span>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col2:
        st.markdown("**Software**")
        st.markdown('<div class="skills-container" style="display: flex; flex-wrap: wrap; gap: 4px; max-width: 100%;">', unsafe_allow_html=True)
        for skill in ["MS Office", "Photoshop", "Premiere", "InDesign", "Figma", "Arduino", "Rhino", "Fusion 360", "AutoCAD", "Flutter", "Overleaf"]:
            st.markdown(f'<span class="skill-tag" style="display: inline-block; white-space: nowrap; background-color: #E2E8F0; padding: 4px 8px; border-radius: 15px; font-size: 0.85rem; color: #1E3A8A; margin-right: 4px; margin-bottom: 4px;">{skill}</span>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown("**Systems & Tools**")
        st.markdown('<div class="skills-container" style="display: flex; flex-wrap: wrap; gap: 4px; max-width: 100%;">', unsafe_allow_html=True)
        for skill in ["Ubuntu", "Windows", "Linux", "Cloud Servers", "Command-line scripting", "ROS2"]:
            st.markdown(f'<span class="skill-tag" style="display: inline-block; white-space: nowrap; background-color: #E2E8F0; padding: 4px 8px; border-radius: 15px; font-size: 0.85rem; color: #1E3A8A; margin-right: 4px; margin-bottom: 4px;">{skill}</span>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col4:
        st.markdown("**Product Development**")
        st.markdown('<div class="skills-container" style="display: flex; flex-wrap: wrap; gap: 4px; max-width: 100%;">', unsafe_allow_html=True)
        for skill in ["PRD", "Project Planning Documentation", "PMF Analysis"]:
            st.markdown(f'<span class="skill-tag" style="display: inline-block; white-space: nowrap; background-color: #E2E8F0; padding: 4px 8px; border-radius: 15px; font-size: 0.85rem; color: #1E3A8A; margin-right: 4px; margin-bottom: 4px;">{skill}</span>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Entrepreneurial section
    st.markdown('<h2 class="section-header">Entrepreneurial Experience</h2>', unsafe_allow_html=True)
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("**Tangwen Zhixin (Beijing) Technology Co., Ltd.**")
    st.markdown("*Product Director*")
    st.markdown("September 2023 - Present")
    st.markdown("""
    - As a core founding team member, led the desktop robotics project from scratch, securing $300,000 seed funding from MiraclePlus and showcasing the prototype at the China International High-tech Expo (CHITEC).
    - As Product Director, created PRD, IP character profiles, HCI documentation, robot motion libraries, and project management documentation, completing the technical roadmap for desktop robotics.
    - As Lead Presenter, won multiple top-tier national innovation and entrepreneurship competitions:
      - Silver Award at the 14th Challenge Cup National Competition (Top 1%)
      - Silver Award at 2024 China International Student Innovation Entrepreneurship Competition (Top 1%)
      - 2nd Prize in the 3rd Beijing University Student Innovation Entrepreneurship Competition (Top 1%)
      - Top Ten in Youth Creative Innovation at the 7th "Entrepreneurship Beijing" Competition (Top 1%)
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Personal section
    st.markdown('<h2 class="section-header">Other Information</h2>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("**Languages**")
        st.markdown("- Mandarin (Native)")
        st.markdown("- English (TOEFL: 111, GRE: 326)")
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('<div class="card">', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("**Athletic Achievements**")
        st.markdown("- Marathon: 1st in 2023 Beijing Railway Half Marathon; 4 half marathons, 2 full marathons")
        st.markdown("- Triathlon: 4th in age group at 2024 Changshu Shanghu Lake International Triatholon Olympic Distance")
        st.markdown("- Cycling: Beijing to Zhangjiakou (400km) in 2020, around Hainan island (1080km) in 2024")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("**Hobbies & Interests**")
        st.markdown('<div class="skills-container" style="display: flex; flex-wrap: wrap; gap: 4px; max-width: 100%;">', unsafe_allow_html=True)
        for hobby in ["Product Research", "Ultimate Frisbee", "Tennis", "Basketball", "Table Tennis", "Swimming", "Fitness", "Strategic Board Games", "Puzzles"]:
            st.markdown(f'<span class="skill-tag" style="display: inline-block; white-space: nowrap; background-color: #E2E8F0; padding: 4px 8px; border-radius: 15px; font-size: 0.85rem; color: #1E3A8A; margin-right: 4px; margin-bottom: 4px;">{hobby}</span>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main() 